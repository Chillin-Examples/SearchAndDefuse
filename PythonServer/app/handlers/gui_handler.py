# -*- coding: utf-8 -*-

# python imports
from __future__ import division
import math

# chillin imports
from chillin_server.gui import scene_actions

# project imports
from ..ks.commands import *
from ..gui_events import GuiEventType
from ..handlers.game_status import GameStatus
from ..ks.models import *


class GuiHandler:

    def __init__(self, world, sides, scene):
        self._world = world
        self._sides = sides
        self._scene = scene
        self._rm = scene.rm


    def initialize(self, config):
        self._init_contants(config)
        self._init_variables()

        # draw
        self._init_light()
        self._init_camera()
        self._init_sounds()
        self._draw_board()
        self._draw_agents()
        self._init_fow()
        self._update_fow()

        # Status
        self._game_status = GameStatus(self._world, self._sides, self._scene)
        self._game_status.initialize()
        self._game_status.draw()

        # Add EndCycle
        self._scene.add_action(scene_actions.EndCycle())


    def _init_contants(self, config):
        self.CELL_SIZE = config['cell_size']
        self.X_OFFSET = -self._world.width / 2.0 * self.CELL_SIZE
        self.Z_OFFSET = -self._world.height / 2.0 * self.CELL_SIZE

        self.DIR_TO_ANGLE = {
            ECommandDirection.Up.name:    0,
            ECommandDirection.Right.name: 90,
            ECommandDirection.Down.name:  180,
            ECommandDirection.Left.name:  -90
        }
        self.FOW_Y = 10
        self.TOTAL_SKINS_MATERIALS = 4

        self.POLICE_SKINS = ['MaleSWAT', 'FemaleFBI', 'FemaleShirt', 'MaleFBI']
        self.POLICE_MATERIAL_OFFSETS = [0, 2, 2, 0]
        self.POLICE_HEADS = [[None], [None], ['WomanHair'], [None]]
        self.POLICE_ITEMS = [[None]]

        self.TERRORIST_SKINS = ['MaleSuitVest', 'FemaleSuitVest', 'MaleOverall', 'FemaleOverall']
        self.TERRORIST_MATERIAL_OFFSETS = [0, 2, 2, 0]
        self.TERRORIST_HEADS = [['Clown'], ['Chicken'], ['ManHair', 'WeldersMask'], ['Trump'],
                                ['Horse'], ['Tiger'], ['Panda'], ['Balaclava'],
                                ['ManHair', 'Fox'], ['Hat'], ['ManHair', 'Hockey'], ['Paperbag']]
        self.TERRORIST_ITEMS = [[None]]


    def _init_variables(self):
        self._agents_ref = {side: {} for side in self._sides}
        self._fows_ref = {}
        self._hidden_fows_pos = [] # fog of wars that are hidden because of the visions


    def _init_light(self):
        main_light = self._rm.new()
        self._scene.add_action(scene_actions.CreateBasicObject(
            ref = main_light,
            type = scene_actions.EBasicObjectType.Light
        ))
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = main_light,
            rotation = scene_actions.Vector3(x=90, y=0, z=0)
        ))
        self._scene.add_action(scene_actions.ChangeLight(
            ref = main_light,
            shadow_strength = 0.7
        ))


    def _init_camera(self):
        fov = 60 # TODO: calculate
        extra_camera_boundry = -5

        self._scene.add_action(scene_actions.ChangeCamera(
            ref = self._rm.get('MainCamera'),
            is_orthographic = False,
            field_of_view = fov,
            min_position = scene_actions.Vector3(x=(self.X_OFFSET + extra_camera_boundry), y=1, z=(self.Z_OFFSET + extra_camera_boundry)),
            max_position = scene_actions.Vector3(x=-(self.X_OFFSET + extra_camera_boundry), y=100, z=-(self.Z_OFFSET + extra_camera_boundry)),
            min_zoom = fov - 20,
            max_zoom = fov + 40
        ))
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = self._rm.get('MainCamera'),
            position = scene_actions.Vector3(x=0, y=10, z=(self.Z_OFFSET + extra_camera_boundry)),
            rotation = scene_actions.Vector3(x=30, y=0, z=0)
        ))


    def _init_sounds(self):
        pass


    def _draw_board(self):
        for y in range(self._world.height):
            for x in range(self._world.width):
                cell = self._world.board[y][x]
                pos = self._get_scene_position(Position(x=x, y=y))
                reference = self._rm.new()

                # Draw non-player cells
                if cell == ECell.Empty:
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Floor1')
                    ))

                elif cell == ECell.Wall:
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Wall')
                    ))

                elif cell == ECell.SmallBombSite:
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Floor2')
                    ))

                elif cell == ECell.MediumBombSite:
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Floor2')
                    ))

                elif cell == ECell.LargeBombSite:
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Floor2')
                    ))

                elif cell == ECell.VastBombSite:
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Floor2')
                    ))

                else:
                    self._rm.remove(reference)
                    continue

                # Set Position
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = reference,
                    position = scene_actions.Vector3(x=pos['x'], z=pos['z'])
                ))


    def _draw_agents(self):
        for side in self._sides:
            agents = self._world.polices if side == 'Police' else self._world.terrorists
            skins = self.POLICE_SKINS if side == 'Police' else self.TERRORIST_SKINS
            material_offsets = self.POLICE_MATERIAL_OFFSETS if side == 'Police' else self.TERRORIST_MATERIAL_OFFSETS
            heads = self.POLICE_HEADS if side == 'Police' else self.TERRORIST_HEADS
            items = self.POLICE_ITEMS if side == 'Police' else self.TERRORIST_ITEMS

            for agent in agents:
                pos = self._get_scene_position(agent.position)
                reference = self._rm.new()
                self._agents_ref[side][agent.id] = reference

                self._scene.add_action(scene_actions.InstantiateBundleAsset(
                    ref = reference,
                    asset = scene_actions.Asset(bundle_name='main', asset_name=side)
                ))

                # set ID
                self._scene.add_action(scene_actions.ChangeText(
                    ref = reference,
                    child_ref = 'Root/Hips/Spine_01/Spine_02/Spine_03/Neck/Head/Canvas/ID',
                    text = str(agent.id)
                ))

                # set appearance
                skin = skins[agent.id % len(skins)]
                self._scene.add_action(scene_actions.ChangeIsActive(
                    ref = reference,
                    child_ref = 'Skin/{0}'.format(skin),
                    is_active = True
                ))

                material_num = (((agent.id // len(material_offsets)) + material_offsets[agent.id % len(material_offsets)]) % self.TOTAL_SKINS_MATERIALS) + 1
                self._scene.add_action(scene_actions.ChangeMaterial(
                    ref = reference,
                    child_ref = 'Skin/{0}'.format(skin),
                    material_asset = scene_actions.Asset(bundle_name='main', asset_name='Material{:d}'.format(material_num)),
                    index = 0
                ))

                for head in heads[agent.id % len(heads)]:
                    if head == None:
                        continue
                    self._scene.add_action(scene_actions.ChangeIsActive(
                        ref = reference,
                        child_ref = 'Root/Hips/Spine_01/Spine_02/Spine_03/Neck/Head/HeadMask/{0}'.format(head),
                        is_active = True
                    ))

                for item in items[agent.id % len(items)]:
                    if item == None:
                        continue
                    self._scene.add_action(scene_actions.ChangeIsActive(
                        ref = reference,
                        child_ref = 'Root/Hips/Items/{0}'.format(item),
                        is_active = True
                    ))

                gun = 'Rifle' if side == 'Police' else 'Pistol'
                self._scene.add_action(scene_actions.ChangeIsActive(
                    ref = reference,
                    child_ref = 'Root/Hips/Spine_01/Spine_02/Spine_03/Clavicle_R/Shoulder_R/Elbow_R/Hand_R/{0}'.format(gun),
                    is_active = True
                ))

                # set position
                direction = ECommandDirection.Right if side == 'Police' else ECommandDirection.Left
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = reference,
                    position = scene_actions.Vector3(x=pos['x'], z=pos['z']),
                    rotation = scene_actions.Vector3(y=self.DIR_TO_ANGLE[direction.name])
                ))


    def _init_fow(self):
        for y in range(self._world.height):
            for x in range(self._world.width):
                reference = self._rm.new()
                self._fows_ref[(x, y)] = reference
                pos = self._get_scene_position(Position(x=x, y=y))

                self._scene.add_action(scene_actions.InstantiateBundleAsset(
                    ref = reference,
                    asset = scene_actions.Asset(bundle_name='main', asset_name='FOW')
                ))
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = reference,
                    position = scene_actions.Vector3(x=pos['x'], y=self.FOW_Y, z=pos['z'])
                ))


    def _update_fow(self):
        new_hidden_fows_pos = []

        for side in self._sides:
            for visible_pos in self._world.visions[side]:
                pos = (visible_pos.x, visible_pos.y)
                new_hidden_fows_pos.append(pos)

                if not pos in self._hidden_fows_pos:
                    self._hidden_fows_pos.append(pos)
                    self._scene.add_action(scene_actions.ChangeIsActive(
                        ref = self._fows_ref[pos],
                        is_active = False
                    ))

        must_remove_pos = []
        for pos in self._hidden_fows_pos:
            if not pos in new_hidden_fows_pos:
                must_remove_pos.append(pos)
        for pos in must_remove_pos:
            self._hidden_fows_pos.remove(pos)
            self._scene.add_action(scene_actions.ChangeIsActive(
                ref = self._fows_ref[pos],
                is_active = True
            ))


    def update(self, current_cycle, gui_events):
        moving_terrorists, moving_polices, bombs_defusing, bombs_defused, bombs_op_canceled = [], [], [], [], []
        bombs_events = {"planting": [], "planted": [], "exploded": []}
        agents_dead = {"Terrorist": [], "Police": []}

        self._game_status.update(current_cycle)
        self._update_fow()

        for event in gui_events:
            if event.type == GuiEventType.MovePolice:
                moving_polices.append(event.payload)

            if event.type == GuiEventType.MoveTerrorist:
                moving_terrorists.append(event.payload)

            if event.type == GuiEventType.DefusingBomb:
                bombs_defusing.append(event.payload)

            if event.type == GuiEventType.PlantingBomb:
                bombs_events['planting'].append(event.payload)

            if event.type == GuiEventType.DefusedBomb:
                bombs_defused.append(event.payload)
                self._game_status.increase_defused_number()

            if event.type == GuiEventType.PlantedBomb:
                bombs_events['planted'].append(event.payload)
                self._game_status.increase_planted_number()

            if event.type == GuiEventType.ExplodeBomb:
                bombs_events['exploded'].append(event.payload)
                self._game_status.increase_exploded_number()

            if event.type in [GuiEventType.CancelPlant, GuiEventType.CancelDefuse]:
                bombs_op_canceled.append(event.payload)

            if event.type == GuiEventType.TerroristDeath:
                agents_dead["Terrorist"].append(event.payload)

            if event.type == GuiEventType.PoliceDeath:
                agents_dead["Police"].append(event.payload)

        # Updates
        if (len(moving_terrorists) != 0) or (len(moving_polices) != 0):
            for side in self._sides:
                moves = moving_polices if side == 'Police' else moving_terrorists
                for move in moves:
                    pos = self._get_scene_position(move['agent_position'])
                    reference = self._agents_ref[side][move['agent_id']]

                    self._scene.add_action(scene_actions.ChangeTransform(
                        ref = reference,
                        duration_cycles = 1,
                        position = scene_actions.Vector3(x=pos['x'], z=pos['z']),
                        rotation = scene_actions.Vector3(y=self.DIR_TO_ANGLE[move['direction'].name])
                    ))

        # if len(bombs_events['planting']) != 0:
        #     bomb.update_board_on_planting(self, bombs_events['planting'])

        # if len(bombs_events['planted']) != 0:
        #     bomb.update_board_on_planted(self, bombs_events['planted'])

        # if len(bombs_events['exploded']) != 0:
        #     bomb.update_board_on_explode(self, bombs_events['exploded'])

        # if len(bombs_defusing) != 0:
        #     bomb.update_board_on_defusing(self, bombs_defusing)

        # if len(bombs_defused) != 0:
        #     bomb.update_board_on_defuse(self, bombs_defused)

        # if len(bombs_op_canceled) != 0:
        #     bomb.update_board_on_bomb_cancel(self, bombs_op_canceled)

        # if len(agents_dead["Terrorist"]) != 0:
        #     death.update_on_death_terrorist(self, agents_dead)

        # if len(agents_dead["Police"]) != 0:
        #     death.update_on_death_police(self, agents_dead)

        self._scene.add_action(scene_actions.EndCycle())


    def _get_scene_position(self, position):
        addition = self.CELL_SIZE / 2
        return {
            'x': position.x * self.CELL_SIZE + addition + self.X_OFFSET,
            'z': -(position.y * self.CELL_SIZE + addition + self.Z_OFFSET)
        }

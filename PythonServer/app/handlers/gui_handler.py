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
        self.FOW_Y = 10

        self.DIR_TO_ANGLE = {
            ECommandDirection.Up.name:    0,
            ECommandDirection.Right.name: 90,
            ECommandDirection.Down.name:  180,
            ECommandDirection.Left.name:  -90
        }

        self.TURN_CYCLES = 0.3
        self.MOVE_CYCLES = 0.5
        self.STOP_CYCLES = 0.2
        self.BEFORE_FIRE_CYCLES = 0.5
        self.BEFORE_DEATH_CYCLES = 1
        self.AFTER_DEATH_CYCLES = 5
        self.DEEP_DOWN_Y = -5
        self.DEEP_DOWN_CYCLES = 5
        self.EXPLOSION_CYCLES = 4

        self.RIFLE_TRANSFORM = {
            'Police': {
                'default': {
                    'position': {'x': 11.8, 'y': 5.6, 'z': -0.5},
                    'rotation': {'x': -21.869, 'y': 97.065, 'z': 263.517}
                },
                'fire': {
                    'position': {'x': 9.8, 'y': 7.1, 'z': -2.2},
                    'rotation': {'x': 10.032, 'y': 80.775, 'z': 260.71}
                }
            },
            'Terrorist': {
                'default': {
                    'position': {'x': 10.5, 'y': 5.4, 'z': -2.6},
                    'rotation': {'x': -17.88, 'y': 93.76501, 'z': 266.088}
                },
                'fire': {
                    'position': {'x': 10.3, 'y': 5.4, 'z': -1.6},
                    'rotation': {'x': 9.580001, 'y': 83.952, 'z': 272.559}
                }
            }
        }

        self.WATER_Y = -2
        self.BEACH_SCALE_FACTOR = 0.1

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
        self._agents_direction = {side: {} for side in self._sides}
        self._fows_ref = {}
        self._hidden_fows_pos = [] # fog of wars that are hidden because of the visions
        self._bombsites_ref = {} # key: (x, y)
        self._plantings_ref = {} # key: bombsite_ref, value: agent
        self._active_bombsites_ref = {} # key: bombsite_ref, value: bomb


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
            max_position = scene_actions.Vector3(x=-(self.X_OFFSET + extra_camera_boundry), y=20, z=-(self.Z_OFFSET + extra_camera_boundry)),
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
        ground_ref = self._rm.new()
        self._scene.add_action(scene_actions.InstantiateBundleAsset(
            ref = ground_ref,
            asset = scene_actions.Asset(bundle_name='main', asset_name='Ground')
        ))
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = ground_ref, child_ref = 'Beach',
            scale = scene_actions.Vector3(
                x = self._world.width * self.CELL_SIZE * self.BEACH_SCALE_FACTOR,
                z = self._world.height * self.CELL_SIZE * self.BEACH_SCALE_FACTOR
            )
        ))

        water_ref = self._rm.new()
        self._scene.add_action(scene_actions.InstantiateBundleAsset(
            ref = water_ref,
            asset = scene_actions.Asset(bundle_name='main', asset_name='Water')
        ))
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = water_ref,
            position = scene_actions.Vector3(y=self.WATER_Y)
        ))

        # Draw non-player cells
        for y in range(self._world.height):
            for x in range(self._world.width):
                cell = self._world.board[y][x]

                if cell == ECell.Empty:
                    continue

                reference = self._rm.new()

                if cell == ECell.Wall:
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Barrier')
                    ))

                elif cell in [ECell.SmallBombSite, ECell.MediumBombSite, ECell.LargeBombSite, ECell.VastBombSite]:
                    self._bombsites_ref[(x, y)] = reference
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name=cell.name)
                    ))

                # Set Position
                pos = self._get_scene_position(Position(x=x, y=y))
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

                self._scene.add_action(scene_actions.ChangeIsActive(
                    ref = reference,
                    child_ref = 'Root/Hips/Spine_01/Spine_02/Spine_03/Clavicle_R/Shoulder_R/Elbow_R/Hand_R/{0}'.format(side + 'Rifle'),
                    is_active = True
                ))

                # set position
                self._agents_direction[side][agent.id] = agent.init_direction
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = reference,
                    position = scene_actions.Vector3(x=pos['x'], z=pos['z']),
                    rotation = scene_actions.Vector3(y=self.DIR_TO_ANGLE[agent.init_direction.name])
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
        moving_terrorists, moving_polices = [], []
        bombs_defusing, bombs_defused, cancel_defusing = [], [], []
        bombs_planting, bombs_planted, bombs_exploded, cancel_planting = [], [], [], []
        polices_dead, terrorists_dead = [], []

        self._game_status.update(current_cycle)
        self._update_fow()

        for event in gui_events:
            if event.type == GuiEventType.MovePolice:
                moving_polices.append(event.payload)

            if event.type == GuiEventType.MoveTerrorist:
                moving_terrorists.append(event.payload)

            if event.type == GuiEventType.PlantingBomb:
                bombs_planting.append(event.payload)

            if event.type == GuiEventType.CancelPlant:
                cancel_planting.append(event.payload)

            if event.type == GuiEventType.PlantedBomb:
                bombs_planted.append(event.payload)

            if event.type == GuiEventType.DefusingBomb:
                bombs_defusing.append(event.payload)

            if event.type == GuiEventType.CancelDefuse:
                cancel_defusing.append(event.payload)

            if event.type == GuiEventType.DefusedBomb:
                bombs_defused.append(event.payload)
                self._game_status.increase_defused_number()

            if event.type == GuiEventType.ExplodeBomb:
                bombs_exploded.append(event.payload)

            if event.type == GuiEventType.TerroristDeath:
                terrorists_dead.append(event.payload)

            if event.type == GuiEventType.PoliceDeath:
                polices_dead.append(event.payload)

        # Updates
        # Moves
        if len(moving_terrorists) != 0 or len(moving_polices) != 0:
            for side in self._sides:
                moves = moving_polices if side == 'Police' else moving_terrorists

                for move in moves:
                    agent = self._world.polices[move['agent_id']] if side == 'Police' else self._world.terrorists[move['agent_id']]
                    curr_direction = self._agents_direction[side][move['agent_id']]
                    pos = self._get_scene_position(move['agent_position'])
                    reference = self._agents_ref[side][move['agent_id']]

                    # Animations
                    # Turn
                    turn_animation, need_to_turn = self._get_turn_animation(curr_direction, move['direction'])
                    self._change_animator_state(reference, 0, turn_animation)
                    if need_to_turn:
                        self._scene.add_action(scene_actions.ChangeTransform(
                            ref = reference,
                            cycle = self.TURN_CYCLES,
                            rotation = scene_actions.Vector3(y=self.DIR_TO_ANGLE[move['direction'].name])
                        ))
                    # Move
                    self._scene.add_action(scene_actions.ChangeTransform(
                        ref = reference,
                        duration_cycles = 1,
                        position = scene_actions.Vector3(x=pos['x'], z=pos['z'])
                    ))
                    self._change_animator_state(reference, self.TURN_CYCLES, 'Move')
                    # Stop
                    self._change_animator_state(reference, self.TURN_CYCLES + self.MOVE_CYCLES, 'MoveToIdle')
                    self._change_animator_state(reference, 1, 'Idle')

                    # Store new direction
                    self._agents_direction[side][move['agent_id']] = move['direction']

        # Planting Bomb
        if len(bombs_planting) != 0:
            for plant in bombs_planting:
                bomb = plant['bomb']
                bombsite_ref = self._bombsites_ref[(bomb.position.x, bomb.position.y)]
                planter = self._world.terrorists[plant['agent_id']]
                # update status dictionaries
                self._plantings_ref[bombsite_ref] = planter
                # Update bombsite
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Planting', 0, True)
                # update agent
                self._change_animator_state(self._agents_ref['Terrorist'][planter.id], 0, 'BombAction')
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = self._agents_ref['Terrorist'][planter.id],
                    rotation = scene_actions.Vector3(y=self.DIR_TO_ANGLE[plant['direction'].name])
                ))

        # Cancel Planting
        if len(cancel_planting) != 0:
            for canceled in cancel_planting:
                bomb = canceled['bomb']
                bombsite_ref = self._bombsites_ref[(bomb.position.x, bomb.position.y)]
                planter = self._plantings_ref[bombsite_ref]
                # update status dictionaries
                del self._plantings_ref[bombsite_ref]
                # Update bombsite
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Planting', 0, False)
                # update agent
                self._change_animator_state(self._agents_ref['Terrorist'][planter.id], 0, 'Idle')
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = self._agents_ref['Terrorist'][planter.id],
                    rotation = scene_actions.Vector3(y=self.DIR_TO_ANGLE[self._agents_direction['Terrorist'][planter.id].name])
                ))

        # Bombs Planted
        if len(bombs_planted) != 0:
            for planted in bombs_planted:
                bomb = planted['bomb']
                bombsite_ref = self._bombsites_ref[(bomb.position.x, bomb.position.y)]
                planter = self._plantings_ref[bombsite_ref]
                # increase counter
                self._game_status.increase_planted_number()
                # update status dictionaries
                self._active_bombsites_ref[bombsite_ref] = bomb
                del self._plantings_ref[bombsite_ref]
                # Update bombsite
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Planting', 0, False)
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Timer', 0, True)
                # update agent
                self._change_animator_state(self._agents_ref['Terrorist'][planter.id], 0, 'Idle')

        # Bombs Exploded
        if len(bombs_exploded) != 0:
            for exploded in bombs_exploded:
                bomb = exploded['bomb']
                bombsite_ref = self._bombsites_ref[(bomb.position.x, bomb.position.y)]
                # increase counter
                self._game_status.increase_exploded_number()
                # update status dictionaries
                del self._active_bombsites_ref[bombsite_ref]
                # Update bombsite
                self._change_is_active(bombsite_ref, 'Canvas', 0, False)
                self._change_animator_state(bombsite_ref, 0, 'Explosion')
                self._deep_down(bombsite_ref, self.EXPLOSION_CYCLES)

        # Update bombsites canvas
        self._update_planting_bombsites()
        self._update_bombsites_timer()

        # Add EndCycle
        self._scene.add_action(scene_actions.EndCycle())


    def _change_animator_state(self, reference, cycle, state_name):
        self._scene.add_action(scene_actions.ChangeAnimatorState(
            ref = reference,
            cycle = cycle,
            state_name = state_name
        ))


    def _get_turn_animation(self, curr_direction, new_direction):
        diff = new_direction.value - curr_direction.value

        # return (animation, need to turn)
        if diff == 0:
            return 'IdleToMove', False
        if abs(diff) == 2:
            return 'TurnBack', True
        if diff == 1 or diff == -3:
            return 'TurnRight', True
        if diff == -1 or diff == 3:
            return 'TurnLeft', True


    def _change_is_active(self, reference, child_ref, cycle, is_active):
        self._scene.add_action(scene_actions.ChangeIsActive(
            ref = reference, child_ref = child_ref,
            cycle = cycle,
            is_active = is_active
        ))


    def _change_text(self, reference, child_ref, cycle, text):
        self._scene.add_action(scene_actions.ChangeText(
            ref = reference, child_ref = child_ref,
            cycle = cycle,
            text = text
        ))


    def _update_planting_bombsites(self):
        for bombsite_ref in self._plantings_ref:
            agent = self._plantings_ref[bombsite_ref]
            self._change_text(bombsite_ref, 'Canvas/Panel/Planting/Text', None, str(agent.planting_remaining_time))


    def _update_bombsites_timer(self):
        for bombsite_ref in self._active_bombsites_ref:
            bomb = self._active_bombsites_ref[bombsite_ref]
            self._change_text(bombsite_ref, 'Canvas/Panel/Timer/Text', None, str(bomb.explosion_remaining_time))


    def _deep_down(self, reference, cycle):
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = reference,
            cycle = cycle,
            duration_cycles = self.DEEP_DOWN_CYCLES,
            position = scene_actions.Vector3(y=self.DEEP_DOWN_Y)
        ))


    def _get_scene_position(self, position):
        addition = self.CELL_SIZE / 2
        return {
            'x': position.x * self.CELL_SIZE + addition + self.X_OFFSET,
            'z': -(position.y * self.CELL_SIZE + addition + self.Z_OFFSET)
        }

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
        self._init_render_settings()
        self._init_light()
        self._init_camera()
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

        self.ANGLE_BETWEEN_OFFSET = -90

        self.BOMB_OPERATIONS_COMPLETED_SOUND_CYCLES = 1.5

        self.TURN_CYCLES = 0.3
        self.MOVE_CYCLES = 0.4
        self.STOP_CYCLES = 0.3

        self.EXPLOSION_CYCLES = 3
        self.EXPLOSION_SOUND_CYCLES = 2
        self.EXPLOSION_THROWBACK = 5
        self.EXPLOSION_THROWBACK_CYCLES = 2
        self.EXPLOSION_THROWBACK = 5

        self.SHOOT_OFFSET_CYCLES = 1
        self.BEFORE_SHOOT_CYCLES = 1
        self.SHOOT_CYCLES = 1
        self.SHOOT_THROWBACK_CYCLES = 2
        self.SHOOT_THROWBACK = 1
        self.SHOOT_ANGLE_BETWEEN_OFFSET = self.ANGLE_BETWEEN_OFFSET - 6

        self.DEEP_DOWN_Y = -5
        self.DEEP_DOWN_CYCLES = 3

        self.RIFLE_TRANSFORM = {
            'Police': {
                'Default': {
                    'position': scene_actions.Vector3(x=11.8, y=5.6, z=-0.5),
                    'rotation': scene_actions.Vector3(x=-21.869, y=97.065, z=263.517),
                },
                'Fire': {
                    'position': scene_actions.Vector3(x=9.8, y=7.1, z=-2.2),
                    'rotation': scene_actions.Vector3(x=10.032, y=80.775, z=260.71),
                }
            },
            'Terrorist': {
                'Default': {
                    'position': scene_actions.Vector3(x=10.5, y=5.4, z=-2.6),
                    'rotation': scene_actions.Vector3(x=-17.88, y=93.76501, z=266.088),
                },
                'Fire': {
                    'position': scene_actions.Vector3(x=10.3, y=5.4, z=-1.6),
                    'rotation': scene_actions.Vector3(x=9.580001, y=83.952, z=272.559),
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
        self._bombsites_ref = {} # key: (x, y), value: reference
        self._plantings_ref = {} # key: bombsite_ref, value: terrorist
        self._active_bombsites_ref = {} # key: bombsite_ref, value: bomb
        self._defusings_ref = {} # key: bombsite_ref, value: police


    def _init_render_settings(self):
        self._scene.add_action(scene_actions.ChangeRenderSettings(
            skybox_asset = scene_actions.Asset(bundle_name='main', asset_name='Skybox'),
            ambient_intensity=1.5
        ))


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
            shadow_strength = 0.4
        ))


    def _init_camera(self):
        fov = 60 # TODO: calculate
        extra_camera_boundry = -10

        self._scene.add_action(scene_actions.ChangeCamera(
            ref = self._rm.get('MainCamera'),
            is_orthographic = False,
            field_of_view = fov,
            min_position = scene_actions.Vector3(x=(self.X_OFFSET + extra_camera_boundry), y=2, z=(self.Z_OFFSET + extra_camera_boundry)),
            max_position = scene_actions.Vector3(x=-(self.X_OFFSET + extra_camera_boundry), y=100, z=-(self.Z_OFFSET + extra_camera_boundry)),
            min_zoom = fov - 20,
            max_zoom = fov + 40,
            post_process_profile_asset = scene_actions.Asset(bundle_name='main', asset_name='PostProcess'),
        ))
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = self._rm.get('MainCamera'),
            position = scene_actions.Vector3(x=0, y=10, z=(self.Z_OFFSET + extra_camera_boundry)),
            rotation = scene_actions.Vector3(x=30, y=0, z=0)
        ))


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

                    # Add floor
                    floor_ref = self._rm.new()
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = floor_ref,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='BombFloor')
                    ))
                    self._move_xz(floor_ref, None, None, Position(x=x, y=y))

                # Set Position
                self._move_xz(reference, None, None, Position(x=x, y=y))


    def _draw_agents(self):
        for side in self._sides:
            agents = self._world.polices if side == 'Police' else self._world.terrorists
            skins = self.POLICE_SKINS if side == 'Police' else self.TERRORIST_SKINS
            material_offsets = self.POLICE_MATERIAL_OFFSETS if side == 'Police' else self.TERRORIST_MATERIAL_OFFSETS
            heads = self.POLICE_HEADS if side == 'Police' else self.TERRORIST_HEADS
            items = self.POLICE_ITEMS if side == 'Police' else self.TERRORIST_ITEMS

            for agent in agents:
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
                self._move_xz(reference, None, None, agent.position)
                self._turn_y(reference, None, None, self.DIR_TO_ANGLE[agent.init_direction.name])


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
        self._game_status.update(current_cycle)
        self._update_fow()

        # Store events
        moving_terrorists, moving_polices = [], []
        bombs_defusing, bombs_defused, cancel_defusing = [], [], []
        bombs_planting, bombs_planted, bombs_exploded, cancel_planting = [], [], [], []
        bombs_death, terrorists_shooted, shoot_terrorists = [], [], []

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

            if event.type == GuiEventType.ExplodeBomb:
                bombs_exploded.append(event.payload)

            if event.type == GuiEventType.BombDeath:
                bombs_death.append(event.payload)

            if event.type == GuiEventType.TerroristShooted:
                terrorists_shooted.append(event.payload)

            if event.type == GuiEventType.ShootTerrorist:
                shoot_terrorists.append(event.payload)

        # Process events
        # Moves
        if len(moving_terrorists) != 0 or len(moving_polices) != 0:
            for side in self._sides:
                moves = moving_polices if side == 'Police' else moving_terrorists

                for move in moves:
                    agent = self._world.polices[move['agent_id']] if side == 'Police' else self._world.terrorists[move['agent_id']]
                    curr_direction = self._agents_direction[side][move['agent_id']]
                    reference = self._agents_ref[side][move['agent_id']]

                    # Animations
                    # Turn
                    turn_animation, need_to_turn = self._get_turn_animation(curr_direction, move['direction'])
                    self._change_animator_state(reference, 0, turn_animation)
                    if need_to_turn:
                        self._turn_y(reference, self.TURN_CYCLES, None, self.DIR_TO_ANGLE[move['direction'].name])
                    # Move
                    self._move_xz(reference, None, 1, move['agent_position'])
                    self._change_animator_state(reference, self.TURN_CYCLES, 'Move')
                    # Stop
                    self._change_animator_state(reference, self.TURN_CYCLES + self.MOVE_CYCLES, 'MoveToIdle')
                    self._change_animator_state(reference, 1, 'Idle')

                    # Store new direction
                    self._agents_direction[side][move['agent_id']] = move['direction']

        # Planting Bomb
        if len(bombs_planting) != 0:
            for planting in bombs_planting:
                bomb = planting['bomb']
                bombsite_ref = self._bombsites_ref[(bomb.position.x, bomb.position.y)]
                planter = self._world.terrorists[planting['agent_id']]
                # update status dictionaries
                self._plantings_ref[bombsite_ref] = planter
                # Update bombsite
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Planting', 0, True)
                # update agent
                self._change_animator_state(self._agents_ref['Terrorist'][planter.id], 0, 'BombAction')
                self._turn_y(self._agents_ref['Terrorist'][planter.id], None, None, self.DIR_TO_ANGLE[planting['direction'].name])
                # Update gun position
                self._change_rifle_transform(self._agents_ref['Terrorist'][planter.id], None, 'Terrorist', 'Fire')
                # Store new direction
                self._agents_direction['Terrorist'][planter.id] = planting['direction']

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
                # Update gun position
                self._change_rifle_transform(self._agents_ref['Terrorist'][planter.id], None, 'Terrorist', 'Default')

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
                self._add_bomb(bombsite_ref)
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Planting', 0, False)
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Timer', 0, True)
                # update agent
                self._change_animator_state(self._agents_ref['Terrorist'][planter.id], 0, 'Idle')
                # Update sounds
                self._play_sound(bombsite_ref, 'AudioSource', None, 'bomb_planted_sfx')
                self._pause_sound(bombsite_ref, 'AudioSource', self.BOMB_OPERATIONS_COMPLETED_SOUND_CYCLES)
                # Update gun position
                self._change_rifle_transform(self._agents_ref['Terrorist'][planter.id], None, 'Terrorist', 'Default')

        # Defusing Bomb
        if len(bombs_defusing) != 0:
            for defusing in bombs_defusing:
                bomb = defusing['bomb']
                bombsite_ref = self._bombsites_ref[(bomb.position.x, bomb.position.y)]
                defuser = self._world.polices[defusing['agent_id']]
                # update status dictionaries
                self._defusings_ref[bombsite_ref] = defuser
                # Update bombsite
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Defusing', 0, True)
                # update agent
                self._change_animator_state(self._agents_ref['Police'][defuser.id], 0, 'BombAction')
                self._turn_y(self._agents_ref['Police'][defuser.id], None, None, self.DIR_TO_ANGLE[defusing['direction'].name])
                # Update gun position
                self._change_rifle_transform(self._agents_ref['Police'][defuser.id], None, 'Police', 'Fire')
                # Store new direction
                self._agents_direction['Police'][defuser.id] = defusing['direction']

        # Cancel Defusing
        if len(cancel_defusing) != 0:
            for canceled in cancel_defusing:
                bomb = canceled['bomb']
                bombsite_ref = self._bombsites_ref[(bomb.position.x, bomb.position.y)]
                defuser = self._defusings_ref[bombsite_ref]
                # update status dictionaries
                del self._defusings_ref[bombsite_ref]
                # Update bombsite
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Defusing', 0, False)
                # update agent
                self._change_animator_state(self._agents_ref['Police'][defuser.id], 0, 'Idle')
                # Update gun position
                self._change_rifle_transform(self._agents_ref['Police'][defuser.id], None, 'Police', 'Default')

        # Bombs Defused
        if len(bombs_defused) != 0:
            for defused in bombs_defused:
                bomb = defused['bomb']
                bombsite_ref = self._bombsites_ref[(bomb.position.x, bomb.position.y)]
                defuser = self._defusings_ref[bombsite_ref]
                # increase counter
                self._game_status.increase_defused_number()
                # update status dictionaries
                del self._defusings_ref[bombsite_ref]
                # Update bombsite
                self._remove_bomb(bombsite_ref)
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Defusing', 0, False)
                self._change_is_active(bombsite_ref, 'Canvas/Panel/Timer', 0, False)
                # update agent
                self._change_animator_state(self._agents_ref['Police'][defuser.id], 0, 'Idle')
                # Update sounds
                self._play_sound(bombsite_ref, 'AudioSource', None, 'bomb_defused_sfx')
                self._pause_sound(bombsite_ref, 'AudioSource', self.BOMB_OPERATIONS_COMPLETED_SOUND_CYCLES)
                # Update gun position
                self._change_rifle_transform(self._agents_ref['Police'][defuser.id], None, 'Police', 'Default')

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
                self._remove_bomb(bombsite_ref)
                self._add_explosion(bombsite_ref)
                self._play_sound(bombsite_ref, 'AudioSource', None, 'bomb_explosion_sfx')
                self._pause_sound(bombsite_ref, 'AudioSource', self.EXPLOSION_SOUND_CYCLES)
                self._change_is_active(bombsite_ref, 'Canvas', 0, False)
                self._change_animator_state(bombsite_ref, 0, 'Explosion')
                self._deep_down(bombsite_ref, self.EXPLOSION_CYCLES)

        # Bombs Death
        if len(bombs_death) != 0:
            for bomb_death in bombs_death:
                side = bomb_death['side']
                agent = bomb_death['agent']
                reference = self._agents_ref[side][agent.id]
                bomb = bomb_death['bomb']
                # turn toward bomb
                turn_angle = agent.position.angle_between(bomb.position)
                self._turn_y(reference, None, None, turn_angle + self.ANGLE_BETWEEN_OFFSET)
                # throwback and deep down
                end_position = agent.position.add_vector(turn_angle, self.EXPLOSION_THROWBACK)
                self._move_xz(reference, None, self.EXPLOSION_THROWBACK_CYCLES / 2, end_position)
                self._deep_down(reference, self.EXPLOSION_THROWBACK_CYCLES)
                # update animation
                self._change_animator_state(reference, 0, 'Death')

        # Terrorists Shooted
        if len(terrorists_shooted) != 0:
            for shooted in terrorists_shooted:
                agent = shooted['agent']
                reference = self._agents_ref['Terrorist'][agent.id]
                killer = shooted['killer']
                # increase counter
                self._game_status.increase_terrorists_killed()
                # turn toward killer
                turn_angle = agent.position.angle_between(killer.position)
                self._turn_y(reference, self.SHOOT_OFFSET_CYCLES, self.BEFORE_SHOOT_CYCLES, turn_angle + self.SHOOT_ANGLE_BETWEEN_OFFSET)
                # throwback and deep down
                end_position = agent.position.add_vector(turn_angle, self.SHOOT_THROWBACK)
                self._move_xz(reference, self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES, self.SHOOT_THROWBACK_CYCLES / 2, end_position)
                self._deep_down(reference, self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES + self.SHOOT_THROWBACK_CYCLES)
                # update animation
                self._change_animator_state(reference, self.SHOOT_OFFSET_CYCLES, 'BeforeDeath')
                self._change_animator_state(reference, self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES, 'Death')
                # Update gun position
                self._change_rifle_transform(reference, self.SHOOT_OFFSET_CYCLES, 'Terrorist', 'Fire')

        # Shoot Terrorists
        if len(shoot_terrorists) != 0:
            for shoot in shoot_terrorists:
                police = shoot['police']
                reference = self._agents_ref['Police'][police.id]
                terrorist = shoot['terrorist']
                # turn toward terrorist
                turn_angle = police.position.angle_between(terrorist.position)
                self._turn_y(reference, self.SHOOT_OFFSET_CYCLES, self.BEFORE_SHOOT_CYCLES, turn_angle + self.SHOOT_ANGLE_BETWEEN_OFFSET) # turn toward terrorist
                self._turn_y(reference, self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES + self.SHOOT_CYCLES, None, self.DIR_TO_ANGLE[self._agents_direction['Police'][police.id].name]) # back start rotation
                # update animation
                self._change_animator_state(reference, self.SHOOT_OFFSET_CYCLES, 'BeforeFire')
                self._change_animator_state(reference, self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES, 'Fire')
                self._change_animator_state(reference, self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES + self.SHOOT_CYCLES, 'Idle')
                # Update gun position
                self._change_rifle_transform(reference, self.SHOOT_OFFSET_CYCLES, 'Police', 'Fire')
                self._change_rifle_transform(reference, self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES + self.SHOOT_CYCLES, 'Police', 'Default')
                # Update sounds
                self._play_sound(reference, 'AudioSource', self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES)
                self._pause_sound(reference, 'AudioSource', self.SHOOT_OFFSET_CYCLES + self.BEFORE_SHOOT_CYCLES + self.SHOOT_CYCLES)

        # Update bombsites canvas
        self._update_planting_bombsites()
        self._update_defusing_bombsites()
        self._update_bombsites_timer()

        # Add EndCycle
        self._scene.add_action(scene_actions.EndCycle())
        if len(shoot_terrorists) != 0:
            for _ in range(self.BEFORE_SHOOT_CYCLES + self.SHOOT_CYCLES):
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


    def _turn_y(self, reference, cycle, duration_cycles, angle):
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = reference,
            cycle = cycle,
            duration_cycles = duration_cycles,
            rotation = scene_actions.Vector3(y=angle)
        ))


    def _move_xz(self, reference, cycle, duration_cycles, position):
        scene_position = self._get_scene_position(position)
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = reference,
            cycle = cycle,
            duration_cycles = duration_cycles,
            position = scene_actions.Vector3(x=scene_position['x'], z=scene_position['z'])
        ))


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


    def _update_defusing_bombsites(self):
        for bombsite_ref in self._defusings_ref:
            agent = self._defusings_ref[bombsite_ref]
            self._change_text(bombsite_ref, 'Canvas/Panel/Defusing/Text', None, str(agent.defusion_remaining_time))


    def _update_bombsites_timer(self):
        for bombsite_ref in self._active_bombsites_ref:
            bomb = self._active_bombsites_ref[bombsite_ref]
            self._change_text(bombsite_ref, 'Canvas/Panel/Timer/Text', None, str(bomb.explosion_remaining_time))


    def _add_bomb(self, bombsite_ref):
        self._scene.add_action(scene_actions.ChangeIsActive(
            ref = bombsite_ref, child_ref = 'BombPosition',
            is_active = True
        ))
        self._scene.add_action(scene_actions.ChangeAnimatorState(
            ref = bombsite_ref, child_ref = 'BombPosition/Bomb',
            state_name = 'BombBeep',
            normalized_time = 0
        ))


    def _remove_bomb(self, bombsite_ref):
        self._pause_sound(bombsite_ref, 'AudioSource', None)
        self._scene.add_action(scene_actions.ChangeIsActive(
            ref = bombsite_ref, child_ref = 'BombPosition',
            is_active = False
        ))


    def _add_explosion(self, bombsite_ref):
        self._scene.add_action(scene_actions.ChangeIsActive(
            ref = bombsite_ref, child_ref = 'Explosion',
            is_active = True
        ))


    def _deep_down(self, reference, cycle):
        cycle = cycle if cycle != None else 0

        self._scene.add_action(scene_actions.ChangeTransform(
            ref = reference,
            cycle = cycle,
            duration_cycles = self.DEEP_DOWN_CYCLES,
            position = scene_actions.Vector3(y=self.DEEP_DOWN_Y)
        ))


    def _change_rifle_transform(self, reference, cycle, side, state):
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = reference,
            child_ref = 'Root/Hips/Spine_01/Spine_02/Spine_03/Clavicle_R/Shoulder_R/Elbow_R/Hand_R/{}Rifle'.format(side),
            cycle = cycle,
            position = self.RIFLE_TRANSFORM[side][state]['position'],
            rotation = self.RIFLE_TRANSFORM[side][state]['rotation']
        ))


    def _play_sound(self, reference, child_ref, cycle, sound_name=None):
        clip_asset = None
        if sound_name != None:
            clip_asset = scene_actions.Asset(bundle_name='main', asset_name=sound_name)

        self._scene.add_action(scene_actions.ChangeAudioSource(
            ref = reference, child_ref = child_ref,
            cycle = cycle,
            play = True,
            time = 0,
            audio_clip_asset = clip_asset
        ))


    def _pause_sound(self, reference, child_ref, cycle):
        self._scene.add_action(scene_actions.ChangeAudioSource(
            ref = reference, child_ref = child_ref,
            cycle = cycle,
            play = False
        ))


    def _get_scene_position(self, position):
        addition = self.CELL_SIZE / 2
        return {
            'x': position.x * self.CELL_SIZE + addition + self.X_OFFSET,
            'z': -(position.y * self.CELL_SIZE + addition + self.Z_OFFSET)
        }

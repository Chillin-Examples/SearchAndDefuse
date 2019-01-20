# -*- coding: utf-8 -*-

# chillin imports
from chillin_server.gui import scene_actions

# project imports
from ..ks.models import AgentStatus, ESoundIntensity


class GameStatus:

    def __init__(self, world, sides, scene):
        self._world = world
        self._sides = sides
        self._scene = scene
        self._rm = scene.rm


    def initialize(self):
        self._num_bombs_exploded = 0
        self._num_bombs_defused = 0
        self._num_bombs_planted = 0

        self._top_panel_ref = self._rm.new()
        self._cycle_text_ref = 'Statuses/CycleText'
        self._police_score_ref = 'Statuses/Scores/PoliceScore'
        self._terrorist_score_ref = 'Statuses/Scores/TerroristScore'
        self._planted_bombs_ref = 'Statuses/Stats/PlantedBombs/Text'
        self._exploded_bombs_ref = 'Statuses/Stats/ExplodedBombs/Text'
        self._defused_bombs_ref = 'Statuses/Stats/DefusedBombs/Text'
        self._polices_table_ref = 'Polices'
        self._terrorists_table_ref = 'Terrorists'
        self._polices_ref = {}
        self._terrorists_ref = {}


    def draw(self):
        self._scene.add_action(scene_actions.InstantiateBundleAsset(
            ref = self._top_panel_ref,
            asset = scene_actions.Asset(bundle_name='main', asset_name='TopPanel'),
            default_parent = scene_actions.EDefaultParent.RootCanvas
        ))

        # Cycle
        self._set_cycle_text(0)

        # Agents
        for side in self._sides:
            agents = self._world.polices if side == 'Police' else self._world.terrorists
            table_ref = self._polices_table_ref if side == 'Police' else self._terrorists_table_ref
            agents_ref = self._polices_ref if side == 'Police' else self._terrorists_ref
            asset_name = 'PoliceStatus' if side == 'Police' else 'TerroristStatus'

            for agent in agents:
                reference = self._rm.new()
                agents_ref[agent.id] = reference

                self._scene.add_action(scene_actions.InstantiateBundleAsset(
                    ref = reference,
                    parent_ref = self._top_panel_ref,
                    parent_child_ref = table_ref,
                    asset = scene_actions.Asset(bundle_name='main', asset_name=asset_name),
                ))
                self._set_text('Stats/ID', str(agent.id), reference)
                self._update_agent(reference, agent, side)


    def update(self, current_cycle):
        # Cycle
        self._set_cycle_text(current_cycle)

        # Scores
        for side in self._sides:
            score = self._world.scores['Police'] if side == 'Police' else self._world.scores['Terrorist']
            ref = self._police_score_ref if side == 'Police' else self._terrorist_score_ref
            self._set_text(ref, str(score))

        # Agents
        for side in self._sides:
            agents = self._world.polices if side == 'Police' else self._world.terrorists
            agents_ref = self._polices_ref if side == 'Police' else self._terrorists_ref

            for agent in agents:
                self._update_agent(agents_ref[agent.id], agent, side)


    def _set_text(self, child_ref, text, reference=None, cycle=None):
        reference = reference if reference != None else self._top_panel_ref
        self._scene.add_action(scene_actions.ChangeText(
            ref = reference,
            cycle = cycle,
            child_ref = child_ref,
            text = text
        ))


    def _set_cycle_text(self, cycle):
        self._set_text(self._cycle_text_ref, 'Cycle: {:d}/{:d}'.format(cycle, self._world.constants.max_cycles))


    def _update_agent(self, agent_ref, agent, side):
        self._set_position_text(agent_ref, agent)
        self._set_bomb_text(agent_ref, agent, side)
        self._set_footstep_sounds(agent_ref, agent)
        if side == 'Police':
            self._set_bomb_sounds(agent_ref, agent)


    def _set_position_text(self, agent_ref, agent):
        text = '{:d}, {:d}'.format(agent.position.x, agent.position.y) if agent.status == AgentStatus.Alive else '<color=red>Dead</color>'
        self._set_text('Stats/Position', text, agent_ref, 1)


    def _set_bomb_text(self, agent_ref, agent, side):
        value = agent.defusion_remaining_time if side == 'Police' else agent.planting_remaining_time
        text = '<color=red>{:d}</color>'.format(value) if value >= 0 else '-'
        self._set_text('Stats/BombText', text, agent_ref)


    def _set_footstep_sounds(self, agent_ref, agent):
        num_weaks, num_normals, num_strongs = self._calc_intensities(agent.footstep_sounds)
        self._set_text('Sounds/WeakFootstep/Panel/Text', str(num_weaks), agent_ref)
        self._set_text('Sounds/NormalFootstep/Panel/Text', str(num_normals), agent_ref)
        self._set_text('Sounds/StrongFootstep/Panel/Text', str(num_strongs), agent_ref)


    def _set_bomb_sounds(self, agent_ref, agent):
        num_weaks, num_normals, num_strongs = self._calc_intensities(agent.bomb_sounds)
        self._set_text('Sounds/WeakBomb/Panel/Text', str(num_weaks), agent_ref)
        self._set_text('Sounds/NormalBomb/Panel/Text', str(num_normals), agent_ref)
        self._set_text('Sounds/StrongBomb/Panel/Text', str(num_strongs), agent_ref)


    def _calc_intensities(self, sounds_intensity):
        num_weaks = 0
        num_normals = 0
        num_strongs = 0
        for intensity in sounds_intensity:
            if intensity == ESoundIntensity.Weak:
                num_weaks += 1
            elif intensity == ESoundIntensity.Normal:
                num_normals += 1
            elif intensity == ESoundIntensity.Strong:
                num_strongs += 1

        return num_weaks, num_normals, num_strongs


    def increase_exploded_number(self):
        self._num_bombs_exploded += 1
        self._set_text(self._exploded_bombs_ref, str(self._num_bombs_exploded))


    def increase_defused_number(self):
        self._num_bombs_defused += 1
        self._set_text(self._defused_bombs_ref, str(self._num_bombs_defused))


    def increase_planted_number(self):
        self._num_bombs_planted += 1
        self._set_text(self._planted_bombs_ref, str(self._num_bombs_planted))

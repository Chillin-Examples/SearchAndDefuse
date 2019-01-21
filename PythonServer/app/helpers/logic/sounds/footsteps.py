# -*- coding: utf-8 -*-

# project imports
from . import utils
from ....ks.models import EAgentStatus


def update_police_intensities(world):
    _update_agents_footsteps_intensity(world, 'Police')


def update_terrorist_intensities(world):
    _update_agents_footsteps_intensity(world, 'Terrorist')


def _update_agents_footsteps_intensity(world, side):
    agents = world.polices if side == 'Police' else world.terrorists
    opponent_agents = world.terrorists if side == 'Police' else world.polices

    for agent in agents:
        if agent.status == EAgentStatus.Alive:
            agent.footstep_sounds = _get_agent_footsteps_intensity(agent, opponent_agents, world.constants.sound_ranges)


def _get_agent_footsteps_intensity(agent, opponent_agents, max_intensities_dict):
    sounds = []
    for opponent_agent in opponent_agents:
        if opponent_agent.status == EAgentStatus.Alive and opponent_agent.is_moving:
            distance = utils.calculate_distance(agent.position, opponent_agent.position)
            intensity = utils.int_to_intensity(int(distance), max_intensities_dict)
            if intensity != None:
                sounds.append(intensity)

    return sounds

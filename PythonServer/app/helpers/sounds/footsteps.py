# -*- coding: utf-8 -*-

# project imports
from . import utils


def update_police_intensities(world):
    for police in world.polices:
        police.footstep_sounds = _update_agent_sound_intensity(police, world.terrorists, world.constants.sound_ranges)


def update_terrorist_intensities(world):
    for terrorist in world.terrorists:
        terrorist.footstep_sounds = _update_agent_sound_intensity(terrorist, world.polices, world.constants.sound_ranges)


def _update_agent_sound_intensity(agent, opponent_agents, max_intensities_dict):
    sounds = []
    for opponent_agent in opponent_agents:
        distance = utils.calculate_distance(agent.position, opponent_agent.position)
        intensity = utils.calculate_intensity(distance)
        sounds.append(utils.map_to_enum(intensity, max_intensities_dict))
    return sounds

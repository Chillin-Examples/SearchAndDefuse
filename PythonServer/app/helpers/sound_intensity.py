# -*- coding: utf-8 -*-

# python imports
import math

# project imports
from ..ks.models import *


def update_police_intensities(world):
    for police in world.polices:
        police.footstep_sounds = _update_agent_sound_intensity(police, world.terrorists, world.constants.sound_ranges)


def update_terrorist_intensities(world):
    for terrorist in world.terrorists:
        terrorist.footstep_sounds = _update_agent_sound_intensity(terrorist, world.polices, world.constants.sound_ranges)


def _update_agent_sound_intensity(agent, opponent_agents, max_intensities_dict):
    sounds = []
    for opponent_agent in opponent_agents:
        distance = _calculate_distance(agent.position, opponent_agent.position)
        intensity = _calculate_intensity(distance)
        sounds.append(_convert_to_enum(intensity, max_intensities_dict))
    return sounds


def _calculate_intensity(distance):
    return int(distance)


def _calculate_distance(point_a, point_b):
    return math.sqrt(math.pow(point_a.x - point_b.y, 2) + math.pow(point_a.y - point_b.y, 2))


def _convert_to_enum(intensity, max_intensities_dict):
    if max_intensities_dict['max_weak_sound_bomb'] > intensity:
        return ESoundIntensity.Weak
    elif max_intensities_dict['max_weak_sound_bomb'] <= intensity <= max_intensities_dict['max_normal_sound_bomb']:
        return ESoundIntensity.Normal
    elif max_intensities_dict['max_strong_sound_bomb'] < intensity:
        return ESoundIntensity.Strong

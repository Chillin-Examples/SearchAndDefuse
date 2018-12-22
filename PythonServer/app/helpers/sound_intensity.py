# -*- coding: utf-8 -*-

# python imports
import math

# project imports
from ..ks.models import *


def update_sound_intensities(world):
    for terrorist in world.terrorists:
        terrorist.footstep_sounds = _update_agent_sound_intensity(terrorist, world.polices)
    for police in world.polices:
        police.footstep_sounds = _update_agent_sound_intensity(police, world.terrorists)


def _update_agent_sound_intensity(agent, opponent_agents):
    sounds = []
    for opponent_agent in opponent_agents:
        distance = _calculate_distance(agent.position, opponent_agent.position)
        intensity = _calculate_intensity(distance)
        sounds.append(_convert_to_enum(intensity))
    return sounds


def _calculate_intensity(distance):
    return int(distance)


def _calculate_distance(point_a, point_b):
    return math.sqrt(math.pow(point_a.x - point_b.y, 2) + math.pow(point_a.y - point_b.y, 2))


def _convert_to_enum(intensity):
    if 15 > intensity:
        return ESoundIntensity.Weak
    elif 15 <= intensity <= 20:
        return ESoundIntensity.Normal
    elif 20 < intensity:
        return ESoundIntensity.Strong

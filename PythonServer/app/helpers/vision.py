# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from . import vision_calculator


def compute_agent_vision(strategy, position, limit, world):
    if strategy == 'dls':
        return _join_visions(vision_calculator.calculate_visions_dls(position, limit, world))
    if strategy == 'square':
        return vision_calculator.calculate_visions_square(position, limit, world)


# computes all polices visions and converts them into one list.
def compute_polices_visions(world):
    vision_positions = []
    for police in world.polices:
        if police.status == AgentStatus.Alive:
            vision_positions += compute_agent_vision('square', police.position,
                                                     world.constants.police_vision_distance, world)
    return _join_visions(vision_positions)


# computes all terrorists visions and converts them into one list.
def compute_terrorists_visions(world):
    vision_positions = []
    for terrorist in world.terrorists:
        if terrorist.status == AgentStatus.Alive:
            vision_positions += compute_agent_vision('square', terrorist.position,
                                                     world.constants.terrorist_vision_distance, world)
    return _join_visions(vision_positions)


# removes duplicates
def _join_visions(vision_positions):
    final_list = []
    for position in vision_positions:
        if any(position == new_pos for new_pos in final_list):
            continue
        else:
            final_list.append(position)
    return final_list

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from . import vision_compute


def compute_vision(algorithm, position, limit, world):
    if algorithm == 'dls':
        return vision_compute._depth_limited_search(position, limit, world)
    if algorithm == 'square':
        return vision_compute.compute_vision(position, limit, world)


# computes agent's vision based on its vision_distance.
def compute_agent_vision(agent, world):
    if type(agent) == Terrorist:
        return compute_vision('square', agent.position, world.constants.terrorist_vision_distance, world)
    elif type(agent) == Police:
        return compute_vision('square', agent.position, world.constants.police_vision_distance, world)


# computes all polices visions and converts them into one list.
def compute_polices_visions(world):
    vision_positions = []
    for police in world.polices:
        vision_positions += compute_agent_vision(police, world)
        # set(vision_positions) not working :/
    return _join_visions(vision_positions)


# computes all terrorists visions and converts them into one list.
def compute_terrorists_visions(world):
    vision_positions = []
    for terrorist in world.terrorists:
        vision_positions += compute_agent_vision(terrorist, world)
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

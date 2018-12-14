# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *


def _compute_agent_fog(agent, world):
    if type(agent) == Terrorist:
        return _depth_limited_search(agent.position, world.constants.terrorist_vision_distance)
    elif type(agent) == Police:
        return _depth_limited_search(agent.position, world.constants.police_vision_distance)


def compute_polices_fogs(world):
    fog_positions = []
    for police in world.polices:
        fog_positions += _compute_agent_fog(police, world)
        # set(fog_positions) not working :/
    return _join_fogs(fog_positions)


def compute_terrorists_fogs(world):
    fog_positions = []
    for terrorist in world.terrorists:
        fog_positions += _compute_agent_fog(terrorist, world)
    return _join_fogs(fog_positions)


# depth limited search with no specific goal position
def _depth_limited_search(position, limit):
    limit += 1
    sentinel = object()
    position_stack = [position]
    visited = []
    path = []

    while position_stack:
        current_position = position_stack.pop()
        if current_position not in visited:
            if current_position == sentinel:

                # finished this level; go back up one level
                limit += 1

            elif limit != 0:

                visited.append(current_position)
                # go one level deeper, push sentinel
                limit -= 1
                path.append(current_position)
                position_stack.append(sentinel)
                if limit != 0:
                    position_stack.extend(current_position.get_neighbours())
    return path


def _join_fogs(fog_positions):
    final_list = []
    for position in fog_positions:
        if any(position == new_pos for new_pos in final_list):
            continue
        else:
            final_list.append(position)
    return final_list

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *


# computes agent's fog based on its vision_distance.
def compute_agent_fog(agent, world):
    if type(agent) == Terrorist:
        return _depth_limited_search(agent.position, world.constants.terrorist_vision_distance, world)
    elif type(agent) == Police:
        return _depth_limited_search(agent.position, world.constants.police_vision_distance, world)


# computes all polices fogs and converts them into one list.
def compute_polices_fogs(world):
    fog_positions = []
    for police in world.polices:
        fog_positions += compute_agent_fog(police, world)
        # set(fog_positions) not working :/
    return _join_fogs(fog_positions)


# computes all terrorists fogs and converts them into one list.
def compute_terrorists_fogs(world):
    fog_positions = []
    for terrorist in world.terrorists:
        fog_positions += compute_agent_fog(terrorist, world)
    return _join_fogs(fog_positions)


# performs a depth limited search with no specific goal position.
def _depth_limited_search(position, limit, world):
    limit += 1
    sentinel = Position(None, None)
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
                    position_stack.extend(_get_valid_neighbours(current_position.get_neighbours(), world))
    return path


# removes duplicates
def _join_fogs(fog_positions):
    final_list = []
    for position in fog_positions:
        if any(position == new_pos for new_pos in final_list):
            continue
        else:
            final_list.append(position)
    return final_list


# returns valid neighbours based on world's board.
def _get_valid_neighbours(neighbours, world):
    valid_neighbours = []
    for neighbour in neighbours:
        if 0 <= neighbour.x < world.width:
            if 0 <= neighbour.y < world.height:
                valid_neighbours.append(neighbour)
    return valid_neighbours

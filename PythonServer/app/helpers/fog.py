# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


def _compute_agent_fog(agent):
    pass


def _compute_polices_fogs(positions):
    pass


def compute_terrorists_fogs(positions):
    pass


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

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


def _compute_agent_fog(agent):
    pass


def _compute_polices_fogs(positions):
    pass


def compute_terrorists_fogs(positions):
    pass


# TODO fix dls algorithm
def _depth_limited_search(position, limit):
    limit += 1
    sentinel = object()
    visited_stack = [position]
    path = []

    while visited_stack:
        current_position = visited_stack.pop()

        if current_position == sentinel:

            # finished this level; go back up one level
            limit += 1
            visited_stack.pop()

        elif limit != 0:

            # go one level deeper, push sentinel
            limit -= 1
            path.append(current_position)
            visited_stack.append(sentinel)
            if limit != 0:
                visited_stack.extend(current_position.get_neighbours())
    return path

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


# performs a depth limited search with no specific goal position.
def compute_visions_dls(position, limit, world):
    limit += 1
    sentinel = Position(None, None)
    position_stack = [position]
    visited = [position]
    path = []

    while position_stack:
        current_position = position_stack.pop()

        if current_position == sentinel:

            # finished this level; go back up one level
            limit += 1

        elif limit != 0:

            # go one level deeper, push sentinel
            limit -= 1
            path.append(current_position)
            position_stack.append(sentinel)

            for neighbour in _get_valid_neighbours(current_position.get_neighbours(), world):
                # if neighbour not in visited:
                position_stack.append(neighbour)
                visited.append(neighbour)
    return path


def compute_visions_square(position, limit, world):
    visions = []
    for x in range(position.x - limit, position.x + limit + 1):
        if _is_valid_position(x, world.width):
            for y in range(position.y - limit, position.y + limit + 1):
                if _is_valid_position(y, world.height):
                    if _get_manhattan_distance(position.x, position.y, x, y) <= limit:
                        visions.append(Position(x=x, y=y))
        else:
            continue
    return visions


# returns valid neighbours based on world's board.
def _get_valid_neighbours(neighbours, world):
    valid_neighbours = []
    for neighbour in neighbours:
        if 0 <= neighbour.x < world.width:
            if 0 <= neighbour.y < world.height:
                valid_neighbours.append(neighbour)
    return valid_neighbours


def _is_valid_position(n, radius):
    return 0 <= n < radius


def _get_manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

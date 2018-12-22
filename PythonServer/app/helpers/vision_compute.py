# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


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


def compute_vision(position, limit, world):
    visions = []
    for x in range(position.x - limit, position.x + limit + 1):
        if _is_valid_position(x, world.height):
            for y in range(position.y - limit, position.y + limit + 1):
                if _is_valid_position(y, world.height):
                    if get_manhattan_distance(position.x, position.y, x, y) <= limit:
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


def get_manhattan_distance(x1, y1, x2, y2):
     return abs(x1-x2) + abs(y1-y2)
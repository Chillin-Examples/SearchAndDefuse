# -*- coding: utf-8 -*-

# python imports
from collections import deque


# performs a Depth Limited Search
def dls(world, start_position, max_depth, goal, valid_ecells=None):
    if not goal is None and goal.is_equal(start_position):
        return 0, []

    positions = deque([start_position])
    depths = deque([0])
    visited = [start_position]

    while len(positions) > 0:
        pos = positions.popleft()
        depth = depths.popleft()

        if max_depth == None or depth < max_depth:
            # Check neighbours
            neighbours = pos.get_neighbours(world)
            for neighbour in neighbours:
                if not neighbour in visited:
                    # Check ecell
                    board_ecell = world.board[neighbour.y][neighbour.x]
                    if not valid_ecells is None and not board_ecell in valid_ecells:
                        continue

                    # Update visited
                    visited.append(neighbour)

                    # Check goal
                    if not goal is None and neighbour == goal:
                        return depth + 1, visited

                    # Update queue
                    positions.append(neighbour)
                    depths.append(depth + 1)

    return None, visited

# -*- coding: utf-8 -*-

# project imports
from..ks.models import Position

class FogDetector:

    def __init__(self, terrorist_vision_distance, police_vision_distance):
        self.police_vision_distance = police_vision_distance
        self.terrorist_vision_distance = terrorist_vision_distance

    def _compute_agent_fog(self, agent):
        pass

    def _compute_polices_fogs(self, positions):
        pass

    def compute_terrorists_fogs(self, positions):
        pass

    # TODO fix dls algorithm
    def _depth_limited_search(self, position, limit):
        sentinel = object()
        visited_stack = [position]
        path = []

        while visited_stack:
            current_position = visited_stack.pop()

            if current_position == sentinel:

                # finished this level; go back up one level
                limit += 1
                path.pop()

            elif limit != 0:

                # go one level deeper, push sentinel
                limit -= 1
                path.append(current_position)
                visited_stack.append(sentinel)
                # visited_stack.extend()
        return path

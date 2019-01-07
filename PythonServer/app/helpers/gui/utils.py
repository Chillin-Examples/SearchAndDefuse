# -*- coding: utf-8 -*-

# python imports
import math


class GuiUtils:

    def __init__(self, cell_size):
        self.cell_size = cell_size

    def get_canvas_position(self, position, center_origin=True):
        addition = int(self.cell_size / 2) if center_origin else 0
        return {
            'x': position.x * self.cell_size + addition,
            'y': position.y * self.cell_size + addition
        }

    def _get_line_xys(self, agent, curr_val, max_val, offset):
        canvas_pos = self.get_canvas_position(agent.position.x, agent.position.y)
        y1 = y2 = canvas_pos['y'] + int(self.cell_size / 2) - 10 + offset
        x1 = canvas_pos['x'] - int(self.cell_size / 2) + 5
        if curr_val == 0:
            x2 = x1
        else:
            x2 = x1 + math.ceil((self.cell_size - 10) * (curr_val / max_val))

        return x1, y1, x2, y2

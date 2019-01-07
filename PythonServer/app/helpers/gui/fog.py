# -*- coding: utf-8 -*-

# python imports
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ...ks.commands import *
from ...ks.models import *
from ...gui_events import GuiEventType


def initialize_fogs(handler, canvas):
    for y in range(handler.world.height):
        for x in range(handler.world.width):
            cell = handler.world.board[y][x]
            canvas_pos = handler.utils.get_canvas_position(Position(x=x, y=y), center_origin=False)
            # is_visible = False
            # for side in handler._sides:
            #     for visible_cell_pos in handler._world.visions[side]:
            #         if visible_cell_pos.x == x and visible_cell_pos.y == y:
            #             is_visible = True
            #             break
            # if not is_visible:
            # if cell != ECell.Wall:
            new_fog_ref = canvas.create_image('Fog', canvas_pos['x'], canvas_pos['y'],
                                              scale_type=ScaleType.ScaleToWidth,
                                              scale_value=handler.cell_size)
            handler.fog_refs.append(new_fog_ref)


def update_fogs(handler):
    i = 0
    for y in range(handler.world.height):
        for x in range(handler.world.width):
            cell = handler.world.board[y][x]
            canvas_pos = handler.utils.get_canvas_position(Position(x=x, y=y), center_origin=False)
            is_visible = False
            for side in handler.sides:
                for visible_cell_pos in handler.world.visions[side]:
                    if visible_cell_pos.x == x and visible_cell_pos.y == y:
                        is_visible = True
                        break
            if not is_visible:
                if cell != ECell.Wall:
                    handler.canvas.edit_image(handler.fog_refs[i], canvas_pos['x'], canvas_pos['y'],
                                            scale_type=ScaleType.ScaleToWidth,
                                            scale_value=handler.cell_size)
                    i += 1
    for index in range(i, len(handler.fog_refs)):
        handler.canvas.edit_image(handler.fog_refs[index], 5000, 5000,
                                scale_type=ScaleType.ScaleToWidth,
                                scale_value=handler.cell_size)

# -*- coding: utf-8 -*-

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ...ks.models import *


def initialize_board(handler, canvas):
    for y in range(handler.world.height):
        for x in range(handler.world.width):
            cell = handler.world.board[y][x]
            canvas_pos = handler.utils.get_canvas_position(Position(x=x, y=y), center_origin=False)

            # Draw non-player cells
            if cell == ECell.Empty:
                canvas.create_image('Empty', canvas_pos['x'], canvas_pos['y'],
                                    scale_type=ScaleType.ScaleToWidth, scale_value=handler.cell_size)
            elif cell == ECell.Wall:
                canvas.create_image('Wall', canvas_pos['x'], canvas_pos['y'],
                                    scale_type=ScaleType.ScaleToWidth, scale_value=handler.cell_size)
            elif cell == ECell.SmallBombSite:
                handler.small_bomb_ref = canvas.create_image('SmallBomb', canvas_pos['x'], canvas_pos['y'],
                                                             scale_type=ScaleType.ScaleToWidth,
                                                             scale_value=handler.cell_size)
            elif cell == ECell.MediumBombSite:
                handler.medium_bomb_ref = canvas.create_image('MediumBomb', canvas_pos['x'], canvas_pos['y'],
                                                              scale_type=ScaleType.ScaleToWidth,
                                                              scale_value=handler.cell_size)
            elif cell == ECell.LargeBombSite:
                handler.large_bomb_ref = canvas.create_image('LargeBomb', canvas_pos['x'], canvas_pos['y'],
                                                             scale_type=ScaleType.ScaleToWidth,
                                                             scale_value=handler.cell_size)
            elif cell == ECell.VastBombSite:
                handler.vast_bomb_ref = canvas.create_image('VastBomb', canvas_pos['x'], canvas_pos['y'],
                                                            scale_type=ScaleType.ScaleToWidth,
                                                            scale_value=handler.cell_size)

    # Draw Agents
    for side in handler.sides:
        agents = handler.world.polices if side == 'Police' else handler.world.terrorists
        dead_img_name = 'DeadPolice' if side == 'Police' else 'DeadTerrorist'

        for agent in agents:
            position = agent.position

            canvas_pos = handler.utils.get_canvas_position(agent.position)
            agent.angle = handler.angle[EDirection.Left.name]
            agent.img_ref = canvas.create_image(side, canvas_pos['x'], canvas_pos['y'],
                                                center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                                scale_value=handler.cell_size)
            handler.img_refs[side][agent.id] = agent.img_ref

            handler.dead_img_refs[side][agent.id] = handler.canvas.create_image(dead_img_name, 7000, 7000,
                                                                                scale_type=ScaleType.ScaleToWidth,
                                                                                scale_value=handler.cell_size,
                                                                                center_origin=True)

# -*- coding: utf-8 -*-

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ...ks.models import *


def update_board_on_bomb_cancel(handler, bombs_planting):
    for bomb in bombs_planting:
        canvas_pos = handler.utils.get_canvas_position(bomb['bomb_position'])
        board_cell = handler.world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
        if board_cell == ECell.SmallBombSite:
            handler.canvas.create_image('SmallBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.MediumBombSite:
            handler.canvas.create_image('MediumBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.LargeBombSite:
            handler.canvas.create_image('LargeBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.VastBombSite:
            handler.canvas.create_image('VastBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)


def update_board_on_planting(handler, bombs_planting):
    for bomb in bombs_planting:
        canvas_pos = handler.utils.get_canvas_position(bomb['bomb_position'])
        board_cell = handler.world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
        if board_cell == ECell.SmallBombSite:
            handler.canvas.create_image('PlantingBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.MediumBombSite:
            handler.canvas.create_image('PlantingBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.LargeBombSite:
            handler.canvas.create_image('PlantingBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.VastBombSite:
            handler.canvas.create_image('PlantingBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)


def update_board_on_planted(handler, bombs_planted):
    for bomb in bombs_planted:
        canvas_pos = handler.utils.get_canvas_position(bomb['bomb_position'])
        board_cell = handler.world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
        if board_cell == ECell.SmallBombSite:
            handler.canvas.create_image('PlantedBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.MediumBombSite:
            handler.canvas.create_image('PlantedBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.LargeBombSite:
            handler.canvas.create_image('PlantedBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.VastBombSite:
            handler.canvas.create_image('PlantedBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)


def update_board_on_explode(handler, bombs_exploded):
    for bomb in bombs_exploded:
        canvas_pos = handler.utils.get_canvas_position(bomb['bomb_position'])
        board_cell = handler.world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
        if board_cell == ECell.Empty:
            handler.canvas.create_image('ExplodedBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        # elif board_cell == ECell.MediumBombSite:
        #     handler.canvas.create_image('ExplodedBomb', canvas_pos['x'], canvas_pos['y'],
        #                               center_origin=True, scale_type=ScaleType.ScaleToWidth,
        #                               scale_value=handler.cell_size)
        # elif board_cell == ECell.LargeBombSite:
        #     handler.canvas.create_image('ExplodedBomb', canvas_pos['x'], canvas_pos['y'],
        #                               center_origin=True, scale_type=ScaleType.ScaleToWidth,
        #                               scale_value=handler.cell_size)
        # elif board_cell == ECell.VastBombSite:
        #     handler.canvas.create_image('ExplodedBomb', canvas_pos['x'], canvas_pos['y'],
        #                               center_origin=True, scale_type=ScaleType.ScaleToWidth,
        #                               scale_value=handler.cell_size)


def update_board_on_defuse(handler, bombs_defusing):
    for bomb in bombs_defusing:
        canvas_pos = handler.utils.get_canvas_position(bomb['bomb_position'])
        board_cell = handler.world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
        if board_cell == ECell.Empty:
            handler.canvas.create_image('Empty', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.SmallBombSite:
            handler.canvas.create_image('SmallBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.MediumBombSite:
            handler.canvas.create_image('MediumBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.LargeBombSite:
            handler.canvas.create_image('LargeBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.VastBombSite:
            handler.canvas.create_image('VastBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)


def update_board_on_defusing(handler, bombs_defusing):
    for bomb in bombs_defusing:
        canvas_pos = handler.utils.get_canvas_position(bomb['bomb_position'])
        board_cell = handler.world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
        if board_cell == ECell.SmallBombSite:
            handler.canvas.create_image('DefusingBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.MediumBombSite:
            handler.canvas.create_image('DefusingBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.LargeBombSite:
            handler.canvas.create_image('DefusingBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)
        elif board_cell == ECell.VastBombSite:
            handler.canvas.create_image('DefusingBomb', canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                        scale_value=handler.cell_size)

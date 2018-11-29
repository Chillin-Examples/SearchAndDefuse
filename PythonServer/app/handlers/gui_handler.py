# -*- coding: utf-8 -*-

# python imports
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ..ks.commands import *
from ..ks.models import *


class GuiHandler:

    def __init__(self, world, sides, canvas, config):
        self._world = world
        self._sides = sides
        self._canvas = canvas
        self._config = config
        self._utils = GuiUtils()
        self._img_refs = {side: {} for side in self._sides}

    def initialize(self):
        canvas = self._canvas
        config = self._config

        # Draw background
        background_ref = canvas.create_image('Background', 0, 0)
        canvas.edit_image(background_ref, scale_type=ScaleType.ScaleToWidth,
                          scale_value=canvas.width)

        # Initialize Commands
        self.angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }

        self._scale_factor = (canvas.width) / (
                self._world.width * config['cell_size'])
        self._scale_percent = math.ceil(self._scale_factor * 100)
        self._cell_size = math.ceil(config['cell_size'] * self._scale_factor)
        self._font_size = int(self._cell_size / 2)

        self._initialize_board(canvas)

    def update(self, gui_events):
        terrorist_IDs, police_IDs = [], []
        for event in gui_events:
            if not event == 'error':
                if event.type.value == 0:  # move police
                    police_IDs.append(event.payload['agent_id'])
                elif event.type.value == 1:  # move terrorist
                    terrorist_IDs.append(event.payload['agent_id'])
        if (len(terrorist_IDs) != 0) or (len(police_IDs) != 0):
            self._update_board_on_move(self._canvas, terrorist_IDs, police_IDs)

    def _update_board_on_move(self, canvas, terrorist_IDs, polices_IDs):

        # Update Terrorists
        for terrorist in self._world.terrorists:
            if terrorist.id in terrorist_IDs:
                position = terrorist.position

                canvas_pos = self._utils.get_canvas_position(position.x, position.y, self._cell_size,
                                                             center_origin=True)
                terrorist.angle = self.angle[EDirection.Left.name]
                terrorist.img_ref = canvas.edit_image(self._img_refs["Terrorist"][terrorist.id], canvas_pos['x'],
                                                      canvas_pos['y'],
                                                      center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                                      scale_value=self._cell_size)

        # Update Polices
        for police in self._world.polices:
            if police.id in polices_IDs:
                position = police.position
                canvas_pos = self._utils.get_canvas_position(position.x, position.y, self._cell_size,
                                                             center_origin=True)
                police.angle = self.angle[EDirection.Left.name]
                police.img_ref = canvas.edit_image(self._img_refs["Police"][police.id], canvas_pos['x'],
                                                   canvas_pos['y'],
                                                   center_origin=True,
                                                   scale_type=ScaleType.ScaleToWidth,
                                                   scale_value=self._cell_size)

    def _initialize_board(self, canvas):
        for y in range(self._world.height):
            for x in range(self._world.width):
                cell = self._world.board[y][x]

                # Draw non-player cells
                if cell == ECell.Empty:
                    canvas.create_image('Empty', x * self._cell_size, y * self._cell_size,
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self._cell_size)
                elif cell == ECell.Wall:
                    canvas.create_image('Wall', x * self._cell_size, y * self._cell_size,
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self._cell_size)
                elif cell == ECell.SmallBombSite:
                    canvas.create_image('SmallBomb', x * self._cell_size, y * self._cell_size,
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self._cell_size)
                elif cell == ECell.MediumBombSite:
                    canvas.create_image('MediumBomb', x * self._cell_size, y * self._cell_size,
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self._cell_size)
                elif cell == ECell.LargeBombSite:
                    canvas.create_image('LargeBomb', x * self._cell_size, y * self._cell_size,
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self._cell_size)
                elif cell == ECell.VastBombSite:
                    canvas.create_image('VastBomb', x * self._cell_size, y * self._cell_size,
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self._cell_size)

        # Draw Terrorists
        for terrorist in self._world.terrorists:
            position = terrorist.position

            canvas_pos = self._utils.get_canvas_position(position.x, position.y, self._cell_size,
                                                         center_origin=True)
            terrorist.angle = self.angle[EDirection.Left.name]
            terrorist.img_ref = canvas.create_image("Terrorist", canvas_pos['x'], canvas_pos['y'],
                                                    center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                                    scale_value=self._cell_size)
            self._img_refs["Terrorist"][terrorist.id] = terrorist.img_ref

        # Draw Polices
        for police in self._world.polices:
            position = police.position
            canvas_pos = self._utils.get_canvas_position(position.x, position.y, self._cell_size,
                                                         center_origin=True)
            police.angle = self.angle[EDirection.Left.name]
            police.img_ref = canvas.create_image("Police", canvas_pos['x'], canvas_pos['y'],
                                                 center_origin=True,
                                                 scale_type=ScaleType.ScaleToWidth,
                                                 scale_value=self._cell_size)
            self._img_refs["Police"][police.id] = police.img_ref


class GuiUtils:

    def __init__(self):
        pass

    def get_canvas_position(self, x, y, cell_size, center_origin=False):
        addition = int(cell_size / 2) if center_origin else 0
        return {
            'x': x * cell_size + addition,
            'y': y * cell_size + addition
        }

    def _get_line_xys(self, player, curr_val, max_val, offset, cell_size):
        position = player.position
        canvas_pos = self.get_canvas_position(position.x, position.y, cell_size, center_origin=True)
        y1 = y2 = canvas_pos['y'] + int(cell_size / 2) - 10 + offset
        x1 = canvas_pos['x'] - int(cell_size / 2) + 5
        if curr_val == 0:
            x2 = x1
        else:
            x2 = x1 + math.ceil((cell_size - 10) * (curr_val / max_val))

        return (x1, y1, x2, y2)

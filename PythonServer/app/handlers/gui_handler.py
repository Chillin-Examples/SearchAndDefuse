# -*- coding: utf-8 -*-

# python imports
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ..ks.commands import *
from ..ks.models import *
from ..gui_events import GuiEventType


class GuiHandler:

    def __init__(self, world, sides, canvas, config):

        self._world = world
        self._sides = sides
        self._canvas = canvas
        self._config = config
        self._scale_factor = canvas.width / (self._world.width * config['cell_size'])
        self._scale_percent = math.ceil(self._scale_factor * 100)
        self._cell_size = math.ceil(config['cell_size'] * self._scale_factor)
        self._font_size = int(self._cell_size / 2)
        self._utils = GuiUtils(self._cell_size)
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

        self._initialize_board(canvas)

    def update(self, gui_events):
        terrorist_info, police_info = [], []
        for event in gui_events:
            if event.type == GuiEventType.move_police:
                police_info.append((event.payload['agent_id'], event.payload['agent_position']))
            elif event.type == GuiEventType.move_terrorist:
                terrorist_info.append((event.payload['agent_id'], event.payload['agent_position']))

        if (len(terrorist_info) != 0) or (len(police_info) != 0):
            self._update_board_on_move(self._canvas, terrorist_info, police_info)

    def _update_board_on_move(self, canvas, terrorist_info, police_info):

        # Update Terrorists
        for terrorist in terrorist_info:
            id, position = terrorist

            canvas_pos = self._utils.get_canvas_position(position.x, position.y,
                                                         center_origin=True)
            # terrorist.angle = self.angle[EDirection.Left.name]
            canvas.edit_image(self._img_refs["Terrorist"][id], canvas_pos['x'],
                              canvas_pos['y'],
                              center_origin=True, scale_type=ScaleType.ScaleToWidth,
                              scale_value=self._cell_size)

        # Update Polices
        for police in police_info:
            id, position = police
            canvas_pos = self._utils.get_canvas_position(position.x, position.y,
                                                         center_origin=True)
            # police.angle = self.angle[EDirection.Left.name]
            canvas.edit_image(self._img_refs["Police"][id], canvas_pos['x'],
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

            canvas_pos = self._utils.get_canvas_position(position.x, position.y,
                                                         center_origin=True)
            terrorist.angle = self.angle[EDirection.Left.name]
            terrorist.img_ref = canvas.create_image("Terrorist", canvas_pos['x'], canvas_pos['y'],
                                                    center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                                    scale_value=self._cell_size)
            self._img_refs["Terrorist"][terrorist.id] = terrorist.img_ref

        # Draw Polices
        for police in self._world.polices:
            position = police.position
            canvas_pos = self._utils.get_canvas_position(position.x, position.y,
                                                         center_origin=True)
            police.angle = self.angle[EDirection.Left.name]
            police.img_ref = canvas.create_image("Police", canvas_pos['x'], canvas_pos['y'],
                                                 center_origin=True,
                                                 scale_type=ScaleType.ScaleToWidth,
                                                 scale_value=self._cell_size)
            self._img_refs["Police"][police.id] = police.img_ref


class GuiUtils:

    def __init__(self, cell_size):
        self._cell_size = cell_size

    def get_canvas_position(self, x, y, center_origin=False):
        addition = int(self._cell_size / 2) if center_origin else 0
        return {
            'x': x * self._cell_size + addition,
            'y': y * self._cell_size + addition
        }

    def _get_line_xys(self, player, curr_val, max_val, offset):
        position = player.position
        canvas_pos = self.get_canvas_position(position.x, position.y, center_origin=True)
        y1 = y2 = canvas_pos['y'] + int(self._cell_size / 2) - 10 + offset
        x1 = canvas_pos['x'] - int(self._cell_size / 2) + 5
        if curr_val == 0:
            x2 = x1
        else:
            x2 = x1 + math.ceil((self._cell_size - 10) * (curr_val / max_val))

        return x1, y1, x2, y2

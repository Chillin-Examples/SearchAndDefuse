# -*- coding: utf-8 -*-

# python imports
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ..ks.commands import *
from ..ks.models import *


class GuiHandler:

    def __init__(self, world, sides, canvas):
        self.world = world
        self.sides = sides
        self.canvas = canvas

    def update(self, gui_events):
        pass

    def initialize(self, canvas, config, world):
        # Draw background
        background_ref = self.canvas.create_image('Background', 0, 0)
        canvas.edit_image(background_ref, scale_type=ScaleType.ScaleToWidth,
                          scale_value=self.canvas.width - config['statuses_width'])
        # Initialize Commands
        self.move_angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }

        self.plant_angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }

        self.defuse_angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }
        self.scale_factor = (canvas.width) / (
                self.world.width * self.world.map_config['cell_size'])
        self.scale_percent = math.ceil(self.scale_factor * 100)
        self.cell_size = math.ceil(config['cell_size'] * self.scale_factor)
        self.font_size = int(self.cell_size / 2)

        # Draw Board
        for y in range(world.height):
            for x in range(world.width):
                cell = world.board[y][x]
                if cell == ECell.Empty:
                    self.canvas.create_image('Empty', x * self.cell_size, y * self.cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
                elif cell == ECell.Wall:
                    self.canvas.create_image('Wall', x * self.cell_size, y * self.cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
                elif cell == ECell.SmallBombSite:
                    self.canvas.create_image('SmallBomb', x * self.cell_size, y * self.cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
                elif cell == ECell.MediumBombSite:
                    self.canvas.create_image('MediumBomb', x * self.cell_size, y * self.cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
                elif cell == ECell.LargeBombSite:
                    self.canvas.create_image('LargeBomb', x * self.cell_size, y * self.cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
                elif cell == ECell.VastBombSite:
                    self.canvas.create_image('VastBomb', x * self.cell_size, y * self.cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)

                # Draw Terrorists
                for terrorist in world.terrorists:
                    position = terrorist.position
                    canvas_pos = GuiUtils()._get_canvas_position(position.x, position.y, self.cell_size,
                                                                 center_origin=True)
                    terrorist.angle = self.move_angle[EDirection.Left.name]
                    terrorist.img_ref = self.canvas.create_image("Terrorist", canvas_pos['x'], canvas_pos['y'],
                                                                 center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                                                 scale_value=self.cell_size)
                    # terrorist.id_ref = self.canvas.create_text(str(terrorist.id),canvas_pos['x'] +self.cell_size // 2 - 10,canvas_pos['y'] -self.cell_size // 2, text_color,font_size, center_origin=True)
                    x1, y1, x2, y2 = GuiUtils()._get_line_xys(terrorist, terrorist.health, terrorist.max_health, 0)
                    terrorist.health_ref = canvas.create_line(x1, y1, x2, y2,
                                                              canvas.make_rgba(255, 0, 0, 150),
                                                              stroke_width=5)
                    x1, y1, x2, y2 = GuiUtils()._get_line_xys(terrorist, terrorist.laser_count,
                                                              terrorist.max_laser_count, 5)
                    terrorist.ammo_ref = canvas.create_line(x1, y1, x2, y2, canvas.make_rgba(0, 0, 255, 150),
                                                            stroke_width=5)

                # Draw Polices
                for police in world.polices:
                    position = police.position
                    canvas_pos = GuiUtils()._get_canvas_position(position.x, position.y, self.cell_size,
                                                                 center_origin=True)
                    police.angle = self.move_angle[EDirection.Left.name]
                    police.img_ref = self.canvas.create_image("Police", canvas_pos['x'], canvas_pos['y'],
                                                              center_origin=True,
                                                              scale_type=ScaleType.ScaleToWidth,
                                                              scale_value=self.cell_size)
                    # terrorist.id_ref = self.canvas.create_text(str(terrorist.id),canvas_pos['x'] +self.cell_size // 2 - 10,canvas_pos['y'] -self.cell_size // 2, text_color,font_size, center_origin=True)
                    x1, y1, x2, y2 = GuiUtils()._get_line_xys(police, police.health, police.max_health, 0)
                    police.health_ref = canvas.create_line(x1, y1, x2, y2,
                                                           canvas.make_rgba(255, 0, 0, 150),
                                                           stroke_width=5)
                    x1, y1, x2, y2 = GuiUtils()._get_line_xys(police, police.laser_count,
                                                              police.max_laser_count, 5)
                    police.ammo_ref = canvas.create_line(x1, y1, x2, y2, canvas.make_rgba(0, 0, 255, 150),
                                                         stroke_width=5)


class GuiUtils:

    def __init__(self):
        pass

    def _get_canvas_position(self, x, y, cell_size, center_origin=False):
        addition = int(cell_size / 2) if center_origin else 0
        return {
            'x': x * cell_size + addition,
            'y': y * cell_size + addition
        }

    def _get_line_xys(self, player, curr_val, max_val, offset, cell_size):
        position = player.position
        canvas_pos = self._get_canvas_position(position.x, position.y, cell_size, center_origin=True)
        y1 = y2 = canvas_pos['y'] + int(cell_size / 2) - 10 + offset
        x1 = canvas_pos['x'] - int(cell_size / 2) + 5
        if curr_val == 0:
            x2 = x1
        else:
            x2 = x1 + math.ceil((cell_size - 10) * (curr_val / max_val))

        return (x1, y1, x2, y2)

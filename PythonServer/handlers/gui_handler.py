from chillin_server.gui.canvas_elements import ScaleType
from ..ks.commands import *
from ..ks.models import *


class GuiHandler:
    world = None
    sides = []
    canvas = None
    def __init__(self, world, sides, canvas):
        self.world = world
        self.sides = sides
        self.canvas = canvas

    def update(self, gui_events):
        pass

    def initialize(self, background_ref, canvas, config, world, cell_size,):
        # Draw background
        background_ref = self.canvas.create_image('Background', 0, 0)
        canvas.edit_image(background_ref, scale_type=ScaleType.ScaleToWidth,
                               scale_value=self.canvas.width - config['statuses_width'])

        # Draw Board
        for y in range(world.height):
            for x in range(world.width):
                cell = world.board[y][x]
                if cell == ECell.Empty:
                    self.canvas.create_image('Empty', x * cell_size, y * cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=cell_size)
                elif cell == ECell.Wall:
                    self.canvas.create_image('Wall', x * cell_size, y * cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=cell_size)
                elif cell == ECell.SmallBombSite:
                    self.canvas.create_image('SmallBomb', x * cell_size, y * cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=cell_size)
                elif cell == ECell.MediumBombSite:
                    self.canvas.create_image('MediumBomb', x * cell_size, y * cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=cell_size)
                elif cell == ECell.LargeBombSite:
                    self.canvas.create_image('LargeBomb', x * cell_size, y * cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=cell_size)
                elif cell == ECell.VastBombSite:
                    self.canvas.create_image('VastBomb', x * cell_size, y * cell_size,
                                             scale_type=ScaleType.ScaleToWidth, scale_value=cell_size)

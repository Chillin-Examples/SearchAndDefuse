from chillin_server.gui.canvas_elements import ScaleType
from ..ks.commands import *
from ..ks.models import *
from ..chillin_utilities import pos

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

                # Draw Players
                for side in self.sides:
                    img_name = side
                    for banana in self.world.bananas[side]:
                        position = pos.Pos(position=banana.position)
                        canvas_pos = self._get_canvas_position(pos.x, pos.y, center_origin=True)
                        banana.angle = self.move_angle[EMoveDir.Left.name]
                        banana.img_ref = self.canvas.create_image(img_name, canvas_pos['x'], canvas_pos['y'],
                                                                  center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                                                  scale_value=self.cell_size)

                        text_color = self.canvas.make_rgba(0, 0, 255,
                                                           255) if side == 'Chiquita' else self.canvas.make_rgba(255, 0,
                                                                                                                 0, 255)
                        banana.id_ref = self.canvas.create_text(str(banana.id),
                                                                canvas_pos['x'] + self.cell_size // 2 - 10,
                                                                canvas_pos['y'] - self.cell_size // 2, text_color,
                                                                self.font_size, center_origin=True)

                        x1, y1, x2, y2 = self._get_line_xys(banana, banana.health, banana.max_health, 0)
                        banana.health_ref = self.canvas.create_line(x1, y1, x2, y2,
                                                                    self.canvas.make_rgba(255, 0, 0, 150),
                                                                    stroke_width=5)

                        x1, y1, x2, y2 = self._get_line_xys(banana, banana.laser_count, banana.max_laser_count, 5)
                        banana.ammo_ref = self.canvas.create_line(x1, y1, x2, y2, self.canvas.make_rgba(0, 0, 255, 150),
                                                                  stroke_width=5)

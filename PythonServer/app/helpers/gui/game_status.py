# -*- coding: utf-8 -*-

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType


class GameStatus:

    def __init__(self, world, canvas, font_size, cell_size):
        self._world = world
        self._canvas = canvas
        self._statusbar = []
        self._font_size = font_size
        self._cell_size = cell_size
        self._num_bombs_exploded = 0
        self._num_bombs_defused = 0
        self._num_bombs_planted = 0
        self._police_score = 0
        self._terrorist_score = 0
        self._remaining_cycles = 0

    def initialize(self):
        sides_status = [[[], [], []],
                        [[], [], []],
                        [[], [], []]]

        general_status = [[], [], [], []]

        self._statusbar = [sides_status, general_status]

        # side status
        for i_side_status in range(0, 3):
            for j_side_status in range(0, 3):
                self._statusbar[0][i_side_status][j_side_status] = {
                    "row": j_side_status,
                    "col": i_side_status,
                    "x": int(
                        (self._canvas.width - (
                                (3 - i_side_status) * int(self._world.statusbar_width / 3))) / 3 - 600),
                    "y": int(((j_side_status * 250) + 0) / 1.5 + 2100),  # 10 is y0
                    "ref": None
                }

        for i_general_status in range(0, 2):
            self._statusbar[1][i_general_status] = {
                "row": 0,
                "col": i_general_status,
                "x": int(380),
                # int((self._canvas.width - (2 - i_general_status) * int(self._world.statusbar_width / 2))/3-60),
                "y": int(i_general_status * 340 + 2200)  # (600 + 0)/2 + 2000)
            }

        self._statusbar[0][0][0]['ref'] = self._canvas.create_image('PoliceLogo',
                                                                        self._statusbar[0][0][0]['y'],
                                                                        self._statusbar[0][0][0]['x'],
                                                                        center_origin=True,
                                                                        scale_type=ScaleType.ScaleToWidth,
                                                                        scale_value=self._cell_size)

        self._statusbar[0][0][1]['ref'] = self._canvas.create_text('vs.',
                                                                    self._statusbar[0][0][1]['y'],
                                                                    self._statusbar[0][0][1]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)
        self._statusbar[0][0][2]['ref'] = self._canvas.create_image('TerroristLogo',
                                                                        self._statusbar[0][0][2]['y'],
                                                                        self._statusbar[0][0][2]['x'],
                                                                        center_origin=True,
                                                                        scale_type=ScaleType.ScaleToWidth,
                                                                        scale_value=self._cell_size)

        self._statusbar[0][1][0]['ref'] = self._canvas.create_text('0',
                                                                    self._statusbar[0][1][0]['y'],
                                                                    self._statusbar[0][1][0]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)

        self._statusbar[0][1][1]['ref'] = self._canvas.create_text('score',
                                                                    self._statusbar[0][1][1]['y'],
                                                                    self._statusbar[0][1][1]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)

        self._statusbar[0][1][2]['ref'] = self._canvas.create_text('0',
                                                                    self._statusbar[0][1][2]['y'],
                                                                    self._statusbar[0][1][2]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)

        self._statusbar[0][2][0]['ref'] = self._canvas.create_text('0',
                                                                    self._statusbar[0][2][0]['y'],
                                                                    self._statusbar[0][2][0]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)

        self._statusbar[0][2][1]['ref'] = self._canvas.create_text('bombs',
                                                                    self._statusbar[0][2][1]['y'],
                                                                    self._statusbar[0][2][1]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)

        self._statusbar[0][2][2]['ref'] = self._canvas.create_text('0',
                                                                    self._statusbar[0][2][2]['y'],
                                                                    self._statusbar[0][2][2]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)

        self._statusbar[1][0]['ref'] = self._canvas.create_text('remaining cycles:',
                                                                    self._statusbar[1][0]['y'],
                                                                    self._statusbar[1][0]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)

        self._statusbar[1][1]['ref'] = self._canvas.create_text(str(self._world.constants.max_cycles),
                                                                    self._statusbar[1][1]['y'],
                                                                    self._statusbar[1][1]['x'],
                                                                    self._canvas.make_rgba(0, 0, 0, 255),
                                                                    self._font_size * 2,
                                                                    center_origin=True)

    def update(self, current_cycle):
        # scores
        self._police_score = self._world.scores['Police']
        self._terrorist_score = self._world.scores['Terrorist']

        # cycles remaining
        self._remaining_cycles = self._world.constants.max_cycles - current_cycle

        # overall bomb number
        self.update_planted_number()

        self._canvas.edit_text(self._statusbar[0][1][0]['ref'], text=str(self._police_score))
        self._canvas.edit_text(self._statusbar[0][1][2]['ref'], str(self._terrorist_score))
        self._canvas.edit_text(self._statusbar[0][2][0]['ref'], str(self._num_bombs_defused))
        self._canvas.edit_text(self._statusbar[0][2][2]['ref'], str(self._num_bombs_exploded))
        self._canvas.edit_text(self._statusbar[1][1]['ref'], str(self._remaining_cycles))

    def update_exploded_number(self):
        self._num_bombs_exploded += 1

    def update_defused_number(self):
        self._num_bombs_defused += 1

    def update_planted_number(self):
        self._num_bombs_planted = self._num_bombs_exploded + self._num_bombs_defused

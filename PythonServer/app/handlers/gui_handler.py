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
        self._fog_refs = []

    def initialize(self):
        canvas = self._canvas
        config = self._config
        print("AAAAAAAAAAAA")
        print(len(self._world.visions["Terrorist"]))
        for i in self._world.visions["Terrorist"]:
            print("POS:", i.x, ",", i.y)
        print("AAAAAAAAAAAA")

        # Draw background
        background_ref = canvas.create_image('Background', 0, 0)
        canvas.edit_image(background_ref, scale_type=ScaleType.ScaleToWidth,
                          scale_value=canvas.width)

        self.angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }

        self._initialize_board(canvas)
        self._initialize_fogs(canvas)

    def update(self, gui_events, world):
        self._world = world
        moving_terrorists, moving_polices, bombs_defusing, bombs_defused, bombs_op_canceled = [], [], [], [], []
        bombs_events = {"planting": [], "planted": [], "exploded": []}

        for event in gui_events:
            if event.type == GuiEventType.MovePolice:
                moving_polices.append(event.payload)
            if event.type == GuiEventType.MoveTerrorist:
                moving_terrorists.append(event.payload)
            if event.type == GuiEventType.DefusingBomb:
                bombs_defusing.append(event.payload)
                print(len(bombs_defusing))
            if event.type == GuiEventType.DefusedBomb:
                bombs_defused.append(event.payload)
            if event.type == GuiEventType.PlantingBomb:
                bombs_events['planting'].append(event.payload)
            if event.type == GuiEventType.PlantedBomb:
                bombs_events['planted'].append(event.payload)
            if event.type == GuiEventType.ExplodeBomb:
                bombs_events['exploded'].append(event.payload)
            if event.type == GuiEventType.CancelBombOp:
                bombs_op_canceled.append(event.payload)

        if (len(moving_terrorists) != 0) or (len(moving_polices) != 0):
            self._update_board_on_move(moving_terrorists, moving_polices)

        if len(bombs_events['planting']) != 0:
            self._update_board_on_planting(bombs_events['planting'])

        if len(bombs_events['planted']) != 0:
            self._update_board_on_planted(bombs_events['planted'])

        if len(bombs_events['exploded']) != 0:
            self._update_board_on_explode(bombs_events['exploded'])

        if len(bombs_defusing) != 0:
            self._update_board_on_defusing(bombs_defusing)

        if len(bombs_defused) != 0:
            self._update_board_on_defuse(bombs_defused)

        if len(bombs_op_canceled) != 0:
            self._update_board_on_bomb_cancel(bombs_op_canceled)

        self._update_fogs()

    def _update_board_on_move(self, terrorists_move, polices_move):
        for side in self._sides:
            moves = polices_move if side == 'Police' else terrorists_move

            for move in moves:
                canvas_pos = self._utils.get_canvas_position(move['agent_position'])
                # terrorist.angle = self.angle[EDirection.Left.name]
                self._canvas.edit_image(self._img_refs[side][move['agent_id']],
                                        canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True)

    def _update_board_on_bomb_cancel(self, bombs_planting):
        for bomb in bombs_planting:
            canvas_pos = self._utils.get_canvas_position(bomb['bomb_position'])
            board_cell = self._world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
            if board_cell == ECell.SmallBombSite:
                self._canvas.create_image('SmallBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.MediumBombSite:
                self._canvas.create_image('MediumBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.LargeBombSite:
                self._canvas.create_image('LargeBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.VastBombSite:
                self._canvas.create_image('VastBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)

    def _update_board_on_planting(self, bombs_planting):
        for bomb in bombs_planting:
            canvas_pos = self._utils.get_canvas_position(bomb['bomb_position'])
            board_cell = self._world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
            if board_cell == ECell.SmallBombSite:
                self._canvas.create_image('PlantingBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.MediumBombSite:
                self._canvas.create_image('PlantingBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.LargeBombSite:
                self._canvas.create_image('PlantingBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.VastBombSite:
                self._canvas.create_image('PlantingBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)

    def _update_board_on_planted(self, bombs_planted):
        for bomb in bombs_planted:
            canvas_pos = self._utils.get_canvas_position(bomb['bomb_position'])
            board_cell = self._world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
            if board_cell == ECell.SmallBombSite:
                self._canvas.create_image('PlantedBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.MediumBombSite:
                self._canvas.create_image('PlantedBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.LargeBombSite:
                self._canvas.create_image('PlantedBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.VastBombSite:
                self._canvas.create_image('PlantedBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)

    def _update_board_on_explode(self, bombs_exploded):
        for bomb in bombs_exploded:
            canvas_pos = self._utils.get_canvas_position(bomb['bomb_position'])
            board_cell = self._world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
            if board_cell == ECell.Empty:
                self._canvas.create_image('ExplodedBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            # elif board_cell == ECell.MediumBombSite:
            #     self._canvas.create_image('ExplodedBomb', canvas_pos['x'], canvas_pos['y'],
            #                               center_origin=True, scale_type=ScaleType.ScaleToWidth,
            #                               scale_value=self._cell_size)
            # elif board_cell == ECell.LargeBombSite:
            #     self._canvas.create_image('ExplodedBomb', canvas_pos['x'], canvas_pos['y'],
            #                               center_origin=True, scale_type=ScaleType.ScaleToWidth,
            #                               scale_value=self._cell_size)
            # elif board_cell == ECell.VastBombSite:
            #     self._canvas.create_image('ExplodedBomb', canvas_pos['x'], canvas_pos['y'],
            #                               center_origin=True, scale_type=ScaleType.ScaleToWidth,
            #                               scale_value=self._cell_size)

    def _update_board_on_defuse(self, bombs_defusing):
        for bomb in bombs_defusing:
            canvas_pos = self._utils.get_canvas_position(bomb['bomb_position'])
            board_cell = self._world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
            if board_cell == ECell.Empty:
                self._canvas.create_image('Empty', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.SmallBombSite:
                self._canvas.create_image('SmallBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.MediumBombSite:
                self._canvas.create_image('MediumBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.LargeBombSite:
                self._canvas.create_image('LargeBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.VastBombSite:
                self._canvas.create_image('VastBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)

    def _update_board_on_defusing(self, bombs_defusing):
        for bomb in bombs_defusing:
            canvas_pos = self._utils.get_canvas_position(bomb['bomb_position'])
            board_cell = self._world.board[bomb['bomb_position'].y][bomb['bomb_position'].x]
            if board_cell == ECell.SmallBombSite:
                self._canvas.create_image('DefusingBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.MediumBombSite:
                self._canvas.create_image('DefusingBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.LargeBombSite:
                self._canvas.create_image('DefusingBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)
            elif board_cell == ECell.VastBombSite:
                self._canvas.create_image('DefusingBomb', canvas_pos['x'], canvas_pos['y'],
                                          center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                          scale_value=self._cell_size)

    def _initialize_board(self, canvas):
        for y in range(self._world.height):
            for x in range(self._world.width):
                cell = self._world.board[y][x]
                canvas_pos = self._utils.get_canvas_position(Position(x=x, y=y), center_origin=False)

                # Draw non-player cells
                if cell == ECell.Empty:
                    canvas.create_image('Empty', canvas_pos['x'], canvas_pos['y'],
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self._cell_size)
                elif cell == ECell.Wall:
                    canvas.create_image('Wall', canvas_pos['x'], canvas_pos['y'],
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self._cell_size)
                elif cell == ECell.SmallBombSite:
                    self.small_bomb_ref = canvas.create_image('SmallBomb', canvas_pos['x'], canvas_pos['y'],
                                                              scale_type=ScaleType.ScaleToWidth,
                                                              scale_value=self._cell_size)
                elif cell == ECell.MediumBombSite:
                    self.medium_bomb_ref = canvas.create_image('MediumBomb', canvas_pos['x'], canvas_pos['y'],
                                                               scale_type=ScaleType.ScaleToWidth,
                                                               scale_value=self._cell_size)
                elif cell == ECell.LargeBombSite:
                    self.large_bomb_ref = canvas.create_image('LargeBomb', canvas_pos['x'], canvas_pos['y'],
                                                              scale_type=ScaleType.ScaleToWidth,
                                                              scale_value=self._cell_size)
                elif cell == ECell.VastBombSite:
                    self.vast_bomb_ref = canvas.create_image('VastBomb', canvas_pos['x'], canvas_pos['y'],
                                                             scale_type=ScaleType.ScaleToWidth,
                                                             scale_value=self._cell_size)

        # Draw Agents
        for side in self._sides:
            agents = self._world.polices if side == 'Police' else self._world.terrorists

            for agent in agents:
                position = agent.position

                canvas_pos = self._utils.get_canvas_position(agent.position)
                agent.angle = self.angle[EDirection.Left.name]
                agent.img_ref = canvas.create_image(side, canvas_pos['x'], canvas_pos['y'],
                                                    center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                                    scale_value=self._cell_size)
                self._img_refs[side][agent.id] = agent.img_ref

    def _initialize_fogs(self, canvas):
        for y in range(self._world.height):
            for x in range(self._world.width):
                cell = self._world.board[y][x]
                canvas_pos = self._utils.get_canvas_position(Position(x=x, y=y), center_origin=False)
                is_visible = False
                for side in self._sides:
                    for visible_cell_pos in self._world.visions[side]:
                        if visible_cell_pos.x == x and visible_cell_pos.y == y:
                            is_visible = True
                            break
                if not is_visible:
                    if cell != ECell.Wall:
                        new_fog_ref = canvas.create_image('Fog', canvas_pos['x'], canvas_pos['y'],
                                                      scale_type=ScaleType.ScaleToWidth,
                                                      scale_value=self._cell_size)
                        self._fog_refs.append(new_fog_ref)

    def _update_fogs(self):
        i = 0
        for y in range(self._world.height):
            for x in range(self._world.width):
                cell = self._world.board[y][x]
                canvas_pos = self._utils.get_canvas_position(Position(x=x, y=y), center_origin=False)
                is_visible = False
                for side in self._sides:
                    for visible_cell_pos in self._world.visions[side]:
                        if visible_cell_pos.x == x and visible_cell_pos.y == y:
                            is_visible = True
                            break
                if not is_visible:
                    if cell != ECell.Wall:
                        self._canvas.edit_image(self._fog_refs[i], canvas_pos['x'], canvas_pos['y'],
                                                      scale_type=ScaleType.ScaleToWidth,
                                                      scale_value=self._cell_size)
                        i += 1


class GuiUtils:

    def __init__(self, cell_size):
        self._cell_size = cell_size

    def get_canvas_position(self, position, center_origin=True):
        addition = int(self._cell_size / 2) if center_origin else 0
        return {
            'x': position.x * self._cell_size + addition,
            'y': position.y * self._cell_size + addition
        }

    def _get_line_xys(self, agent, curr_val, max_val, offset):
        canvas_pos = self.get_canvas_position(agent.position.x, agent.position.y)
        y1 = y2 = canvas_pos['y'] + int(self._cell_size / 2) - 10 + offset
        x1 = canvas_pos['x'] - int(self._cell_size / 2) + 5
        if curr_val == 0:
            x2 = x1
        else:
            x2 = x1 + math.ceil((self._cell_size - 10) * (curr_val / max_val))

        return x1, y1, x2, y2

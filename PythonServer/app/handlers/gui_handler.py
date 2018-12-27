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
        self._scale_factor = int((canvas.width - 1000) / (self._world.width * config['cell_size']))
        self._scale_percent = math.ceil(self._scale_factor * 100)
        self._cell_size = math.ceil(config['cell_size'] * self._scale_factor)
        self._font_size = int(self._cell_size / 2)
        self._utils = GuiUtils(self._cell_size)
        self._img_refs = {side: {} for side in self._sides}
        self.statusbar = []
        self._fog_refs = []
        self._img_refs = {side: {} for side in self._sides}
        self._dead_img_refs = {side: {} for side in self._sides}
        self._fog_refs = []


    def initialize(self):
        canvas = self._canvas
        config = self._config

        # Draw background
        # background_ref = canvas.create_image('Background', 0, 0)
        # canvas.edit_image(background_ref, scale_type=ScaleType.ScaleToWidth,
        #                   scale_value=canvas.width)

        self.angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }

        self._initialize_board(canvas)
        self._initialize_fogs(canvas)
        self._update_fogs()
        self._initialize_statusbar()

    def update(self, gui_events, statusbar):
        moving_terrorists, moving_polices, bombs_defusing, bombs_defused, bombs_op_canceled = [], [], [], [], []
        bombs_events = {"planting": [], "planted": [], "exploded": []}
        agents_dead = {"Terrorist": [], "Police": []}

        for event in gui_events:
            if event.type == GuiEventType.MovePolice:
                moving_polices.append(event.payload)
            if event.type == GuiEventType.MoveTerrorist:
                moving_terrorists.append(event.payload)
            if event.type == GuiEventType.DefusingBomb:
                bombs_defusing.append(event.payload)
            if event.type == GuiEventType.DefusedBomb:
                bombs_defused.append(event.payload)
            if event.type == GuiEventType.PlantingBomb:
                bombs_events['planting'].append(event.payload)
            if event.type == GuiEventType.PlantedBomb:
                bombs_events['planted'].append(event.payload)
            if event.type == GuiEventType.ExplodeBomb:
                bombs_events['exploded'].append(event.payload)
            if event.type == GuiEventType.CancelPlant:
                bombs_op_canceled.append(event.payload)
            if event.type == GuiEventType.CancelDefuse:
                bombs_op_canceled.append(event.payload)
            if event.type == GuiEventType.TerroristDeath:
                agents_dead["Terrorist"].append(event.payload)
            if event.type == GuiEventType.PoliceDeath:
                agents_dead["Police"].append(event.payload)

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

        if len(agents_dead["Terrorist"]) != 0:
            self._update_on_death_terrorist(agents_dead)

        if len(agents_dead["Police"]) != 0:
            self._update_on_death_police(agents_dead)

        self._update_statusbar(statusbar)
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

    def _update_statusbar(self, statusbar):

        self._canvas.edit_text(self.statusbar[0][1][0]['ref'], text=str(statusbar.police_score))

        self._canvas.edit_text(self.statusbar[0][1][2]['ref'], str(statusbar.terrorist_score))

        self._canvas.edit_text(self.statusbar[0][2][0]['ref'], str(statusbar.num_bombs_defused))

        self._canvas.edit_text(self.statusbar[0][2][2]['ref'], str(statusbar.num_bombs_exploded))

        self._canvas.edit_text(self.statusbar[1][1]['ref'], str(statusbar.remaining_cycles))

    def _initialize_statusbar(self):
        sides_status = [[[], [], []],
                        [[], [], []],
                        [[], [], []]]

        general_status = [[], [], [], []]

        self.statusbar.append(sides_status)
        self.statusbar.append(general_status)

        # side status
        for i_side_status in range(0, 3):
            for j_side_status in range(0, 3):
                self.statusbar[0][i_side_status][j_side_status] = {
                    "row": j_side_status,
                    "col": i_side_status,
                    "x": int(
                        (self._canvas.width - ((3 - i_side_status) * int(self._world.statusbar_width / 3))) / 3 - 600),
                    "y": int(((j_side_status * 250) + 0) / 1.5 + 2100),  # 10 is y0
                    "ref": None
                }

        for i_general_status in range(0, 2):
            self.statusbar[1][i_general_status] = {
                "row": 0,
                "col": i_general_status,
                "x": int(380),
                # int((self._canvas.width - (2 - i_general_status) * int(self._world.statusbar_width / 2))/3-60),
                "y": int(i_general_status * 340 + 2200)  # (600 + 0)/2 + 2000)
            }

        self.statusbar[0][0][0]['ref'] = self._canvas.create_image('PoliceLogo',
                                                                   self.statusbar[0][0][0]['y'],
                                                                   self.statusbar[0][0][0]['x'],
                                                                   center_origin=True,
                                                                   scale_type=ScaleType.ScaleToWidth,
                                                                   scale_value=self._cell_size)

        self.statusbar[0][0][1]['ref'] = self._canvas.create_text('vs.',
                                                                  self.statusbar[0][0][1]['y'],
                                                                  self.statusbar[0][0][1]['x'],
                                                                  self._canvas.make_rgba(0, 0, 0, 255),
                                                                  self._font_size * 2,
                                                                  center_origin=True)
        self.statusbar[0][0][2]['ref'] = self._canvas.create_image('TerroristLogo',
                                                                   self.statusbar[0][0][2]['y'],
                                                                   self.statusbar[0][0][2]['x'],
                                                                   center_origin=True,
                                                                   scale_type=ScaleType.ScaleToWidth,
                                                                   scale_value=self._cell_size)

        self.statusbar[0][1][0]['ref'] = self._canvas.create_text('0',
                                                                  self.statusbar[0][1][0]['y'],
                                                                  self.statusbar[0][1][0]['x'],
                                                                  self._canvas.make_rgba(0, 0, 0, 255),
                                                                  self._font_size * 2,
                                                                  center_origin=True)

        self.statusbar[0][1][1]['ref'] = self._canvas.create_text('score',
                                                                  self.statusbar[0][1][1]['y'],
                                                                  self.statusbar[0][1][1]['x'],
                                                                  self._canvas.make_rgba(0, 0, 0, 255),
                                                                  self._font_size * 2,
                                                                  center_origin=True)

        self.statusbar[0][1][2]['ref'] = self._canvas.create_text('0',
                                                                  self.statusbar[0][1][2]['y'],
                                                                  self.statusbar[0][1][2]['x'],
                                                                  self._canvas.make_rgba(0, 0, 0, 255),
                                                                  self._font_size * 2,
                                                                  center_origin=True)

        self.statusbar[0][2][0]['ref'] = self._canvas.create_text('0',
                                                                  self.statusbar[0][2][0]['y'],
                                                                  self.statusbar[0][2][0]['x'],
                                                                  self._canvas.make_rgba(0, 0, 0, 255),
                                                                  self._font_size * 2,
                                                                  center_origin=True)

        self.statusbar[0][2][1]['ref'] = self._canvas.create_text('bombs',
                                                                  self.statusbar[0][2][1]['y'],
                                                                  self.statusbar[0][2][1]['x'],
                                                                  self._canvas.make_rgba(0, 0, 0, 255),
                                                                  self._font_size * 2,
                                                                  center_origin=True)

        self.statusbar[0][2][2]['ref'] = self._canvas.create_text('0',
                                                                  self.statusbar[0][2][2]['y'],
                                                                  self.statusbar[0][2][2]['x'],
                                                                  self._canvas.make_rgba(0, 0, 0, 255),
                                                                  self._font_size * 2,
                                                                  center_origin=True)

        self.statusbar[1][0]['ref'] = self._canvas.create_text('remaining cycles:',
                                                               self.statusbar[1][0]['y'],
                                                               self.statusbar[1][0]['x'],
                                                               self._canvas.make_rgba(0, 0, 0, 255),
                                                               self._font_size * 2,
                                                               center_origin=True)

        self.statusbar[1][1]['ref'] = self._canvas.create_text(str(self._world.constants.max_cycles),
                                                               self.statusbar[1][1]['y'],
                                                               self.statusbar[1][1]['x'],
                                                               self._canvas.make_rgba(0, 0, 0, 255),
                                                               self._font_size * 2,
                                                               center_origin=True)

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
        for index in range(i, len(self._fog_refs)):
            self._canvas.edit_image(self._fog_refs[index], 5000, 5000,
                                    scale_type=ScaleType.ScaleToWidth,
                                    scale_value=self._cell_size)

    def _update_on_death_terrorist(self, dead_agents):
        # for side in dead_agents:
        for agent in dead_agents["Terrorist"]:
            canvas_pos = self._utils.get_canvas_position(agent['position'])

            self._canvas.edit_image(self._img_refs["Terrorist"][agent['terrorist_id']],
                                    6000, 6000,
                                    center_origin=True)
            self._canvas.edit_image(self._dead_img_refs["Terrorist"][agent['terrorist_id']],
                                    canvas_pos['x'], canvas_pos['y'],
                                    center_origin=True)

    def _update_on_death_police(self, dead_agents):
        # for side in dead_agents:
        for agent in dead_agents["Police"]:
            canvas_pos = self._utils.get_canvas_position(agent['position'])

            self._canvas.edit_image(self._img_refs["Police"][agent['police_id']],
                                    6000, 6000,
                                    center_origin=True)
            self._canvas.edit_image(self._dead_img_refs["Police"][agent['police_id']],
                                    canvas_pos['x'], canvas_pos['y'],
                                    center_origin=True)



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

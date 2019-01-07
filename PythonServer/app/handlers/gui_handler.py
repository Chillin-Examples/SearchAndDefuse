# -*- coding: utf-8 -*-

# python imports
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ..ks.commands import *
from ..ks.models import *
from ..gui_events import GuiEventType
from ..helpers.gui import fog, death, bomb


class GuiHandler:

    def __init__(self, world, sides, canvas, config):

        self.world = world
        self.sides = sides
        self.canvas = canvas
        self.config = config
        self.scale_factor = canvas.width / (self.world.width * config['cell_size'])
        self._scale_percent = math.ceil(self.scale_factor * 100)
        self.cell_size = math.ceil(config['cell_size'] * self.scale_factor)
        self.font_size = int(self.cell_size / 2)
        self.utils = GuiUtils(self.cell_size)
        self.img_refs = {side: {} for side in self.sides}
        self.dead_img_refs = {side: {} for side in self.sides}

        self.fog_refs = []

    def initialize(self):
        canvas = self.canvas
        config = self.config

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
        fog.initialize_fogs(self, canvas)
        fog.update_fogs(self)

    def update(self, gui_events):
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
                print(len(bombs_defusing))
            if event.type == GuiEventType.DefusedBomb:
                bombs_defused.append(event.payload)
            if event.type == GuiEventType.PlantingBomb:
                bombs_events['planting'].append(event.payload)
            if event.type == GuiEventType.PlantedBomb:
                bombs_events['planted'].append(event.payload)
            if event.type == GuiEventType.ExplodeBomb:
                bombs_events['exploded'].append(event.payload)
            if event.type in [GuiEventType.CancelPlant, GuiEventType.CancelDefuse]:
                bombs_op_canceled.append(event.payload)

            if event.type == GuiEventType.TerroristDeath:
                agents_dead["Terrorist"].append(event.payload)
            if event.type == GuiEventType.PoliceDeath:
                agents_dead["Police"].append(event.payload)

        if (len(moving_terrorists) != 0) or (len(moving_polices) != 0):
            self._update_board_on_move(moving_terrorists, moving_polices)

        if len(bombs_events['planting']) != 0:
            bomb.update_board_on_planting(self, bombs_events['planting'])

        if len(bombs_events['planted']) != 0:
            bomb.update_board_on_planted(self, bombs_events['planted'])

        if len(bombs_events['exploded']) != 0:
            bomb.update_board_on_explode(self, bombs_events['exploded'])

        if len(bombs_defusing) != 0:
            bomb.update_board_on_defusing(self, bombs_defusing)

        if len(bombs_defused) != 0:
            bomb.update_board_on_defuse(self, bombs_defused)

        if len(bombs_op_canceled) != 0:
            bomb.update_board_on_bomb_cancel(self, bombs_op_canceled)

        if len(agents_dead["Terrorist"]) != 0:
            death.update_on_death_terrorist(self, agents_dead)

        if len(agents_dead["Police"]) != 0:
            death.update_on_death_police(self, agents_dead)

        fog.update_fogs(self)

    def _update_board_on_move(self, terrorists_move, polices_move):
        for side in self.sides:
            moves = polices_move if side == 'Police' else terrorists_move
            for move in moves:
                canvas_pos = self.utils.get_canvas_position(move['agent_position'])
                # terrorist.angle = self.angle[EDirection.Left.name]
                self.canvas.edit_image(self.img_refs[side][move['agent_id']],
                                        canvas_pos['x'], canvas_pos['y'],
                                        center_origin=True)

    def _initialize_board(self, canvas):
        for y in range(self.world.height):
            for x in range(self.world.width):
                cell = self.world.board[y][x]
                canvas_pos = self.utils.get_canvas_position(Position(x=x, y=y), center_origin=False)

                # Draw non-player cells
                if cell == ECell.Empty:
                    canvas.create_image('Empty', canvas_pos['x'], canvas_pos['y'],
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
                elif cell == ECell.Wall:
                    canvas.create_image('Wall', canvas_pos['x'], canvas_pos['y'],
                                        scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
                elif cell == ECell.SmallBombSite:
                    self.small_bomb_ref = canvas.create_image('SmallBomb', canvas_pos['x'], canvas_pos['y'],
                                                              scale_type=ScaleType.ScaleToWidth,
                                                              scale_value=self.cell_size)
                elif cell == ECell.MediumBombSite:
                    self.medium_bomb_ref = canvas.create_image('MediumBomb', canvas_pos['x'], canvas_pos['y'],
                                                               scale_type=ScaleType.ScaleToWidth,
                                                               scale_value=self.cell_size)
                elif cell == ECell.LargeBombSite:
                    self.large_bomb_ref = canvas.create_image('LargeBomb', canvas_pos['x'], canvas_pos['y'],
                                                              scale_type=ScaleType.ScaleToWidth,
                                                              scale_value=self.cell_size)
                elif cell == ECell.VastBombSite:
                    self.vast_bomb_ref = canvas.create_image('VastBomb', canvas_pos['x'], canvas_pos['y'],
                                                             scale_type=ScaleType.ScaleToWidth,
                                                             scale_value=self.cell_size)

        # Draw Agents
        for side in self.sides:
            agents = self.world.polices if side == 'Police' else self.world.terrorists
            dead_img_name = 'DeadPolice' if side == 'Police' else 'DeadTerrorist'

            for agent in agents:
                position = agent.position

                canvas_pos = self.utils.get_canvas_position(agent.position)
                agent.angle = self.angle[EDirection.Left.name]
                agent.img_ref = canvas.create_image(side, canvas_pos['x'], canvas_pos['y'],
                                                    center_origin=True, scale_type=ScaleType.ScaleToWidth,
                                                    scale_value=self.cell_size)
                self.img_refs[side][agent.id] = agent.img_ref

                self.dead_img_refs[side][agent.id] = self.canvas.create_image(dead_img_name, 7000, 7000,
                                                                                scale_type=ScaleType.ScaleToWidth,
                                                                                scale_value=self.cell_size,
                                                                                center_origin=True)



class GuiUtils:

    def __init__(self, cell_size):
        self.cell_size = cell_size

    def get_canvas_position(self, position, center_origin=True):
        addition = int(self.cell_size / 2) if center_origin else 0
        return {
            'x': position.x * self.cell_size + addition,
            'y': position.y * self.cell_size + addition
        }

    def _get_line_xys(self, agent, curr_val, max_val, offset):
        canvas_pos = self.get_canvas_position(agent.position.x, agent.position.y)
        y1 = y2 = canvas_pos['y'] + int(self.cell_size / 2) - 10 + offset
        x1 = canvas_pos['x'] - int(self.cell_size / 2) + 5
        if curr_val == 0:
            x2 = x1
        else:
            x2 = x1 + math.ceil((self.cell_size - 10) * (curr_val / max_val))

        return x1, y1, x2, y2

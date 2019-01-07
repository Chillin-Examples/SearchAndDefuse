# -*- coding: utf-8 -*-

# python imports
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ..ks.commands import *
from ..gui_events import GuiEventType
from ..helpers.gui import fog, death, bomb, move, initializer, utils


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
        self.utils = utils.GuiUtils(self.cell_size)
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

        initializer.initialize_board(self, canvas)
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
            move.update_board_on_move(self, moving_terrorists, moving_polices)

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

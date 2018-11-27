# -*- coding: utf-8 -*-

# python imports
import math

# project imports
from ..ks.commands import *
from ..ks.models import *


class LogicHandler:

    def __init__(self, world, sides):
        self.last_gui_events = []
        self.world = world
        self._sides = sides
        self._last_cycle_commands = {'Police': [], 'Terrorist': []}

    def store_command(self, side_name, command):
        if command.id < 0 or command.id >= max(len(self.world.polices), len(self.world.terrorists)):
            print('Invalid id in command: %s %i' % (side_name, command.id))
            return

        print('command: %s(%i)' % (side_name, command.id))
        self._last_cycle_commands[side_name].append(command)


    def clear_commands(self):
        pass

    def initialize(self):
        self.move_dirs = {
            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }
        self.plant_dirs = {
            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }
        self.defuse_dirs = {
            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }
        self.directions = {'move_dir': self.move_dirs,
                           'plant_dir': self.plant_dirs,
                           'defuse_dir': self.defuse_dirs}

    def process(self, current_cycle):
        print(self._last_cycle_commands['Police'])
        gui_events = []
        for side in self._sides:
            for command in self._last_cycle_commands[side]:
                gui_events.append(self.world.apply_command(side, command, self.directions))
        self.last_gui_events = gui_events

    def get_client_world(self, side_name):
        return self.world

    def _check_end_game(self):
        pass

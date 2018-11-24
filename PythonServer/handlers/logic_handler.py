# -*- coding: utf-8 -*-

# python imports
import math

# project imports
import sys
sys.path.append('../')
from ks.commands import *
from ks.models import *


class LogicHandler:

    def __init__(self, world, sides):
        self.world = world
        self.sides = sides

    def store_command(self, side_name, command):
        pass

    def clear_commands(self):
        pass

    def initialize(self, canvas, config):

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


    def process(self, current_cycle):
        pass

    def get_client_world(self, side_name):
        pass

    def _check_end_game(self):
        pass

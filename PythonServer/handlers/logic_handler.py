# -*- coding: utf-8 -*-

# python imports
import math

# project imports
import sys
sys.path.append('../')
from ks.commands import *
from ks.models import *


class LogicHandler:

    def __init__(self, world, sides, board):
        self.world = world
        self.sides = sides
        self.char_board = board

    def store_command(self, side_name, command):
        pass

    def clear_commands(self):
        pass

    def initialize(self, canvas, config):
        # Create World board
        for y in range(self.world.height):
            for x in range(self.world.width):
                if self.char_board[y][x] == 'w':  # Wall
                    self.world.board[y][x] = ECell.Wall
                elif self.char_board[y][x] == 's':  # Small Bomb
                    self.world.board[y][x] = ECell.SmallBombSite
                elif self.char_board[y][x] == 'l':  # Large Bomb
                    self.world.board[y][x] = ECell.LargeBombSite
                elif self.char_board[y][x] == 'm':  # Medium Bomb
                    self.world.board[y][x] = ECell.MediumBombSite
                elif self.char_board[y][x] == 'v':  # Vast Bomb
                    self.world.board[y][x] = ECell.VastBombSite
                elif self.char_board[y][x] == 'e':  # Empty
                    self.world.board[y][x] = ECell.Empty

        # Create Polices and Terrorists
        for side in self.sides:
            for player in self.world.map_config['player'][side]:
                player_position = Position(x=player['position'][0], y=player['position'][1])
                if side == 'Police':
                    new_police = Police()
                    new_police.id = len(self.world.polices)
                    new_police.position = player_position
                    new_police.defusion_remaining_time = -1  # self.world.constants.bomb_defusing_time
                    new_police.footstep_sounds = []
                    new_police.bomb_sounds = []
                    new_police.is_visible = False
                    self.world.polices.append(new_police)
                if side == 'Terrorist':
                    new_terrorist = Terrorist()
                    new_terrorist.id = len(self.world.terrorists)
                    new_terrorist.position = player_position
                    new_terrorist.planting_remaining_time = self.world.constants["bomb_planting_time"]
                    new_terrorist.footstep_sounds = []
                    new_terrorist.is_dead = False
                    self.world.terrorists.append(new_terrorist)

        # Status Bar Not Initialized Yet.

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

    def check_end_game(self):
        pass

from ..ks.commands import *
from ..ks.models import *
import math


class LogicHandler:
    world = None
    board = []
    sides = []
    move_dirs=None
    move_angle=None
    plant_dirs=None
    plant_angle=None
    defuse_dirs=None
    defuse_angle=None


    def __init__(self, world, sides, board):
        self.world = world
        self.sides = sides
        self.board = board

    def store_command(self, side_name, command):
        pass

    def clear_commands(self):
        pass

    def initialize(self):
        # Create World board
        for y in range(self.world.height):
            for x in range(self.world.width):
                if self.board[y][x] == 'w':  # Wall
                    self.world.board[y][x] = ECell.Wall
                elif self.board[y][x] == 's':  # Small Bomb
                    self.world.board[y][x] = ECell.SmallBombSite
                elif self.board[y][x] == 'l':  # Large Bomb
                    self.world.board[y][x] = ECell.LargeBombSite
                elif self.board[y][x] == 'm':  # Medium Bomb
                    self.world.board[y][x] = ECell.MediumBombSite
                elif self.board[y][x] == 'v':  # Vast Bomb
                    self.world.board[y][x] = ECell.VastBombSite
                elif self.board[y][x] == 'e':  # Empty
                    self.world.board[y][x] = ECell.Empty

        # Create Polices and Terrorists
        for side in self.sides:
            for player in self.world.map_config['player'][side]:
                if side == 'Police':
                    new_police = Police()
                    new_police.id = len(self.world.polices[side])
                    new_police.position = player['position']
                    new_police.defusion_remaining_time = -1  # self.world.constants.bomb_defusing_time
                    new_police.footstep_sounds = []
                    new_police.bomb_sounds = []
                    new_police.is_visible = False
                    self.world.polices[side].append(new_police)
                if side == 'Terrorist':
                    new_terrorist = Terrorist()
                    new_terrorist.id = len(self.world.terrorists[side])
                    new_terrorist.position = player['position']
                    new_terrorist.planting_remaining_time = self.world.constants.bomb_planting_time
                    new_terrorist.footstep_sounds = []
                    new_terrorist.is_dead = False
                    self.world.terrorists[side].append(new_terrorist)

        # Status Bar Not Initialized Yet.

        # Initialize Commands
        self.move_dirs = {

            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }
        self.move_angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }

        self.plant_dirs = {

            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }
        self.plant_angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }

        self.defuse_dirs = {

            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }
        self.defuse_angle = {
            ECommandDirection.Up.name: -90,
            ECommandDirection.Right.name: 180,
            ECommandDirection.Down.name: 90,
            ECommandDirection.Left.name: 0
        }

        return self.move_dirs, self.move_angle, self.plant_dirs, self.plant_angle, \
               self.defuse_dirs, self.defuse_angle

    def process(self, current_cycle):
        pass

    def get_client_world(self, side_name):
        pass

    def check_end_game(self):
        pass

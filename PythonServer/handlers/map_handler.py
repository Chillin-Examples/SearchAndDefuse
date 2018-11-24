# -*- coding: utf-8 -*-

# python imports
import json

# project imports
# from ..ks.models import World, ECell
import sys
sys.path.append('../')
from ks.models import World, ECell, Constants

GLOBAL_BOARD_WIDTH = 0
GLOBAL_BOARD_HEIGHT = 0


class MapHandler:

    def __init__(self, sides):
        self._sides = sides

    def _fill_board(self, board, width, height, char_board):
        # Create World board
        for y in range(height):
            for x in range(width):
                if char_board[y][x] == 'w':  # Wall
                    board[y][x] = ECell.Wall
                elif char_board[y][x] == 's':  # Small Bomb
                    board[y][x] = ECell.SmallBombSite
                elif char_board[y][x] == 'l':  # Large Bomb
                    board[y][x] = ECell.LargeBombSite
                elif char_board[y][x] == 'm':  # Medium Bomb
                    board[y][x] = ECell.MediumBombSite
                elif char_board[y][x] == 'v':  # Vast Bomb
                    board[y][x] = ECell.VastBombSite
                elif char_board[y][x] == 'e':  # Empty
                    board[y][x] = ECell.Empty


    def load_map(self, config):
        map_config = json.loads(open((config['map']), "r").read())
        char_board = map_config['char_board']

        world = World()
        world.width = len(char_board[0])
        world.height = len(char_board)
        world.map_config = map_config
        world.config = config
        world.scores = {side: 0 for side in self._sides}
        world.bombs = []
        world.polices = []
        world.terrorists = []
        world.constants = Constants()
        world.constants.bomb_planting_time = map_config["constants"]["bomb_planting_time"]
        world.constants.bomb_defusion_time = map_config["constants"]["bomb_defusion_time"]
        world.constants.bomb_explosion_time = map_config["constants"]["bomb_explosion_time"]
        world.constants.bomb_planting_score = map_config["constants"]["bomb_planting_score"]
        world.constants.bomb_defusion_score = map_config["constants"]["bomb_defusion_score"]
        world.constants.bomb_explosion_score = map_config["constants"]["bomb_explosion_score"]
        world.constants.score_coefficient_small_bomb_site = map_config["constants"]["score_coefficient_small_bomb_site"]
        world.constants.score_coefficient_medium_bomb_site = map_config["constants"]["score_coefficient_medium_bomb_site"]
        world.constants.score_coefficient_large_bomb_site = map_config["constants"]["score_coefficient_large_bomb_site"]
        world.constants.score_coefficient_vast_bomb_site = map_config["constants"]["score_coefficient_vast_bomb_site"]
        world.constants.terrorist_vision_distance = map_config["constants"]["terrorist_vision_distance"]
        world.constants.terrorist_death_score = map_config["constants"]["terrorist_death_score"]
        world.constants.police_vision_distance = map_config["constants"]["police_vision_distance"]
        world.constants.max_cycles = map_config["constants"]["max_cycles"]
        world.board = [[ECell.Empty for _ in range(world.width)] for _ in range(world.height)]
        self._fill_board(world.board, world.width, world.height, char_board)


        return world

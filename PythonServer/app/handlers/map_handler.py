# -*- coding: utf-8 -*-

# python imports
import json

# project imports
from ..ks.models import *
from ..helpers import test



class MapHandler:

    def __init__(self, sides):
        self._sides = sides

    def _fill_board(self, world, char_board):
        # Init World Board
        world.board = [[ECell.Empty for _ in range(world.width)] for _ in range(world.height)]

        # Create World board
        for y in range(world.height):
            for x in range(world.width):
                if char_board[y][x] == 'w':  # Wall
                    world.board[y][x] = ECell.Wall
                elif char_board[y][x] == 's':  # Small Bomb
                    world.board[y][x] = ECell.SmallBombSite
                elif char_board[y][x] == 'l':  # Large Bomb
                    world.board[y][x] = ECell.LargeBombSite
                elif char_board[y][x] == 'm':  # Medium Bomb
                    world.board[y][x] = ECell.MediumBombSite
                elif char_board[y][x] == 'v':  # Vast Bomb
                    world.board[y][x] = ECell.VastBombSite
                elif char_board[y][x] == 'e':  # Empty
                    world.board[y][x] = ECell.Empty

    def _fill_constants(self, world, constants_config):
        world.constants = Constants()
        world.constants.bomb_planting_time = constants_config["bomb_planting_time"]
        world.constants.bomb_defusion_time = constants_config["bomb_defusion_time"]
        world.constants.bomb_explosion_time = constants_config["bomb_explosion_time"]
        world.constants.bomb_planting_score = constants_config["bomb_planting_score"]
        world.constants.bomb_defusion_score = constants_config["bomb_defusion_score"]
        world.constants.bomb_explosion_score = constants_config["bomb_explosion_score"]
        world.constants.score_coefficient_small_bomb_site = constants_config["score_coefficient_small_bomb_site"]
        world.constants.score_coefficient_medium_bomb_site = constants_config["score_coefficient_medium_bomb_site"]
        world.constants.score_coefficient_large_bomb_site = constants_config["score_coefficient_large_bomb_site"]
        world.constants.score_coefficient_vast_bomb_site = constants_config["score_coefficient_vast_bomb_site"]
        world.constants.terrorist_vision_distance = constants_config["terrorist_vision_distance"]
        world.constants.terrorist_death_score = constants_config["terrorist_death_score"]
        world.constants.police_vision_distance = constants_config["police_vision_distance"]
        world.constants.max_cycles = constants_config["max_cycles"]

    def _create_players(self, world, player_config):
        world.polices = []
        world.terrorists = []

        # Create Polices and Terrorists
        for side in self._sides:
            for player in player_config[side]:
                player_position = Position(x=player['position'][0], y=player['position'][1])
                if side == 'Police':
                    new_police = Police()
                    new_police.id = len(world.polices)
                    new_police.position = player_position
                    new_police.defusion_remaining_time = -1
                    new_police.footstep_sounds = []
                    new_police.bomb_sounds = []
                    new_police.is_visible = False
                    world.polices.append(new_police)
                if side == 'Terrorist':
                    new_terrorist = Terrorist()
                    new_terrorist.id = len(world.terrorists)
                    new_terrorist.position = player_position
                    new_terrorist.planting_remaining_time = -1
                    new_terrorist.footstep_sounds = []
                    new_terrorist.is_dead = False
                    world.terrorists.append(new_terrorist)

    def load_map(self, config):
        map_config = json.loads(open((config['map']), "r").read())
        char_board = map_config['char_board']
        constants_config = map_config['constants']
        player_config = map_config['player']

        world = World()
        world.width = len(char_board[0])
        world.height = len(char_board)
        world.scores = {side: 0 for side in self._sides}
        world.bombs = []
        self._fill_board(world, char_board)
        self._fill_constants(world, constants_config)
        self._create_players(world, player_config)
        test.plant_bomb_manually(Position(x=3, y=5), world)

        return world

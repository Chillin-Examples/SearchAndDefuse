import json

from .ks.models import World

GLOBAL_BOARD_WIDTH = 0
GLOBAL_BOARD_HEIGHT = 0

class MapHandler:
    BOARD_WIDTH = 0
    BOARD_HEIGHT = 0

    sides = []
    def __init__(self, sides):
        self.sides = sides

    def load_map(self, constants, map_config, config):
        self.initialize_constants(constants)
        self.map_config = json.loads(open((config['map']), "r").read())
        board = self.map_config['board']
        self.BOARD_WIDTH = len(board[0])
        self.BOARD_HEIGHT = len(board)
        world = World()
        world.width = self.BOARD_WIDTH
        world.height = self.BOARD_HEIGHT
        world.constants = constants
        world.scores = {side: 0 for side in self.sides}
        world.bombs = {side: [] for side in self.sides}
        world.polices = {side: [] for side in self.sides}
        world.terrorists = {side: [] for side in self.sides}
        world.enter_score = map_config['enter_score']
        # world.players = map_config['player']
        world.map_config = map_config
        world.config = config
        powerup_emmiters = []  # powerup emitters position


        GLOBAL_BOARD_WIDTH = self.BOARD_WIDTH
        GLOBAL_BOARD_HEIGHT = self.BOARD_HEIGHT

        return world, board

    def initialize_constants(self, constants):
        constants.initialize(7, 10, 15, 2, 1, 2, 2.5, 5, 7.5, 10, 5, 4, 6, 100)


from ..handlers import map_handler

class Pos(object):
    x = 0
    y = 0
    position = 0

    def __init__(self, x=None, y=None, position=None):
        if position is not None:
            self.position = position
            self._position_to_xy()
        else:
            self.x = x
            self.y = y
            self._xy_to_position()


    def _position_to_xy(self):
        self.x = self.position % map_handler.GLOBAL_BOARD_WIDTH
        self.y = self.position // map_handler.GLOBAL_BOARD_WIDTH


    def _xy_to_position(self):
        self.position = (self.y * map_handler.GLOBAL_BOARD_WIDTH) + self.x


    def __add__(self, other):
        return Pos(x=self.x + other.x, y=self.y + other.y)


# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


def is_equal(self, position):
    if self.y == position.y and self.x == position.x:
        return True
    return False


def __eq__(self, position):
    return self.is_equal(position)


def add(self, position):
    x = self.x + position.x
    y = self.y + position.y
    return Position(x=x, y=y)


def __add__(self, position):
    return self.add(position)


# def get_neighbours(self):
#     return [Position(x=self.x-1, y=self.y), Position(x=self.x+1, y=self.y),
#             Position(x=self.x, y=self.y-1), Position(x=self.x, y=self.y+1)]


Position.is_equal = is_equal
Position.__eq__ = __eq__
Position.add = add
Position.__add__ = __add__
# Position.get_neighbours = get_neighbours

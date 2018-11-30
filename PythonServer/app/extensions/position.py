# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


def is_equal(self, another_position):
    if self.y == another_position.y and self.x == another_position.x:
        return True
    return False


def __eq__(self, another_position):
    return self.is_equal(another_position)


def add(self, another_position):
    # Bug Potential :)
    x = self.x + another_position.x
    y = self.y + another_position.y
    return Position(x=x, y=y)


Position.is_equal = is_equal
Position.__eq__ = __eq__
Position.add = add

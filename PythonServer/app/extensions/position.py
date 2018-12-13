# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


def is_equal(self, position):
    return self.x == position.x and self.y == position.y


def __eq__(self, position):
    return self.is_equal(position)


def add(self, position):
    return Position(
        x=self.x + position.x,
        y=self.y + position.y
    )


def __add__(self, position):
    return self.add(position)


Position.is_equal = is_equal
Position.__eq__ = __eq__
Position.add = add
Position.__add__ = __add__

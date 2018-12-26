# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


def is_equal(self, position):
    return self.y == position.y and self.x == position.x


def __eq__(self, position):
    return self.is_equal(position)


def add(self, position):
    return Position(
        x=self.x + position.x,
        y=self.y + position.y
    )


def __add__(self, position):
    return self.add(position)


def get_neighbours(self):
    return [Position(x=self.x - 1, y=self.y), Position(x=self.x + 1, y=self.y),
            Position(x=self.x, y=self.y - 1), Position(x=self.x, y=self.y + 1)]


def is_neighbour(self, position):
    return any(self.position == neighbour for neighbour in get_neighbours(position))


Position.is_equal = is_equal
Position.__eq__ = __eq__
Position.add = add
Position.__add__ = __add__
Position.get_neighbours = get_neighbours

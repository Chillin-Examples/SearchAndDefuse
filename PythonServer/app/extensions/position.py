# -*- coding: utf-8 -*-

# python imports
import math

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
    return any(self == neighbour for neighbour in get_neighbours(position))


def angle_between(self, position):
    return math.degrees(math.atan2(self.y - position.y, self.x - position.x))


def add_vector(self, vector_angle, vector_length):
    radians = math.radians(vector_angle)

    return Position(
        x = self.x + math.cos(radians) * vector_length,
        y = self.y + math.sin(radians) * vector_length
    )


Position.is_equal = is_equal
Position.__eq__ = __eq__
Position.add = add
Position.__add__ = __add__
Position.get_neighbours = get_neighbours
Position.is_neighbour = is_neighbour
Position.angle_between = angle_between
Position.add_vector = add_vector

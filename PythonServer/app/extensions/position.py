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


def get_neighbours(self, world):
    neighbours = [Position(x=self.x - 1, y=self.y), Position(x=self.x + 1, y=self.y),
                  Position(x=self.x, y=self.y - 1), Position(x=self.x, y=self.y + 1)]
    valid_neighbours = []
    for neighbour in neighbours:
        if 0 <= neighbour.x < world.width and 0 <= neighbour.y < world.height:
            valid_neighbours.append(neighbour)
    return valid_neighbours


def is_neighbour(self, position, world):
    return any(self == neighbour for neighbour in position.get_neighbours(world))


def angle_between(self, position):
    return math.degrees(math.atan2(self.y - position.y, self.x - position.x))


def add_vector(self, vector_angle, vector_length):
    radians = math.radians(vector_angle)

    return Position(
        x = self.x + math.cos(radians) * vector_length,
        y = self.y + math.sin(radians) * vector_length
    )


def __repr__(self):
    return 'Position: {}, {}'.format(self.x, self.y)


Position.is_equal = is_equal
Position.__eq__ = __eq__
Position.add = add
Position.__add__ = __add__
Position.get_neighbours = get_neighbours
Position.is_neighbour = is_neighbour
Position.angle_between = angle_between
Position.add_vector = add_vector
Position.__repr__ = __repr__

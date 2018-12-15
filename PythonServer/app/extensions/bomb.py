# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Bomb


def is_equal(self, bomb):
    return sorted(self.__dict__.items()) == sorted(bomb.__dict__.items())


def __eq__(self, bomb):
    return self.is_equal(bomb)


Bomb.is_equal = is_equal
Bomb.__eq__ = __eq__

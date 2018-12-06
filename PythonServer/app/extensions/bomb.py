# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Bomb


def is_equal(self, bomb):
    return cmp(self.__dict__, bomb.__dict__) == 0


def __eq__(self, bomb):
    return self.is_equal(bomb)


Bomb.is_equal = is_equal
Bomb.__eq__ = __eq__

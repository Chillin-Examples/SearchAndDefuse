# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Bomb


def is_equal(self, bomb):
    if self.position == bomb.position and self.explosion_remaining_time == position.explosion_remaining_time:
        if self.planter_id == bomb.planter_id and self.defuser_id == bomb.defuser_id:
            return True
    return False


def __eq__(self, bomb):
    return self.is_equal(bomb)


Bomb.is_equal = is_equal
Bomb.__eq__ = __eq__

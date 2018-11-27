# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position


def is_equal(self, position):
    if self.y == position.y and self.x == position.x:
        return True
    return False


Position.is_equal = is_equal

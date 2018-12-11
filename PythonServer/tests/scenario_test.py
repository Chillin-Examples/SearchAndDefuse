# -*- coding: utf-8 -*-

# project imports
from ..app.ks.models import Bomb


def plant_bomb_manually(position, world):
    new_test_bomb = Bomb(position=position)
    world.bombs.append(new_test_bomb)

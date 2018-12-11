# -*- coding: utf-8 -*-

# project imports
from ..app.ks.models import Bomb


def plant_bomb_manually(position, world):
    new_test_bomb = Bomb(position=position,
                         explosion_remaining_time=world.constants.bomb_explosion_time,
                         planter_id=-1, defuser_id=None)

    world.bombs.append(new_test_bomb)

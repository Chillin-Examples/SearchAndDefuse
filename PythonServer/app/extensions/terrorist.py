# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist
from ..ks.commands import Move, PlantBomb
from .agent import move


def plant_bomb(self, world, command):
    # defuser_id should be -1 at first.
    return True


Terrorist.defuse_bomb = plant_bomb
Terrorist.move = move

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist
from ..ks.commands import Move, PlantBomb
from .agent import move


def plant_bomb(self, world, command):
    return True


Terrorist.defuse_bomb = plant_bomb
Terrorist.move = move

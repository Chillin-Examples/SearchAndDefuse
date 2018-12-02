# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist, Bomb, Constants
from ..ks.commands import Move, PlantBomb
from .agent import move, directions


def plant_bomb(self, world, command):
    bomb_position = self.position.add(directions[command.direction.name])
    world.bombs.append(Bomb(position=bomb_position, explosion_remaining_time=world.constants.bomb_planting_time))


Terrorist.plant_bomb = plant_bomb
Terrorist.move = move

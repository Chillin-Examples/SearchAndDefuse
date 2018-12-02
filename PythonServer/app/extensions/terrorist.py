# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist, Bomb, Constants
from ..ks.commands import Move, PlantBomb
from .agent import move, directions


def plant_bomb(self, world, command):
    bomb_position = self.position.add(directions[command.direction.name])
    world.bombs.append(Bomb(position=bomb_position, explosion_remaining_time=world.constants.bomb_planting_time))
    # I'm not sure about this yet. If it doesn't work, we should:
    # 1. pass the bomb list instead of world to the function
    # 2. return the updated list and in the world.py file,
    #    write this: self.bombs = plant_bomb(bombs_list, command)


Terrorist.plant_bomb = plant_bomb
Terrorist.move = move

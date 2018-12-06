# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist, Bomb
from .agent import move, directions


def plant_bomb(self, world, command):
    bomb_position = self.position.add(directions[command.direction.name])
    new_bomb = Bomb(position=bomb_position, explosion_remaining_time=world.constants.bomb_explosion_time,
                    planter_id=self.id, defuser_id=None)

    # check replanting condition
    world.bombs[:] = [bomb for bomb in world.bombs if bomb != new_bomb]
    world.bombs.append(new_bomb)

    # for bomb in world.bombs:
    #     if new_bomb == bomb:
    #         del world.bombs[bomb]
    #         break
    # world.bombs.append(new_bomb)


Terrorist.plant_bomb = plant_bomb
Terrorist.move = move

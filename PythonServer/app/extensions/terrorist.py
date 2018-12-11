# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist, Bomb
from .agent import move, directions


def plant_bomb(self, world, command):
    bomb_position = self.position.add(directions[command.direction.name])

    new_bomb = Bomb(position=bomb_position, explosion_remaining_time=-1,
                    planter_id=self.id, defuser_id=None)

    # check replanting condition
    for bomb in world.bombs:
        if bomb == new_bomb:
            world.bombs.remove(bomb)
            self.planting_remaining_time = world.constants.bomb_planting_time
            break

    world.bombs.append(new_bomb)


def cancel_plant(self, bombs):
    for bomb in bombs:
        if bomb.planter_id == self.id and bomb.position.is_neighbor(self.position):
            self.bombs.remove(bomb)
            self.planting_remaining_time = -1


Terrorist.plant_bomb = plant_bomb
Terrorist.move = move
Terrorist.cancel_plant = cancel_plant

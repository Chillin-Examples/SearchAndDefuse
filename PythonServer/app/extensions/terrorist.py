# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist, Bomb
from .agent import directions, move as base_move


def move(self, world, command):
    if self.planting_remaining_time != -1:
        self.cancel_plant(self, world)
    base_move(self, world, command)


def plant_bomb(self, world, command):
    if self.planting_remaining_time != -1:
        self.cancel_plant(world)

    bomb_position = self.position + directions[command.direction.name]
    new_bomb = Bomb(position=bomb_position, explosion_remaining_time=-1,
                    planter_id=self.id, defuser_id=None)
    world.bombs.append(new_bomb)


def cancel_plant(self, world):
    bomb = next((bomb for bomb in world.bombs if bomb.planter_id == self.id))
    self.bombs.remove(bomb)
    self.planting_remaining_time = -1


Terrorist.plant_bomb = plant_bomb
Terrorist.move = move
Terrorist.cancel_plant = cancel_plant

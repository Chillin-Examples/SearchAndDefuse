# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist, Bomb, ECell
from .agent import directions, can_move as base_can_move, move as base_move


def move(self, world, command):
    if self.planting_remaining_time != -1:
        self.cancel_plant(self, world)
    base_move(self, world, command)


def plant_bomb(self, world, command):
    if self.planting_remaining_time != -1:
        self.cancel_plant(world)

    bomb_position = self.position + directions[command.direction.name]
    new_bomb = Bomb(position=bomb_position, explosion_remaining_time=-1,
                    planter_id=self.id, defuser_id=-1)
    world.bombs.append(new_bomb)


def cancel_plant(self, world):
    bomb = next((bomb for bomb in world.bombs if bomb.planter_id == self.id))
    bomb_position = bomb.position
    world.bombs.remove(bomb)
    self.planting_remaining_time = -1
    return bomb_position


def can_plant_bomb(self, world, command):
    new_bomb_position = self.position.add(directions[command.direction.name])

    # If it's not a bombsite return false
    if world.board[new_bomb_position.y][new_bomb_position.x] not in [ECell.SmallBombSite, ECell.MediumBombSite,
                                                                     ECell.LargeBombSite, ECell.VastBombSite]:
        return False

    # If it already has a bomb with different planter
    for planted_bomb in world.bombs:
        if planted_bomb.position == new_bomb_position and planted_bomb.planter_id != self.id:
            return False

        # if bomb is exploding
        if planted_bomb.position == new_bomb_position and planted_bomb.explosion_remaining_time != -1:
            return False

    # Otherwise return True!
    return True


Terrorist.plant_bomb = plant_bomb
Terrorist.move = move
Terrorist.cancel_plant = cancel_plant
Terrorist.can_plant_bomb = can_plant_bomb
Terrorist.can_move = base_can_move

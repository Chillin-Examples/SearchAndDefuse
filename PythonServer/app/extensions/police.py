# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Police
from .agent import directions, can_move as base_can_move, move as base_move


def move(self, world, command):
    if self.defusion_remaining_time != -1:
        self.cancel_defuse(self, world)
    base_move(self, world, command)


def defuse_bomb(self, world, command):
    if self.defusion_remaining_time != -1:
        self.cancel_defuse(world)

    bomb_position = self.position + directions[command.direction.name]
    for bomb in world.bombs:
        if bomb.position == bomb_position:
            bomb.defuser_id = self.id
            break


def cancel_defuse(self, world):
    bomb = next((bomb for bomb in world.bombs if bomb.defuser_id == self.id))
    bomb.defuser_id = -1
    self.defusion_remaining_time = -1
    print('cancel shod')


def can_defuse_bomb(self, world, command):
    planted_position = self.position.add(directions[command.direction.name])

    for planted_bomb in world.bombs:

        # no police is defusing at the moment
        if planted_bomb.defuser_id == -1 or planted_bomb.defuser_id == self.id:
            # bomb exists and is exploding
            if planted_bomb.position == planted_position and planted_bomb.explosion_remaining_time != -1:
                return True

    # Otherwise return False!
    return False


Police.defuse_bomb = defuse_bomb
Police.move = move
Police.cancel_defuse = cancel_defuse
Police.can_defuse_bomb = can_defuse_bomb
Police.can_move = base_can_move

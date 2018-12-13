# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Police
from .agent import directions, move as base_move


def move(self, world, command):
    if self.defusion_remaining_time != -1:
        self.cancel_defuse(self, world)
    base_move(self, world, command)


def defuse_bomb(self, world, command):
    if self.defusion_remaining_time != -1:
        self.cancel_defuse(world)

    bomb_position = self.position.add(directions[command.direction.name])
    for bomb in world.bombs:
        if bomb.position == bomb_position:
            bomb.defuser_id = self.id
            break


def cancel_defuse(self):
    self.defusion_remaining_time = -1


Police.defuse_bomb = defuse_bomb
Police.move = move
Police.cancel_defuse = cancel_defuse

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Police, Bomb
from .agent import move, directions


def defuse_bomb(self, world, command):
    bomb_position = self.position.add(directions[command.direction.name])
    world.bombs.remove(Bomb(position=bomb_position, explosion_remaining_time=world.constants.bomb_explosion_time))


Police.defuse_bomb = defuse_bomb
Police.move = move

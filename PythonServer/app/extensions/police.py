# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Police
from ..ks.commands import Move, DefuseBomb
from .agent import move


def change_direction(self, world, command):
    # start
    return True


def defuse_bomb(self, world, command):
    return True


Police.change_direction = change_direction
Police.defuse_bomb = defuse_bomb
Police.move = move
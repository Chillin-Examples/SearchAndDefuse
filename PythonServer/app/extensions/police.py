# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Police
from ..ks.commands import Move, DefuseBomb
from .agent import move


def defuse_bomb(self, world, command):
    return True


Police.defuse_bomb = defuse_bomb
Police.move = move

from ..ks.models import Police
from ..ks.commands import Move,DefuseBomb

def change_direction(self, world, command):
    #start
    return True


def defuse_bomb(self, world, command):
    return True


Police.change_direction = change_direction
Police.defuse_bomb = defuse_bomb

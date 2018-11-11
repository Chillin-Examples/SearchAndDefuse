from ..ks.models import Police
from ..ks.commands import Move,DefuseBomb

def change_direction(self, world, command):
    return True


def defuse_bomb(self, world, command):
    pass


Police.validate_command = change_direction
Police.apply_command = defuse_bomb

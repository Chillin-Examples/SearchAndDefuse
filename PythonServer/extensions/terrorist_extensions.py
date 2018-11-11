from ..ks.models import Terrorist
from ..ks.commands import Move,PlantBomb

def change_direction(self, world, command):
    return True


def plant_bomb(self, world, command):
    return True


Terrorist.change_direction = change_direction
Terrorist.defuse_bomb = plant_bomb()

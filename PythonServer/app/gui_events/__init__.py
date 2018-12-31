# -*- coding: utf-8 -*-

# python imports
from enum import Enum


class GuiEventType(Enum):
    MovePolice = 0
    MoveTerrorist = 1
    PlantingBomb = 2
    PlantedBomb = 3
    DefusingBomb = 4
    DefusedBomb = 5
    ExplodeBomb = 6
    TerroristDeath = 7
    PoliceDeath = 8
    CancelPlant = 9
    CancelDefuse = 10


class GuiEvent(object):

    def __init__(self, type, **kwargs):
        self.type = type
        self.payload = kwargs

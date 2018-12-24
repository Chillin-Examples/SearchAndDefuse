# -*- coding: utf-8 -*-

# python imports
from enum import Enum


class GuiEventType(Enum):
    MovePolice = 0
    MoveTerrorist = 1
    ChangePoliceDirection = 2
    ChangeTerroristDirection = 3
    PlantingBomb = 4
    PlantedBomb = 5
    DefusingBomb = 6
    DefusedBomb = 7
    ExplodeBomb = 8
    TerroristDeath = 9
    PoliceDeath = 9
    CancelBombOp = 11


class GuiEvent(object):

    def __init__(self, type, **kwargs):
        self.type = type
        self.payload = kwargs

# -*- coding: utf-8 -*-

# python imports
from enum import Enum


class GuiEventType(Enum):
    MovePolice = 0
    MoveTerrorist = 1
    ChangePoliceDirection = 2
    ChangeTerroristDirection = 3
    PlantBomb = 4
    DefuseBomb = 5
    ExplodeBomb = 6
    TerroristDeath = 7
    ChangePolicesStatus = 8
    ChangeTerroristsStatus = 9
    ChangeBombTimer = 12


class GuiEvent(object):

    def __init__(self, type, **kwargs):
        self.type = type
        self.payload = kwargs

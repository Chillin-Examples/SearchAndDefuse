# -*- coding: utf-8 -*-

# python imports
from enum import Enum


class GuiEventType(Enum):
    move_police = 0
    move_terrorist = 1
    change_police_direction = 2
    change_terrorist_direction = 3
    plant_bomb = 4
    defuse_bomb = 5
    explode_bomb = 6
    terrorist_death = 7
    change_polices_status = 8
    change_terrorists_status = 9
    change_police_intensity_border = 10
    change_terrorist_intensity_border = 11
    change_bomb_timer = 12


class GuiEvent(object):

    def __init__(self, type):
        self.type = type

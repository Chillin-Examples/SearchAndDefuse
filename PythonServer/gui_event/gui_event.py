from enum import Enum


class GuiEventType(Enum):
    Move_Police = 0
    Move_Terrorist = 1
    Change_Police_Direction = 2
    Change_Terrorist_Direction = 3
    Plant_Bomb = 4
    Defuse_Bomb = 5
    Explode_Bomb=6
    Death_Terrorist=7
    Change_Polices_Status=8
    Change_Terrorists_Status=9
    Change_Police_Intensity_Border=10
    Change_Terrorist_Intensity_Border=11
    Change_Bomb_Timer=12





class GuiEvent:
    type = GuiEventType
    extra_properties = {}

    def __init__(self, type):
        self.type = type

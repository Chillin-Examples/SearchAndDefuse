# -*- coding: utf-8 -*-

# chillin imports
from chillin_client import TurnbasedAI

# project imports
from ks.models import (World, Police, Terrorist, Bomb, Position, Constants,
                       ESoundIntensity, EDirection, ECell)
from ks.commands import DefuseBomb, PlantBomb, Move, ECommandDirection


class AI(TurnbasedAI):

    def __init__(self, world):
        super(AI, self).__init__(world)


    def initialize(self):
        print('initialize')


    def decide(self):
        print('decide')

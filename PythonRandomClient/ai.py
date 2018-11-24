# -*- coding: utf-8 -*-

# python imports
import random

# chillin imports
from chillin_client import RealtimeAI

# project imports
from ks.models import (World, Police, Terrorist, Bomb, Position, Constants,
                       ESoundIntensity, EDirection, ECell)
from ks.commands import DefuseBomb, PlantBomb, Move, ECommandDirection


class AI(RealtimeAI):

    def __init__(self, world):
        super(AI, self).__init__(world)


    def initialize(self):
        print('initialize')


    def decide(self):
        print('decide')

        if self.my_side == 'Police':
            police_id = 0
            direction = random.choice([
                ECommandDirection.Up,
                ECommandDirection.Right,
                ECommandDirection.Down,
                ECommandDirection.Left
            ])
            self.send_command(Move(id=police_id, direction=direction))
        elif self.my_side == 'Terrorist':
            terrorist_id = 0
            direction = random.choice([
                ECommandDirection.Up,
                ECommandDirection.Right,
                ECommandDirection.Down,
                ECommandDirection.Left
            ])
            self.send_command(Move(id=terrorist_id, direction=direction))

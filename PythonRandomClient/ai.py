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
        self.done = False

    def initialize(self):
        print('initialize')

    def decide(self):
        print('decide')
        # if self.my_side == 'Police':
        #     direction = ECommandDirection.Down
        #     for i in range(0, 4):
        #         self.send_command(Move(id=i, direction=direction))

        if self.my_side == 'Police':
            direction = ECommandDirection.Down
            # for i in range(0, 4):
            if not self.done:
                self.send_command(DefuseBomb(id=2, direction=direction))
                self.done = True
            # if self.current_cycle == 4:
            #     direction = ECommandDirection.Down
            #     self.send_command(DefuseBomb(id=2, direction=direction))
            if self.current_cycle >= 2:
                direction = ECommandDirection.Down
                self.send_command(Move(id=2, direction=direction))

            # if self.current_cycle % 4 == 0 and self.current_cycle != 0:
            #     direction = ECommandDirection.Up
            #     self.send_command(Move(id=2, direction=direction))

        elif self.my_side == 'Terrorist':
            direction = ECommandDirection.Down
            # for i in range(0, 5):
            if not self.done:
                self.send_command(PlantBomb(id=2, direction=direction))
                self.done = True
            if self.current_cycle % 4 == 0 and self.current_cycle != 0:
                direction = ECommandDirection.Down
                self.send_command(Move(id=2, direction=direction))

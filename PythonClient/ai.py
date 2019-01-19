# -*- coding: utf-8 -*-

# python imports
import random

# chillin imports
from chillin_client import RealtimeAI

# project imports
from ks.models import (World, Police, Terrorist, Bomb, Position, Constants,
                       ESoundIntensity, ECell)
from ks.commands import DefuseBomb, PlantBomb, Move, ECommandDirection


class AI(RealtimeAI):

    def __init__(self, world):
        super(AI, self).__init__(world)
        self.done = False

    def initialize(self):
        print('initialize')

    def decide(self):
        print('decide')
        my_agents = self.world.polices if self.my_side == 'Police' else self.world.terrorists
        for agent in my_agents:
            direction = random.choice([
                ECommandDirection.Up,
                ECommandDirection.Right,
                ECommandDirection.Down,
                ECommandDirection.Left
            ])
            self.send_command(Move(id=agent.id, direction=direction))

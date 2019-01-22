# -*- coding: utf-8 -*-

# python imports
import random
from copy import deepcopy

# chillin imports
from chillin_client import RealtimeAI

# project imports
from ks.models import (World, Police, Terrorist, Bomb, Position, Constants,
                       ESoundIntensity, ECell, EAgentStatus)
from ks.commands import DefuseBomb, PlantBomb, Move, ECommandDirection


class AI(RealtimeAI):

    def __init__(self, world):
        super(AI, self).__init__(world)
        self.done = False

    def initialize(self):
        print('initialize')
        self._directions = [
            ECommandDirection.Up,
            ECommandDirection.Right,
            ECommandDirection.Down,
            ECommandDirection.Left,
        ]

        self._dir_to_pos = {
            ECommandDirection.Up:    (+0, -1),
            ECommandDirection.Right: (+1, +0),
            ECommandDirection.Down:  (+0, +1),
            ECommandDirection.Left:  (-1, +0),
        }

        self._bombsites_ecell = [
            ECell.SmallBombSite,
            ECell.MediumBombSite,
            ECell.LargeBombSite,
            ECell.VastBombSite,
        ]


    def decide(self):
        print('decide')
        my_agents = self.world.polices if self.my_side == 'Police' else self.world.terrorists

        for agent in my_agents:
            if agent.status == EAgentStatus.Dead:
                continue

            doing_bomb_operation = agent.defusion_remaining_time != -1 if self.my_side == 'Police' else agent.planting_remaining_time != -1

            if doing_bomb_operation:
                self._agent_print(agent.id, 'Continue Bomb Operation')
                continue

            bombsite_direction = self._find_bombsite_direction(agent)
            if bombsite_direction == None:
                self._agent_print(agent.id, 'Random Move')
                self.send_command(Move(id=agent.id, direction=random.choice(self._directions)))
            else:
                self._agent_print(agent.id, 'Start Bomb Operation')
                if self.my_side == 'Police':
                    self.send_command(DefuseBomb(id=agent.id, direction=bombsite_direction))
                else:
                    self.send_command(PlantBomb(id=agent.id, direction=bombsite_direction))


    def _find_bombsite_direction(self, agent):
        for direction in self._directions:
            pos = self._sum_pos_tuples((agent.position.x, agent.position.y), self._dir_to_pos[direction])
            if self.world.board[pos[1]][pos[0]] in self._bombsites_ecell:
                has_bomb = self._has_bomb(pos)
                if (self.my_side == 'Police' and has_bomb) or (self.my_side == 'Terrorist' and not has_bomb):
                    return direction
        return None


    def _has_bomb(self, position):
        for bomb in self.world.bombs:
            if position[0] == bomb.position.x and position[1] == bomb.position.y:
                return True
        return False


    def _sum_pos_tuples(self, t1, t2):
        return (t1[0] + t2[0], t1[1] + t2[1])


    def _agent_print(self, agent_id, text):
        print('Agent[{}]: {}'.format(agent_id, text))

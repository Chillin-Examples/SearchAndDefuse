# -*- coding: utf-8 -*-

# project imports
from ..helpers import score


class Timer(object):

    def __init__(self, world):
        self.world = world


class BombTimer(Timer):

    def __init__(self, world):
        super().__init__(world)

    def update_bombsites_timings(self, world):
        self.world = world

        for bombsite in self.world.bombs:
                # if the bomb is planted in this cycle.
                if self.world.terrorists[bombsite.planter_id].remaining_planting_time == -1:
                    self._update_plant_timer_on_plant(bombsite.planter_id)
                else:
                    # 1. check bombs that are waiting to be planted
                    # 2. check bombs that are already planted
                    # if the planting timer is not zero yet, keep planting
                    if self.world.terrorist[bombsite.planter_id].remaining_planting_time > 0:
                        self.world.terrorist[bombsite.planter_id].remaining_planting_time -= 1
                    else:
                        score.increase_score('plant', world, bombsite.position)
                        self._update_plant_timer_on_cycle(bombsite)

    def _update_plant_timer_on_plant(self, agent_id):
        self.world.terrorists[agent_id].planting_remaining_time = self.world.constants.bomb_planting_time

    def _update_plant_timer_on_cycle(self, bomb):

        # if it explodes
        if bomb.explosion_remaining_time <= 0:
            bomb_position = bomb.position
            score.increase_score('explode', self.world, bomb.position)
            del self.world.bombs[bomb]
            return "bomb_exploded", bomb_position

        # bomb is not exploded yet
        else:
            bomb.explosion_remaining_time -= 1

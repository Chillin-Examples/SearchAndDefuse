# -*- coding: utf-8 -*-
import queue


class Timer(object):

    def __init__(self, world):
        self._world = world


class BombTimer(Timer):

    def __init__(self, world):
        super().__init__(world)

    def update_bombsites_timings(self, world):
        self._world = world
        terrorists = self._world.terrorists

        # for defuse
        polices = self._world.polices

        for bombsite in self._world.bombs:
            for terrorist in terrorists:
                # if the bomb is planted in this cycle.
                if self._world.terrorists[terrorist.id].remaining_planting_time == -1:
                    self._update_plant_timer_on_plant(terrorist.id)
                else:
                    # 1. check bombs that are waiting to be planted
                    # 2. check bombs that are already planted
                    self._update_plant_timer_on_cycle(bombsite, terrorist.id)

    def _update_plant_timer_on_plant(self, agent_id):
        self._world.terrorists[agent_id].planting_remaining_time = self._world.constants.bomb_planting_time

    def _update_plant_timer_on_cycle(self, bomb, terrorist_id):
        # if the planting timer is not zero yet, keep planting
        if self._world.terrorist[terrorist_id].remaining_planting_time > 0:
            self._world.terrorist[terrorist_id].remaining_planting_time -= 1
            return "planting_the_bomb", None

        # if it explodes
        elif bomb.planter_id == terrorist_id:
            if bomb.explosion_remaining_time <= 0:
                bomb_position = bomb.position
                del self._world.bombs[bomb]
                return "bomb_exploded", bomb_position

            # bomb is not exploded yet
            else:
                bomb.explosion_remaining_time -= 1

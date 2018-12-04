# -*- coding: utf-8 -*-
import queue


class Timer(object):

    def __init__(self, world):
        self._world = world


class GameTimer(Timer):

    def __init__(self, world):
        super().__init__(world)
        self._max_cycles = self._world.constants.max_cycles

    def reached_max_cycles(self, current_cycle_number):
        if self._max_cycles <= current_cycle_number:
            return True


class BombTimer(Timer):

    def __init__(self, world):
        super().__init__(world)
        self._bombs_timers = {bomb.position: {} for bomb in world.bombs}

    def update_bombsites_timings(self, bombs_queue):
        for map_bombs in bombs_queue:
            # if the bomb is planned in this cycle.
            if map_bombs not in self._bombs_timers:
                self._update_planting_timer_on_plant(map_bombs)
            else:
                # 1. check bombs that are waiting to be planted
                # 2. check bombs that are already planted
                self._update_planting_timer_on_cycle(map_bombs)

    def _update_planted_timer_on_plant(self, bombsite_position):
        self._bombs_timers[bombsite_position]['remaining_planting_time'] = self._world.constants.bomb_planting_time
        self._bombs_timers[bombsite_position]['remaining_defusion_time'] = -1
        self._bombs_timers[bombsite_position]['remaining_explosion_time'] = -1

    def _update_planted_timer_on_cycle(self, bombsite_position):
        # if the planting timer is not zero yet, keep planting
        if self._bombs_timers[bombsite_position]['remaining_planting_time'] != 0:
            self._bombs_timers[bombsite_position]['remaining_planting_time'] -= 1
            return "planting_the_bomb", None

        else:
            # if the planting timer is zero, plant the bomb
            if self._bombs_timers[bombsite_position]['remaining_explosion_time'] == -1:
                self._bombs_timers[bombsite_position]['remaining_explosion_time'] = self._world.constants.bomb_explosion_time
                return "bomb_planted", bombsite_position

            # keep counting until the bomb explodes
            else:
                self._bombs_timers[bombsite_position]['remaining_explosion_time'] -= 1

            # if it explodes
            if self._bombs_timers[bombsite_position]['remaining_explosion_time'] == 0:
                del self._bombs_timers[bombsite_position]
                return "bomb_exploded", bombsite_position

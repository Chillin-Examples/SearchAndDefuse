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

        for bombsite in self._bombs_timers:
            bombsite[
                'remaining_planting_time'] = world.constants.bomb_planting_time  # this property is for terrorists model in models.ks
            bombsite['remaining_defusion_time'] = -1  # this property is for polices model in models.ks
            bombsite['remaining_explosion_time'] = -1  # this property is for bomb model in models.ks

        self.planting_queue = queue.Queue()
        self.defusion_queue = queue.Queue()

    def update_bombsites_timings(self, active_bombs):
        for active_bomb in active_bombs:
            # if the bomb is planned in this cycle.
            if active_bomb not in self._bombs_timers:
                self._update_bombs_timer_on_plant(active_bomb)

            else:
                # 1. check bombs that are waiting to be planted
                # 2. check bombs that are already planted
                self._update_bombs_timer_on_cycle(active_bomb)

    def _update_bombs_timer_on_plant(self, bombsite_position):
        self._bombs_timers[bombsite_position]['remaining_planting_time'] = self._world.constants.bomb_planting_time

    def _update_bombs_timer_on_cycle(self, bombsite_position):
        # if the planting timer is not zero yet, keep planting
        if self._bombs_timers[bombsite_position]['remaining_planting_time'] != 0:
            self._bombs_timers[bombsite_position]['remaining_planting_time'] -= 1
        else:
            # if the planting timer is zero, plant the bomb
            if self._bombs_timers[bombsite_position]['remaining_explosion_time'] == -1:
                self._bombs_timers[bombsite_position]['remaining_explosion_time'] = self._world.constants.bomb_explosion_time

            # keep counting until the bomb explodes
            else:
                self._bombs_timers[bombsite_position]['remaining_explosion_time'] -= 1

            # if it explodes
            if self._bombs_timers[bombsite_position]['remaining_explosion_time'] == 0:
                # EXPLODE :D
                pass

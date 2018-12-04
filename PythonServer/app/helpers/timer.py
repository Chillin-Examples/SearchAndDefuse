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
        self.bombs_timers = {bomb.position: {} for bomb in world.bombs}

        for bombsite in self.bombs_timers:
            bombsite['remaining_planting_time'] = world.constants.bomb_planting_time # this property is for terrorists model in models.ks
            bombsite['remaining_defusion_time'] = world.constants.bomb_defusion_time # this property is for polices model in models.ks
            bombsite['remaining_explosion_time'] = world.constants.bomb_explosion_time # this property is for bomb model in models.ks

        self.planting_queue = queue.Queue()
        self.defusion_queue = queue.Queue()

    def update_bombsites_timings(self, active_bombs):
        for bombsite in self.bombs_timers:
            for active_bomb in active_bombs:
                # updating the timers for bombs that are already planted
                if bombsite == active_bomb:
                    pass

                # setting timers for bombs that are being planted in this cycle
                else:
                    pass


    def _update_timer_on_plant(self, bombsite):
        # self.bombs_timers[bombsite][]


# -*- coding: utf-8 -*-


class Timer(object):

    def __init(self, world):
        self._world = world


class GameTimer(Timer):

    def __init__(self):
        self._max_cycles = self._world.constants.max_cycles

    def reached_max_cycles(self, current_cycle_number):
        if self._max_cycles <= current_cycle_number:
            return True


class BombTimer(Timer):

    def __init__(self, world):
        self.bombs_timers = {bomb.position: {} for bomb in world.bombs}

        for bombsite in self.bombs_timers:
            bombsite['remaining_planting_time'] = world.constants.bomb_planting_time
            bombsite['remaining_defusion_time'] = world.constants.bomb_defusion_time
            bombsite['remaining_explosion_time'] = world.constants.bomb_explosion_time

    # def check_bombsites(self, bombs):
    #     for bombsite in self.bombs_timers:
    #         pass



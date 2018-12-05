# -*- coding: utf-8 -*-
import queue


class Timer(object):

    def __init__(self, world):
        self._world = world


class BombTimer(Timer):

    def __init__(self, world):
        super().__init__(world)

    def update_bombsites_timings(self, world, agent_id):
        for bombsite in world.bombs:
            # if the bomb is planted in this cycle.
            if world.terrorists[agent_id].remaining_planting_time == -1:
                self._update_plant_timer_on_plant(agent_id, world)
            else:
                # 1. check bombs that are waiting to be planted
                # 2. check bombs that are already planted
                self._update_plant_timer_on_cycle(bombsite, world, agent_id)

    def _update_plant_timer_on_plant(self, agent_id, world):
        world.terrorists[agent_id].planting_remaining_time = world.constants.bomb_planting_time

    def _update_plant_timer_on_cycle(self, bomb, world, terrorist_id):
        # if the planting timer is not zero yet, keep planting
        if world.terrorist[terrorist_id].remaining_planting_time > 0:
            world.terrorist[terrorist_id].remaining_planting_time -= 1
            return "planting_the_bomb", None

        # if it explodes
        elif bomb.explosion_remaining_time <= 0:
            bomb_position = bomb.position
            del world.bombs[bomb]
            return "bomb_exploded", bomb_position

        # bomb is not exploded yet
        else:
            bomb.explosion_remaining_time -= 1

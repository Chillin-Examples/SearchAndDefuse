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
                # bomb has been planted in this cycle.
                if self.world.terrorists[bombsite.planter_id].remaining_planting_time == -1:
                    self._update_plant_timer_on_plant(bombsite.planter_id)
                else:

                    # planting timer is not zero yet,terrorist should keep planting
                    if self.world.terrorist[bombsite.planter_id].remaining_planting_time > 0:

                        # if terrorist has not moved since commanding plant.
                        if self.world.terrorists[bombsite.planter_id] in bombsite.get_neighbours():
                            self.world.terrorist[bombsite.planter_id].remaining_planting_time -= 1
                        else:

                            # command should be canceled.
                            self.world.terrorist[bombsite.planter_id].remaining_planting_time = -1
                            del self.world.bombs[bombsite]
                    else:
                        # TODO return planted bomb position for gui
                        score.increase_score('plant', world, bombsite.position)

                        # check bombs that are already planted
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

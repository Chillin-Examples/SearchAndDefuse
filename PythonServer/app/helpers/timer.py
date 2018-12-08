# -*- coding: utf-8 -*-

# project imports
from ..helpers import score
from ..gui_events import GuiEvent, GuiEventType


class Timer(object):

    def __init__(self, world):
        self.world = world


class BombTimer(Timer):

    def __init__(self, world):
        super().__init__(world)

    def update_bombsites_timings(self, world):
        self.world = world

        for bomb in self.world.bombs:
                # bomb has been planted in this cycle.
                if self.world.terrorists[bomb.planter_id].planting_remaining_time == -1:
                    self._update_plant_timer_on_plant(bomb.planter_id)
                    return []
                else:

                    # planting timer is not zero yet,terrorist should keep planting
                    if self.world.terrorists[bomb.planter_id].planting_remaining_time > 0:
                        self.world.terrorists[bomb.planter_id].planting_remaining_time -= 1
                        return []
                    else:
                        return self._update_plant_timer_on_cycle(bomb)

    def _update_plant_timer_on_plant(self, agent_id):
        self.world.terrorists[agent_id].planting_remaining_time = self.world.constants.bomb_planting_time

    def _update_plant_timer_on_cycle(self, bomb):

        # when bomb starts the timer to explode
        if bomb.explosion_remaining_time == -1:
            score.increase_score('plant', self.world, bomb.position)
            return [GuiEvent(GuiEventType.PlantedBomb, bomb_position=bomb.position)] # show timer on gui later

        # when bomb explodes
        elif bomb.explosion_remaining_time == 0:
            bomb_position = bomb.position
            score.increase_score('explode', self.world, bomb.position)
            self.world.bombs.remove(bomb)
            return [GuiEvent(GuiEventType.ExplodeBomb, bomb_position=bomb_position)]

        # bomb is not exploded yet
        else:
            bomb.explosion_remaining_time -= 1
            return []

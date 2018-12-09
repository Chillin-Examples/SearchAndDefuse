# -*- coding: utf-8 -*-

# project imports
from ..helpers import score
from ..gui_events import GuiEvent, GuiEventType
from ..ks.models import ECell


class BombTimer(object):

    def update_plant_timings(self, world):

        for bomb in world.bombs:
            # bomb has been planted in this cycle.
            if world.terrorists[bomb.planter_id].planting_remaining_time == -1:
                print("terrorist {} commanded plant.".format(bomb.planter_id))
                self._update_plant_timer_on_plant(bomb.planter_id, world)
                return []
            else:

                # planting timer is not zero yet,terrorist should keep planting
                if world.terrorists[bomb.planter_id].planting_remaining_time > 0:
                    print("terrorist {} is planting.".format(bomb.planter_id))
                    world.terrorists[bomb.planter_id].planting_remaining_time -= 1
                    print("B")
                    return []
                else:
                    return self._update_plant_timer_on_cycle(bomb, world)
        return []

    def _update_plant_timer_on_plant(self, agent_id, world):
        world.terrorists[agent_id].planting_remaining_time = world.constants.bomb_planting_time

    def _update_plant_timer_on_cycle(self, bomb, world):

        # when bomb starts the timer to explode
        if bomb.explosion_remaining_time == -1:
            bomb.explosion_remaining_time = world.constants.bomb_explosion_time
            score.increase_score('plant', world, bomb.position)
            return [GuiEvent(GuiEventType.PlantedBomb, bomb_position=bomb.position)] # show timer on gui later

        # when bomb explodes
        elif bomb.explosion_remaining_time == 0:
            bomb_position = bomb.position
            score.increase_score('explode', world, bomb.position)
            world.board[bomb_position.y][bomb_position.x] = ECell.ExplodedBombSite
            world.bombs.remove(bomb)
            return [GuiEvent(GuiEventType.ExplodeBomb, bomb_position=bomb_position)]

        # bomb is not exploded yet
        else:
            bomb.explosion_remaining_time -= 1
            return []

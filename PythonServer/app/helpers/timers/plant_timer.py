# -*- coding: utf-8 -*-

# project imports
from .. import score
from ...gui_events import GuiEvent, GuiEventType
from ...ks.models import *


# TODO exploded bombsite should not be planted by terrorists. ->>>>> RESOLVED :]
# TODO when all bombs are exploded game should end. ->>>>> RESOLVED :]
def update_plant_timings(world):

    for bomb in world.bombs:
        if bomb.planter_id != -1:
            # bomb has been planted in this cycle.
            if world.terrorists[bomb.planter_id].planting_remaining_time == -1:
                print("Terrorist {} commanded plant.".format(bomb.planter_id))
                _update_plant_timer_on_plant(bomb.planter_id, world)
                return []
            else:

                # planting timer is not zero yet,terrorist should keep planting
                if world.terrorists[bomb.planter_id].planting_remaining_time > 0:
                    print("Terrorist {} is planting.".format(bomb.planter_id))
                    world.terrorists[bomb.planter_id].planting_remaining_time -= 1
                    return []
                else:
                    return _update_plant_timer_on_cycle(bomb, world)
    return []


def _update_plant_timer_on_plant(agent_id, world):
    world.terrorists[agent_id].planting_remaining_time = world.constants.bomb_planting_time


def _update_plant_timer_on_cycle(bomb, world):

    # when bomb starts the timer to explode
    if bomb.explosion_remaining_time == -1:
        print('Bomb planted.')
        bomb.explosion_remaining_time = world.constants.bomb_explosion_time
        score.increase_score('plant', world, bomb.position)
        return [GuiEvent(GuiEventType.PlantedBomb, bomb_position=bomb.position)] # show timer on gui later

    # when bomb explodes
    elif bomb.explosion_remaining_time == 0:
        print('Bomb exploded.')
        bomb_position = bomb.position
        score.increase_score('explode', world, bomb.position)
        world.bombs.remove(bomb)
        world.board[bomb_position.y][bomb_position.x] = ECell.Empty
        return [GuiEvent(GuiEventType.ExplodeBomb, bomb_position=bomb_position)]

    # bomb is not exploded yet
    else:
        print('Bomb is exploding...')
        bomb.explosion_remaining_time -= 1
        return []

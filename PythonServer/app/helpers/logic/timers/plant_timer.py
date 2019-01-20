# -*- coding: utf-8 -*-

# project imports
from .. import score
from ....gui_events import GuiEvent, GuiEventType
from ....ks.models import *


def update_plant_timings(world):
    plant_events = []
    bombs_to_remove = []

    for bomb in world.bombs:
        if bomb.planter_id != -1:
            is_bomb_planted = True

            # planting timer is not zero yet, terrorist should keep planting
            if bomb.explosion_remaining_time == -1 and world.terrorists[bomb.planter_id].planting_remaining_time > 0:
                print("Terrorist {} is planting.".format(bomb.planter_id))
                world.terrorists[bomb.planter_id].planting_remaining_time -= 1
                if world.terrorists[bomb.planter_id].planting_remaining_time > 0:
                    is_bomb_planted = False

            if is_bomb_planted:
                new_plant_events, remove_bomb = _update_plant_timer_on_cycle(bomb, world)
                plant_events += new_plant_events
                if remove_bomb:
                    bombs_to_remove.append(bomb)

    for bomb in bombs_to_remove:
        world.bombs.remove(bomb)

    return plant_events


def _update_plant_timer_on_cycle(bomb, world):

    # when bomb starts the timer to explode
    if bomb.explosion_remaining_time == -1:
        # reset plant remaining time
        world.terrorists[bomb.planter_id].planting_remaining_time = -1
        print('Bomb planted.')
        bomb.explosion_remaining_time = world.constants.bomb_explosion_time
        score.increase_plant_score(world, bomb.position)
        return [GuiEvent(GuiEventType.PlantedBomb, bomb=bomb)], False
    else:
        bomb.explosion_remaining_time -= 1

    if bomb.explosion_remaining_time > 0:
        print('Bomb is exploding...')
        return [], False

    # when bomb explodes
    explosion_events = []
    print('Bomb exploded.')
    bomb_position = bomb.position
    score.increase_explode_bomb_score(world, bomb.position)
    world.board[bomb_position.y][bomb_position.x] = ECell.Empty
    explosion_events.append(GuiEvent(GuiEventType.ExplodeBomb, bomb=bomb))

    # eliminate nearby agents
    for terrorist in world.terrorists:
        if terrorist.status == EAgentStatus.Alive and bomb.position.is_neighbour(terrorist.position):
            terrorist.status = EAgentStatus.Dead
            explosion_events.append(GuiEvent(GuiEventType.TerroristDeath,
                                                terrorist_id=terrorist.id, position=terrorist.position))
    for police in world.polices:
        if police.status == EAgentStatus.Alive and bomb.position.is_neighbour(police.position):
            police.status = EAgentStatus.Dead
            explosion_events.append(GuiEvent(GuiEventType.PoliceDeath,
                                                police_id=police.id, position=police.position))
            score.increase_eliminate_police_score(world)

    return explosion_events, True

# -*- coding: utf-8 -*-

# project imports
from .. import score
from ....gui_events import GuiEvent, GuiEventType
from ....ks.models import *


def update_plant_timings(world, statusbar):

    for bomb in world.bombs:
        if bomb.planter_id != -1:

            # bomb has been planted in this cycle and is not exploding.
            if world.terrorists[bomb.planter_id].planting_remaining_time == -1 and bomb.explosion_remaining_time == -1:
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
                    return _update_plant_timer_on_cycle(bomb, world, statusbar)
    return []


def _update_plant_timer_on_plant(agent_id, world):
    world.terrorists[agent_id].planting_remaining_time = world.constants.bomb_planting_time


def _update_plant_timer_on_cycle(bomb, world, statusbar):

    # when bomb starts the timer to explode
    if bomb.explosion_remaining_time == -1:

        # reset plant remaining time
        world.terrorists[bomb.planter_id].planting_remaining_time = -1
        print('Bomb planted.')
        bomb.explosion_remaining_time = world.constants.bomb_explosion_time
        score.increase_plant_score(world, bomb.position)
        return [GuiEvent(GuiEventType.PlantedBomb, bomb_position=bomb.position)]  # show timer on gui later

    # when bomb explodes
    elif bomb.explosion_remaining_time == 0:
        explosion_events = []
        print('Bomb exploded.')
        bomb_position = bomb.position
        score.increase_explode_bomb_score(world, bomb.position)
        world.bombs.remove(bomb)
        statusbar.update_exploded_number()
        world.board[bomb_position.y][bomb_position.x] = ECell.Empty
        explosion_events.append(GuiEvent(GuiEventType.ExplodeBomb, bomb_position=bomb_position))

        # eliminate nearby agents
        for terrorist in world.terrorists:
            if terrorist.status == AgentStatus.Alive and bomb.position.is_neighbour(terrorist.position):
                terrorist.status = AgentStatus.Dead
                explosion_events.append(GuiEvent(GuiEventType.TerroristDeath,
                                                 terrorist_id=terrorist.id, position=terrorist.position))
        for police in world.polices:
            if police.status == AgentStatus.Alive and bomb.position.is_neighbour(police.position):
                police.status = AgentStatus.Dead
                explosion_events.append(GuiEvent(GuiEventType.PoliceDeath,
                                                 police_id=police.id, position=police.position))
                score.increase_eliminate_police_score(world)

        return explosion_events

    # bomb is not exploded yet
    else:
        print('Bomb is exploding...')
        bomb.explosion_remaining_time -= 1
        return []

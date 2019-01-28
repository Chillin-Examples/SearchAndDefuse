# -*- coding: utf-8 -*-

# project imports
from ...ks.models import *
from .dls import dls


def _compute_agents_visions(world, side):
    agents = world.polices if side == 'Police' else world.terrorists
    vision_distance = world.constants.police_vision_distance if side == 'Police' else world.constants.terrorist_vision_distance

    vision_positions = []
    for agent in agents:
        if agent.status == EAgentStatus.Alive:
            doing_bomb_operation = agent.defusion_remaining_time != -1 if side == 'Police' else agent.planting_remaining_time != -1
            if doing_bomb_operation:
                if side == 'Police':
                    bomb = next((bomb for bomb in world.bombs if bomb.defuser_id == agent.id))
                else:
                    bomb = next((bomb for bomb in world.bombs if bomb.planter_id == agent.id
                                 and bomb.explosion_remaining_time == -1))

                agent.visions = [Position(x=agent.position.x, y=agent.position.y),
                                 Position(bomb.position.x, bomb.position.y)]
            else:
                _, agent.visions = dls(world, agent.position, vision_distance, None)

            vision_positions += agent.visions

    return _join_visions(vision_positions)


# computes all polices visions and converts them into one list.
def compute_polices_visions(world):
    return _compute_agents_visions(world, 'Police')


# computes all terrorists visions and converts them into one list.
def compute_terrorists_visions(world):
    return _compute_agents_visions(world, 'Terrorist')


# removes duplicates
def _join_visions(vision_positions):
    final_list = []
    for position in vision_positions:
        if any(position == new_pos for new_pos in final_list):
            continue
        else:
            final_list.append(position)
    return final_list

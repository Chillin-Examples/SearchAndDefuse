# -*- coding: utf-8 -*-

# project imports
from . import utils
from ....ks.models import EAgentStatus


def update_police_bomb_sounds(world):
    for police in world.polices:
        police.bomb_sounds = []
        if police.status == EAgentStatus.Alive:
            distances = []
            for bomb in world.bombs:
                if bomb.explosion_remaining_time != -1:
                    distances.append(int(utils.calculate_distance(world, bomb.position, police.position)))

            police.bomb_sounds = utils.distances_to_intensities(distances, world.constants.sound_ranges)

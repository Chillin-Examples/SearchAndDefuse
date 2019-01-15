# -*- coding: utf-8 -*-

# project imports
from . import utils


def update_police_bomb_sounds(world):
    _empty_polices_bomb_sound_list(world.polices)

    for bomb in world.bombs:
        for police in world.polices:
            distance = utils.calculate_distance(bomb.position, police.position)
            value = int(distance)
            police.bomb_sounds.append(utils.int_to_intensity(value, world.constants.sound_ranges))


def _empty_polices_bomb_sound_list(polices):
    for police in polices:
        police.bomb_sounds = []

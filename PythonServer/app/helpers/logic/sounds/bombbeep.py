# -*- coding: utf-8 -*-

# project imports
from . import utils


def update_police_bomb_sounds(world):
    _empty_polices_bomb_sound_list(world.polices)

    for bomb in world.bombs:
        for police in world.polices:
            distance = utils.calculate_distance(bomb.position, police.position)
            intensity = utils.int_to_intensity(int(distance), world.constants.sound_ranges)
            if intensity != None:
                police.bomb_sounds.append(intensity)


def _empty_polices_bomb_sound_list(polices):
    for police in polices:
        police.bomb_sounds = []

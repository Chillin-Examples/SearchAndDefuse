# -*- coding: utf-8 -*-

# project imports
from . import utils


def update_police_bomb_sounds(world):
    explosion_time = world.constants.bomb_explosion_time
    _empty_polices_bomb_sound_list(world.polices)

    for bomb in world.bombs:
        bomb_sound = 0
        if bomb.explosion_remaining_time != -1:
            for sound_range in range(0, len(world.constants.sound_ranges)):
                if (sound_range*explosion_time/sound_range) <= bomb.explosion_remaining_time < ((sound_range+1)*explosion_time/sound_range):
                    bomb_sound = (sound_range+1)
                    break

        for police in world.polices:
            distance = utils.calculate_distance(bomb.position, police.position)
            value = int(bomb_sound*0.1 + distance*0.9)
            police.bomb_sounds.append(utils.convert_to_enum(value, world.constants.sound_ranges))


def _empty_polices_bomb_sound_list(polices):
    for police in polices:
        police.bomb_sounds = []

# -*- coding: utf-8 -*-

# project imports
from . import utils
from ....ks.models import EAgentStatus


def update_police_bomb_sounds(world):
    for police in world.polices:
        police.bomb_sounds = []
        if police.status == EAgentStatus.Alive:
            for bomb in world.bombs:
                distance = utils.calculate_distance(bomb.position, police.position)
                intensity = utils.int_to_intensity(int(distance), world.constants.sound_ranges)
                if intensity != None:
                    police.bomb_sounds.append(intensity)

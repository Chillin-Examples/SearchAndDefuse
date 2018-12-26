# -*- coding: utf-8 -*-

# python imports
import math

# project imports
from ...ks.models import *


def calculate_intensity(distance):
    return int(distance)


def calculate_distance(point_a, point_b):
    return math.sqrt(math.pow(point_a.x - point_b.y, 2) + math.pow(point_a.y - point_b.y, 2))


def convert_to_enum(intensity, max_intensities_dict):
    if max_intensities_dict['max_weak_sound_bomb'] > intensity:
        return ESoundIntensity.Weak
    elif max_intensities_dict['max_weak_sound_bomb'] <= intensity <= max_intensities_dict['max_normal_sound_bomb']:
        return ESoundIntensity.Normal
    elif max_intensities_dict['max_strong_sound_bomb'] < intensity:
        return ESoundIntensity.Strong

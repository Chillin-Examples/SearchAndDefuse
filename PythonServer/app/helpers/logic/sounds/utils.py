# -*- coding: utf-8 -*-

# python imports
import math

# project imports
from ....ks.models import ESoundIntensity


def calculate_distance(point_a, point_b):
    return math.sqrt(math.pow(point_a.x - point_b.x, 2) + math.pow(point_a.y - point_b.y, 2))


def int_to_intensity(intensity, max_intensities_dict):
    max_strong = max_intensities_dict[ESoundIntensity.Strong]
    max_normal = max_intensities_dict[ESoundIntensity.Normal]
    max_weak = max_intensities_dict[ESoundIntensity.Weak]

    if intensity <= max_strong:
        return ESoundIntensity.Strong
    elif max_strong < intensity <= max_normal:
        return ESoundIntensity.Normal
    elif max_normal < intensity <= max_weak:
        return ESoundIntensity.Weak
    else:
        return None

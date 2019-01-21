# -*- coding: utf-8 -*-

# python imports
import math

# project imports
from ....ks.models import ESoundIntensity


def calculate_distance(point_a, point_b):
    return math.sqrt(math.pow(point_a.x - point_b.x, 2) + math.pow(point_a.y - point_b.y, 2))


def _int_to_intensity(intensity, sound_ranges):
    max_strong = sound_ranges[ESoundIntensity.Strong]
    max_normal = sound_ranges[ESoundIntensity.Normal]
    max_weak = sound_ranges[ESoundIntensity.Weak]

    if intensity <= max_strong:
        return ESoundIntensity.Strong
    elif max_strong < intensity <= max_normal:
        return ESoundIntensity.Normal
    elif max_normal < intensity <= max_weak:
        return ESoundIntensity.Weak
    else:
        return None


def distances_to_intensities(distances, sound_ranges):
    distances.sort()
    intensities = []
    for distance in distances:
        intensity = _int_to_intensity(distance, sound_ranges)
        if intensity != None:
            intensities.append(intensity)

    return intensities

# -*- coding: utf-8 -*-

# python imports
import math

# project imports
from ....ks.models import ESoundIntensity
from ..dls import dls
from ....ks.models import ECell



_sound_pass_ecells = [ECell.Empty, ECell.SmallBombSite, ECell.MediumBombSite, ECell.LargeBombSite, ECell.VastBombSite]


def calculate_distance(world, point_a, point_b):
    distance, _ = dls(world, point_a, world.constants.sound_ranges[ESoundIntensity.Weak], point_b, _sound_pass_ecells)
    if distance == None:
        distance = world.constants.sound_ranges[ESoundIntensity.Weak] + 1
    return distance


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

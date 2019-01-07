# -*- coding: utf-8 -*-

# project imports
from . import defuse_timer, plant_timer


def update_bombs_timings(world):
    bomb_timings = []
    bomb_timings += defuse_timer.update_defuse_timings(world)
    bomb_timings += plant_timer.update_plant_timings(world)
    return bomb_timings

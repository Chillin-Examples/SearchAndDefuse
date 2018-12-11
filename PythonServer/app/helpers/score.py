# -*- coding: utf-8 -*-


def increase_score(operation_type, world):
    if operation_type == "defuse":
        _increase_police_score(world, world.constants.bomb_defusion_score)


def _increase_police_score(world, score):
        world.scores['Police'] += score

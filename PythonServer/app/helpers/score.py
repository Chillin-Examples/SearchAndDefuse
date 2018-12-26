# -*- coding: utf-8 -*-

# python imports
from enum import Enum

# project imports
from ..ks.models import ECell


class OperationType(Enum):
    Plant = 0
    Explode = 1
    Defuse = 2
    KillTerrorist = 3


def increase_score(operation_type, world, bomb_position=None):
    if operation_type == OperationType.Plant:
        _increase_terrorist_score(world, bomb_position, world.constants.bomb_planting_score)
    if operation_type == OperationType.Explode:
        _increase_terrorist_score(world, bomb_position, world.constants.bomb_explosion_score)
    if operation_type == OperationType.Defuse:
        _increase_police_score(world, world.constants.bomb_defusion_score)
    if operation_type == OperationType.KillTerrorist:
        _increase_police_score(world, world.constants.terrorist_death_score)


def _increase_police_score(world, score):
        world.scores['Police'] += score


def _increase_terrorist_score(world, bomb_position, score):
    score_coefficients = {
        ECell.SmallBombSite: world.constants.score_coefficient_small_bomb_site,
        ECell.MediumBombSite: world.constants.score_coefficient_medium_bomb_site,
        ECell.LargeBombSite: world.constants.score_coefficient_large_bomb_site,
        ECell.VastBombSite: world.constants.score_coefficient_vast_bomb_site
    }
    world.scores['Terrorist'] += score_coefficients[world.board[bomb_position.y][bomb_position.x]] * score

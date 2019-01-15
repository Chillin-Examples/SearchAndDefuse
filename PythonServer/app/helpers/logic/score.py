# -*- coding: utf-8 -*-

# project imports
from ...ks.models import ECell


def increase_defuse_score(world):
    world.scores['Police'] += world.constants.bomb_defusion_score


def increase_eliminate_terrorist_score(world):
    world.scores['Police'] += world.constants.terrorist_death_score


def increase_plant_score(world, bomb_position):
    score_coefficients = {
        ECell.SmallBombSite: world.constants.score_coefficient_small_bomb_site,
        ECell.MediumBombSite: world.constants.score_coefficient_medium_bomb_site,
        ECell.LargeBombSite: world.constants.score_coefficient_large_bomb_site,
        ECell.VastBombSite: world.constants.score_coefficient_vast_bomb_site
    }
    world.scores['Terrorist'] += score_coefficients[world.board[bomb_position.y][bomb_position.x]] * world.constants.bomb_planting_score


def increase_explode_bomb_score(world, bomb_position):
    score_coefficients = {
        ECell.SmallBombSite: world.constants.score_coefficient_small_bomb_site,
        ECell.MediumBombSite: world.constants.score_coefficient_medium_bomb_site,
        ECell.LargeBombSite: world.constants.score_coefficient_large_bomb_site,
        ECell.VastBombSite: world.constants.score_coefficient_vast_bomb_site
    }
    world.scores['Terrorist'] += score_coefficients[world.board[bomb_position.y][bomb_position.x]] * world.constants.bomb_explosion_score


def increase_eliminate_police_score(world):
    world.scores['Terrorist'] += world.constants.police_death_score

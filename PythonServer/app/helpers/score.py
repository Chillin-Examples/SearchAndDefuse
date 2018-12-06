# -*- coding: utf-8 -*-

# project imports
from ..ks.models import ECell

handled_bombsites_planted_scores = []


def increase_score(operation_type, world, bomb_position):
    if operation_type == "plant":
        if bomb_position not in handled_bombsites_planted_scores:
            _increase(world, bomb_position, world.constants.bomb_planting_score)
            handled_bombsites_planted_scores.append(bomb_position)
    elif operation_type == "explode":
        _increase(world, bomb_position, world.constants.bomb_explosion_score)


def _increase(world, bomb_position, score):
    if world.board[bomb_position.y][bomb_position.x] == ECell.SmallBombSite:
        world.scores['Terrorist'] += world.constants.score_coefficient_small_bomb_site * score
    elif world.board[bomb_position.y][bomb_position.x] == ECell.MediumBombSite:
        world.scores['Terrorist'] += world.constants.score_coefficient_medium_bomb_site * score
    elif world.board[bomb_position.y][bomb_position.x] == ECell.LargeBombSite:
        world.scores['Terrorist'] += world.constants.score_coefficient_large_bomb_site * score
    elif world.board[bomb_position.y][bomb_position.x] == ECell.VastBombSite:
        world.scores['Terrorist'] += world.constants.score_coefficient_vast_bomb_site * score

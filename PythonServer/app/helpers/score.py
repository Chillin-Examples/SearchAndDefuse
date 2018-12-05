# -*- coding: utf-8 -*-

# project imports
from ..ks.models import ECell
from ..extensions.agent import directions

planted_bombs = []

def increase_score_on_plant(world, bomb_position):

    if bomb_position not in planted_bombs:
        if world.board[bomb_position.y][bomb_position.x] == ECell.SmallBombSite:
            world.scores['Terrorist'] += world.constants.score_coefficient_small_bomb_site*world.bomb_planting_score
        elif world.board[bomb_position.y][bomb_position.x] == ECell.MediumBombSite:
            world.scores['Terrorist'] += world.constants.score_coefficient_medium_bomb_site*world.bomb_planting_score
        elif world.board[bomb_position.y][bomb_position.x] == ECell.LargeBombSite:
            world.scores['Terrorist'] += world.constants.score_coefficient_large_bomb_site*world.bomb_planting_score
        elif world.board[bomb_position.y][bomb_position.x] == ECell.VastBombSite:
            world.scores['Terrorist'] += world.constants.score_coefficient_vast_bomb_site*world.bomb_planting_score
        planted_bombs.append(bomb_position)

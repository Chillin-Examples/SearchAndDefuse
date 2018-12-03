# -*- coding: utf-8 -*-

# project imports
from ..ks.models import ECell
from ..extensions.agent import directions


def increase_score_on_plant(world, terrorist, command):
    new_bomb_position = terrorist.position.add(directions[command.direction.name])

    # Update Terrorists Score
    if world.board[new_bomb_position.y][new_bomb_position.x] == ECell.SmallBombSite:
        world.scores['Terrorist'] += world.constants.score_coefficient_small_bomb_site
    elif world.board[new_bomb_position.y][new_bomb_position.x] == ECell.MediumBombSite:
        world.scores['Terrorist'] += world.constants.score_coefficient_medium_bomb_site
    elif world.board[new_bomb_position.y][new_bomb_position.x] == ECell.LargeBombSite:
        world.scores['Terrorist'] += world.constants.score_coefficient_large_bomb_site
    elif world.board[new_bomb_position.y][new_bomb_position.x] == ECell.VastBombSite:
        world.scores['Terrorist'] += world.constants.score_coefficient_vast_bomb_site

# -*- coding: utf-8 -*-

# project imports
from ..ks.commands import *
from ..ks.models import *


def move(self, world, command):
    self.position = self.position + directions[command.direction.name]


def can_move(self, side_name, world, command):
    new_position = self.position.add(directions[command.direction.name])

    # Check new cell is empty
    valid_cells = [ECell.Empty, ECell.LargeBombSite,
                   ECell.VastBombSite, ECell.MediumBombSite, ECell.SmallBombSite]
    if world.board[new_position.y][new_position.x] in valid_cells:

        # check no bombs are being exploded.
        for bomb in world.bombs:
            if bomb.position == new_position and bomb.explosion_remaining_time > 0:
                return False

        # Check No Teammate Is There
        teammates = world.polices if side_name == 'Police' else world.terrorists
        for teammate in teammates:
            if teammate.position == new_position and teammate != self:
                return False

        return True

    return False


directions = {
    ECommandDirection.Up.name: Position(x=0, y=-1),
    ECommandDirection.Right.name: Position(x=1, y=0),
    ECommandDirection.Down.name: Position(x=0, y=1),
    ECommandDirection.Left.name: Position(x=-1, y=0)
}

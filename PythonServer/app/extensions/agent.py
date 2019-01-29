# -*- coding: utf-8 -*-

# python imports
from enum import Enum

# project imports
from ..ks.commands import *
from ..ks.models import *


class ECanMoveStatus(Enum):
    Can = 0
    Cant = 1
    TeammateBlock = 2


def move(self, world, command):
    self.position = self.position + directions[command.direction.name]
    self.is_moving = True


def can_move(self, side_name, world, command):
    new_position = self.position + directions[command.direction.name]

    # Check new cell is empty
    if world.board[new_position.y][new_position.x] != ECell.Empty:
        return ECanMoveStatus.Cant

    # Check No Teammate Is There
    teammates = world.polices if side_name == 'Police' else world.terrorists
    for teammate in teammates:
        if teammate == self:
            continue
        if teammate.position == new_position and teammate.status == EAgentStatus.Alive:
            return ECanMoveStatus.TeammateBlock

    return ECanMoveStatus.Can


directions = {
    ECommandDirection.Up.name: Position(x=0, y=-1),
    ECommandDirection.Right.name: Position(x=1, y=0),
    ECommandDirection.Down.name: Position(x=0, y=1),
    ECommandDirection.Left.name: Position(x=-1, y=0)
}

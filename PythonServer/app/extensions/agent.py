# -*- coding: utf-8 -*-

from ..ks.commands import *
# project imports
from ..ks.models import *


def move(self, command):
    self.position = self.position.add_to_another_position(directions[command.direction.name])


directions = {
    ECommandDirection.Up.name: Position(x=0, y=-1),
    ECommandDirection.Right.name: Position(x=1, y=0),
    ECommandDirection.Down.name: Position(x=0, y=1),
    ECommandDirection.Left.name: Position(x=-1, y=0)}

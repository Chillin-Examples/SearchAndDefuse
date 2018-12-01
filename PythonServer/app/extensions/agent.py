# -*- coding: utf-8 -*-

# project imports
from ..ks.commands import *
from ..ks.models import *


def move(self, command):
    self.position = self.position.add(directions[command.direction.name])


directions = {
    ECommandDirection.Up.name: Position(x=0, y=-1),
    ECommandDirection.Right.name: Position(x=1, y=0),
    ECommandDirection.Down.name: Position(x=0, y=1),
    ECommandDirection.Left.name: Position(x=-1, y=0)
}

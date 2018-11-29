# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..handlers.logic_handler import LogicHandler


def move(self, command):
    self.position.add_to_another_position(directions[command.direction.name])


directions = LogicHandler.directions

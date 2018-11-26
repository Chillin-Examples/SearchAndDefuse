# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *


def apply_command(self, side_name, command, directions):
    # Read Commands
    if command.name() == Move.name():
        if not _check_move_condition(self, side_name, command, directions['move_dir']):
            return False
        return True

def _check_move_condition(self, side_name, command, move_dir):
    pass

World.apply_command = apply_command

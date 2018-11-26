# -*- coding: utf-8 -*-

# project imports
from ..ks.models import World
from ..ks.commands import Move


def apply_command(self, side_name, command):
    # Read Commands
    if command.name() == Move.name():
        if not _check_move_condition(self, side_name, command):
            return False
        return True

def _check_move_condition(self, side_name, command):
    pass

World.apply_command = apply_command

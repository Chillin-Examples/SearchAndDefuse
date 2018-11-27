# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command, directions):
    # Read Commands
    if command.name() == Move.name():
        if not check_move_condition(self, side_name, command, directions['move_dir']):
            return False
        event = GuiEventType.move_police
        return GuiEvent(event)

def check_move_condition(self, side_name, command, move_dirs):
    player = None

    # Get Player Who Gave Command
    if side_name == 'Police':
        player = self.polices[command.id]

    elif side_name == 'Terrorist':
        player = self.terrorists[command.id]

    # Get New Position
    new_position_x = player.position.x + move_dirs[command.direction.name].x
    new_position_y = player.position.y + move_dirs[command.direction.name].y
    new_position = Position(x=new_position_x, y=new_position_y)

    # Check There Is No Wall In Path
    if self.board[new_position_y][new_position_x] != ECell.Wall:

        # Check No Teammate Is There
        if side_name == 'Police':
            for check_police in self.polices:
                if check_police.position == new_position:
                    return False

            player.position = new_position
            return True

        if side_name == 'Terrorist':
            for check_terrorist in self.terrorists:
                if check_terrorist.position == new_position:
                    return False

            player.position = new_position
            return True

    return False


World.apply_command = apply_command

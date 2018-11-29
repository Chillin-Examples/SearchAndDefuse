# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command, directions):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}

    # Read Commands
    if command.name() == Move.name():
        if not self._check_move_condition(side_name, command, directions['move_dir']):
            return False
        else:
            agents[side_name][command.id].move()
            self._apply_move(command, side_name, directions['move_dir'])
            event = GuiEventType.move_police
            return GuiEvent(event)


def _check_move_condition(self, side_name, command, move_dirs):

    player = _get_player_by_command(self, command, side_name)

    new_position = _get_new_position(self, player, move_dirs, command.direction.name)

    # Check There Is No Wall In Path
    if self.board[new_position.y][new_position.x] != ECell.Wall:

        # Check No Teammate Is There
        if side_name == 'Police':
            for check_police in self.polices:
                if check_police.position == new_position:
                    return False

            return True

        if side_name == 'Terrorist':
            for check_terrorist in self.terrorists:
                if check_terrorist.position == new_position:
                    return False

            return True

    return False


World._agent =
World.apply_command = apply_command
World._check_move_condition = _check_move_condition

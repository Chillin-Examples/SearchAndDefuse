# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..gui_events import GuiEvent, GuiEventType
from ..handlers.logic_handler import LogicHandler

def apply_command(self, side_name, command):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}

    # Read Commands
    if command.name() == Move.name():
        agent = agents[side_name][command.id]
        if not self._check_move_condition(side_name, agent):
            return False
        else:
            agent.move()
            event = GuiEventType.move_police
            return GuiEvent(event)


def _check_move_condition(self, side_name, agent):


    new_position = agent.position.add_to_another_position(LogicHandler.directions)

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


# World._agent =
World.apply_command = apply_command
World._check_move_condition = _check_move_condition

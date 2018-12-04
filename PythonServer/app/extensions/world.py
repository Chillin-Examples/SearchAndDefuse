# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..gui_events import GuiEvent, GuiEventType
from .agent import directions


def apply_command(self, side_name, command):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}

    # Read Commands
    if command.name() == Move.name():
        agent = agents[side_name][command.id]
        if not self._can_move_agent(side_name, agent, command):
            return []
        agent.move(command)

        event_type = GuiEventType.MovePolice if side_name == 'Police' else GuiEventType.MoveTerrorist
        return [GuiEvent(event_type, agent_id=agent.id, agent_position=agent.position)]

    elif command.name() == DefuseBomb.name():
        # Only terrorists can plan
        if side_name == "Terrorist":
            return []

        police = agents["Police"][command.id]
        if not self._can_defuse_bomb(police, command):
            return []
        police.defuse_bomb(self, command)

        event_type = GuiEventType.DefuseBomb
        return [GuiEvent(event_type, bomb_position=police.position.add(directions[command.direction.name]))]


def _can_move_agent(self, side_name, agent, command):
    new_position = agent.position.add(directions[command.direction.name])

    # Check new cell is empty
    if self.board[new_position.y][new_position.x] == ECell.Empty:
        # Check No Teammate Is There
        teammates = self.polices if side_name == 'Police' else self.terrorists

        for teammate in teammates:
            if teammate.position == new_position:
                return False

        return True

    return False


def _can_defuse_bomb(self, police, command):
    planted_position = police.position.add(directions[command.direction.name])

    # If bomb exists return True
    for planted_bomb in self.bombs:
        if planted_bomb.position == planted_position:
            return True

    # Otherwise return False!
    return False


World.apply_command = apply_command
World._can_move = _can_move_agent
World._can_defuse = _can_defuse_bomb

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..gui_events import GuiEvent, GuiEventType
from .agent import directions


def apply_command(self, side_name, command):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}
    bombs = self.bombs

    # Read Commands
    if command.name() == Move.name():
        agent = agents[side_name][command.id]
        if not self._can_move(side_name, agent, command):
            return []
        agent.move(command)

        event_type = GuiEventType.MovePolice if side_name == 'Police' else GuiEventType.MoveTerrorist
        return [GuiEvent(event_type, agent_id=agent.id, agent_position=agent.position)]

    elif command.name() == PlantBomb.name():
        if side_name == "Police":
            return []
        else:
            terrorist = agents["Terrorist"][command.id]
            if not self._can_plant(self, terrorist, command):
                return []
            terrorist.plant_bomb()


def _can_move(self, side_name, agent, command):
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


def _can_plant(self, terrorist, command):
    new_bomb_position = terrorist.add(directions[command.direction.name])

    for planted_bomb in self.bombs:
        if planted_bomb.position == new_bomb_position:
            return False

    return True


World.apply_command = apply_command
World._can_move = _can_move
World._can_plant = _can_plant

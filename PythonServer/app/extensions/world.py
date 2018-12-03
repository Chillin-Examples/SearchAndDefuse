# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..gui_events import GuiEvent, GuiEventType
from .agent import directions
from ..helpers.score import increase_score_on_plant


def apply_command(self, side_name, command):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}

    # Read Commands
    if command.name() == Move.name():
        agent = agents[side_name][command.id]
        if not self._can_move(side_name, agent, command):
            return []
        agent.move(command)

        event_type = GuiEventType.MovePolice if side_name == 'Police' else GuiEventType.MoveTerrorist
        return [GuiEvent(event_type, agent_id=agent.id, agent_position=agent.position)]

    elif command.name() == PlantBomb.name():
        # Only terrorists can plan
        if side_name == "Police":
            return []

        terrorist = agents["Terrorist"][command.id]
        if not self._can_plant(terrorist, command):
            return []
        terrorist.plant_bomb(self, command)
        self._increase_score_on_plant(terrorist, command)

        event_type = GuiEventType.PlantBomb
        return [GuiEvent(event_type, bomb_position=terrorist.position.add(directions[command.direction.name]))]


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
    new_bomb_position = terrorist.position.add(directions[command.direction.name])

    # If it's not a bombsite return false
    if not self.board[new_bomb_position.y][new_bomb_position.x] == ECell.SmallBombSite or \
            self.board[new_bomb_position.y][new_bomb_position.x] == ECell.MediumBombSite or \
            self.board[new_bomb_position.y][new_bomb_position.x] == ECell.LargeBombSite or \
            self.board[new_bomb_position.y][new_bomb_position.x] == ECell.VastBombSite:
        return False

    # If it already has a bomb return false
    for planted_bomb in self.bombs:
        if planted_bomb.position == new_bomb_position:
            return False

    # Otherwise return True!
    return True


World.apply_command = apply_command
World._can_move = _can_move
World._can_plant = _can_plant
World._increase_score_on_plant = increase_score_on_plant

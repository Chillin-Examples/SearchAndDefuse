# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..gui_events import GuiEvent, GuiEventType
from .agent import directions
from ..helpers import fog


def apply_command(self, side_name, command):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}

    # Read Commands
    if command.name() == Move.name():
        agent = agents[side_name][command.id]
        if side_name == "Terrorist" and agent.planting_remaining_time != -1:
            agent.cancel_plant(self)

        if not self._can_move_agent(side_name, agent, command):
            return []

        agent.move(self, command)
        # update agent vision
        agent.vision = fog.compute_agent_fog(agent, self)
        event_type = GuiEventType.MovePolice if side_name == 'Police' else GuiEventType.MoveTerrorist
        return [GuiEvent(event_type, agent_id=agent.id, agent_position=agent.position)]

    elif command.name() == PlantBomb.name():
        # Only terrorists can plan
        if side_name == "Police":
            return []

        terrorist = agents["Terrorist"][command.id]
        if not self._can_plant_bomb(terrorist, command):
            return []
        terrorist.plant_bomb(self, command)

        # TODO event should be matched with bomb when plantation is done
        event_type = GuiEventType.PlantingBomb
        return [GuiEvent(event_type, bomb_position=terrorist.position.add(directions[command.direction.name]))]


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


def _can_plant_bomb(self, terrorist, command):
    new_bomb_position = terrorist.position.add(directions[command.direction.name])

    # If it's not a bombsite return false
    if self.board[new_bomb_position.y][new_bomb_position.x] not in [ECell.SmallBombSite, ECell.MediumBombSite,
                                                                    ECell.LargeBombSite, ECell.VastBombSite]:
        return False

    # If it already has a bomb with different planter
    for planted_bomb in self.bombs:
        if planted_bomb.position == new_bomb_position and planted_bomb.planter_id != terrorist.id:
            return False

        # if bomb is exploding
        if planted_bomb.explosion_remaining_time != -1:
            return False

    # Otherwise return True!
    return True


World.apply_command = apply_command
World._can_move_agent = _can_move_agent
World._can_plant_bomb = _can_plant_bomb

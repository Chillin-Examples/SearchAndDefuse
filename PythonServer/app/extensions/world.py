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

        # cancel defuse command if agent is defusing
        if side_name == "Police" and agent.defusion_remaining_time != -1:
            agent.cancel_defuse(self)

        elif side_name == "Terrorist" and agent.planting_remaining_time != -1:
            agent.cancel_plant(self)

        if not self._can_move_agent(side_name, agent, command):
            return []
        agent.move(self, command)

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

    elif command.name() == DefuseBomb.name():
        # Only terrorists can plan
        if side_name == "Terrorist":
            return []

        police = agents["Police"][command.id]
        if not self._can_defuse_bomb(police, command):
            return []
        police.defuse_bomb(self, command)

        event_type = GuiEventType.DefusingBomb
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


def _can_defuse_bomb(self, police, command):
    planted_position = police.position.add(directions[command.direction.name])

    for planted_bomb in self.bombs:

        # no police is defusing at the moment
        if planted_bomb.defuser_id == -1 or planted_bomb.defuser_id == police.id:
            # bomb exists and is exploding
            if planted_bomb.position == planted_position and planted_bomb.explosion_remaining_time != -1:
                return True

    # Otherwise return False!
    return False


World.apply_command = apply_command
World._can_move_agent = _can_move_agent
World._can_defuse_bomb = _can_defuse_bomb
World._can_plant_bomb = _can_plant_bomb

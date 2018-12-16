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

    if command.name() == PlantBomb.name():
        # Only terrorists can plan
        if side_name == "Police":
            return []

        terrorist = agents["Terrorist"][command.id]
        if not terrorist.can_plant_bomb(self, command):
            return []
        terrorist.plant_bomb(self, command)

        # TODO event should be matched with bomb when plantation is done
        event_type = GuiEventType.PlantingBomb
        return [GuiEvent(event_type, bomb_position=terrorist.position.add(directions[command.direction.name]))]

    if command.name() == DefuseBomb.name():
        # Only terrorists can plan
        if side_name == "Terrorist":
            return []

        police = agents["Police"][command.id]
        if not police.can_defuse_bomb(self, command):
            return []
        police.defuse_bomb(self, command)

        event_type = GuiEventType.DefusingBomb
        return [GuiEvent(event_type, bomb_position=police.position.add(directions[command.direction.name]))]


def _can_move_agent(self, side_name, agent, command):
    new_position = agent.position.add(directions[command.direction.name])

    # Check new cell is empty
    valid_cells = [ECell.Empty, ECell.ExplodedBombSite, ECell.LargeBombSite,
                   ECell.VastBombSite, ECell.MediumBombSite, ECell.SmallBombSite]
    if self.board[new_position.y][new_position.x] in valid_cells:
        # Check No Teammate Is There
        teammates = self.polices if side_name == 'Police' else self.terrorists
        for teammate in teammates:
            if teammate.position == new_position and teammate != agent:
                return False

        return True

    return False


World.apply_command = apply_command
World._can_move_agent = _can_move_agent

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
        if side_name == "Police" and agent.defusion_remaining_time > 0:
            agent.cancel_defuse(self)

            event_type = GuiEventType.CancelBombOp
            return [GuiEvent(event_type, bomb_position=agent.position.add(directions[command.direction.name]))]

        # cancel plant command if agent is planting
        if side_name == "Terrorist" and agent.planting_remaining_time > 0:
            agent.cancel_plant(self)

            event_type = GuiEventType.CancelBombOp
            return [GuiEvent(event_type, bomb_position=agent.position.add(directions[command.direction.name]))]

        if not agent.can_move(side_name, self, command):
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


World.apply_command = apply_command

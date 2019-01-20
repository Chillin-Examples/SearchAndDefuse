# -*- coding: utf-8 -*-

# project imports
from ..ks.commands import *
from ..ks.models import World, EAgentStatus


def apply_command(self, side_name, command):
    agent = self.polices[command.id] if side_name == 'Police' else self.terrorists[command.id]

    if agent.status == EAgentStatus.Dead:
        return []

    # Read Commands
    # Move
    if command.name() == Move.name():
        move_events = []

        # check if agent is planting/defusing.
        if side_name == 'Terrorist':
            if agent.planting_remaining_time != -1:
                move_events += agent.cancel_plant(self)
        if side_name == 'Police':
            if agent.defusion_remaining_time != -1:
                move_events += agent.cancel_defuse(self)

        if not agent.can_move(side_name, self, command):
            return move_events
        move_events += agent.move(self, command)

        return move_events

    # Plant
    if command.name() == PlantBomb.name():
        # Only terrorists can plant
        if side_name == "Police":
            return []

        plant_events = []

        if agent.can_plant_bomb(self, command):
            plant_events += agent.plant_bomb(self, command)

        return plant_events

    # Defuse
    if command.name() == DefuseBomb.name():
        # Only polices can defuse
        if side_name == "Terrorist":
            return []

        defuse_events = []

        if agent.can_defuse_bomb(self, command):
            defuse_events += agent.defuse_bomb(self, command)

        return defuse_events


World.apply_command = apply_command

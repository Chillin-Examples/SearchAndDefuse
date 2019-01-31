# -*- coding: utf-8 -*-

# project imports
from ..ks.commands import *
from ..ks.models import World, EAgentStatus
from .agent import ECanMoveStatus


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

        can_move_status = agent.can_move(side_name, self, command)
        # Can Move
        if can_move_status == ECanMoveStatus.Can:
            move_events += agent.move(self, command)
            return move_events, None
        # Cant Move
        if can_move_status == ECanMoveStatus.Cant:
            return move_events, None
        # Teammate Block
        if can_move_status == ECanMoveStatus.TeammateBlock:
            return move_events, (agent, side_name, command)

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

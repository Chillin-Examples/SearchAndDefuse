# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..helpers import vision


def apply_command(self, side_name, command):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}

    # Read Commands
    if command.name() == Move.name():
        move_events = []
        agent = agents[side_name][command.id]
        if not agent.can_move(side_name, self, command):
            return []
        move_events += agent.move(self, command)

        # update world visions
        if side_name == 'Police':
            self.visions[side_name] = vision.compute_polices_visions(self)
        else:
            self.visions[side_name] = vision.compute_terrorists_visions(self)

        return move_events

    if command.name() == PlantBomb.name():
        plant_events = []

        # Only terrorists can plan
        if side_name == "Police":
            return []

        terrorist = agents["Terrorist"][command.id]
        if not terrorist.can_plant_bomb(self, command):
            return []
        plant_events += terrorist.plant_bomb(self, command)

        return plant_events

    if command.name() == DefuseBomb.name():
        defuse_events = []

        # Only terrorists can plan
        if side_name == "Terrorist":
            return []

        police = agents["Police"][command.id]
        if not police.can_defuse_bomb(self, command):
            return []
        defuse_events += police.defuse_bomb(self, command)

        return defuse_events


World.apply_command = apply_command

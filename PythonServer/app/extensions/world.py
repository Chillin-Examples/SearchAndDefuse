# -*- coding: utf-8 -*-

# project imports
from ..ks.commands import *
from ..gui_events import GuiEventType, GuiEvent
from ..ks.models import World, Status
from ..helpers import vision


def apply_command(self, side_name, command):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}

    # Read Commands
    if command.name() == Move.name():
        move_events = []
        terrorist_death_events = []
        agent = agents[side_name][command.id]
        if agent.status == Status.Alive:
            if not agent.can_move(side_name, self, command):
                return []
            move_events += agent.move(self, command)

            # check death terrorist
            if side_name == 'Police':
                for police_vision in self.visions['Police']:
                    for terrorist in self.terrorists:
                        if terrorist.position == police_vision:
                            terrorist.status = Status.Dead
                            terrorist_death_events.append(GuiEvent(GuiEventType.TerroristDeath,
                                                                   terrorist_id=terrorist.id))
                            self.visions["Terrorist"] = vision.compute_terrorists_visions(self)

            # update world visions
            if side_name == 'Police':
                self.visions[side_name] = vision.compute_polices_visions(self)
            if side_name == 'Terrorist':
                self.visions[side_name] = vision.compute_terrorists_visions(self)
        move_events += terrorist_death_events
        return move_events

    if command.name() == PlantBomb.name():
        plant_events = []

        # Only terrorists can plan
        if side_name == "Police":
            return []
        terrorist = agents["Terrorist"][command.id]
        if terrorist.status == Status.Alive:
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
        if police.status == Status.Alive:
            if not police.can_defuse_bomb(self, command):
                return []
            defuse_events += police.defuse_bomb(self, command)

        return defuse_events


World.apply_command = apply_command

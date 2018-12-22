# -*- coding: utf-8 -*-

# project imports
from ..ks.models import *
from ..ks.commands import *
from ..gui_events import GuiEvent, GuiEventType
from .agent import directions
from ..helpers import sound_intensity


def apply_command(self, side_name, command):
    agents = {'Police': self.polices, 'Terrorist': self.terrorists}

    # Read Commands
    if command.name() == Move.name():
        move_events = []
        agent = agents[side_name][command.id]
        if not agent.can_move(side_name, self, command):
            return []
        move_events += agent.move(self, command)

        agent.move(self, command)
        sound_intensity.update_sound_intensities(self)
        event_type = GuiEventType.MovePolice if side_name == 'Police' else GuiEventType.MoveTerrorist
        return [GuiEvent(event_type, agent_id=agent.id, agent_position=agent.position)]

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

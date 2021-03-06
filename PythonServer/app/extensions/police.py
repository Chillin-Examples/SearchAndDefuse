# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Police, EAgentStatus
from .agent import directions, can_move as base_can_move, move as base_move
from ..gui_events import GuiEventType, GuiEvent
from ..helpers.logic import score


def move(self, world, command):
    gui_events = []
    if self.defusion_remaining_time != -1:
        gui_events += self.cancel_defuse(world)

    base_move(self, world, command)

    gui_events += [GuiEvent(GuiEventType.MovePolice, agent_id=self.id, agent_position=self.position, direction=command.direction)]
    return gui_events


def defuse_bomb(self, world, command):
    gui_events = []
    if self.defusion_remaining_time != -1:
        gui_events += self.cancel_defuse(world)

    self.defusion_remaining_time = world.constants.bomb_defusion_time
    bomb_position = self.position + directions[command.direction.name]
    defusing_bomb = None
    for bomb in world.bombs:
        if bomb.position == bomb_position:
            defusing_bomb = bomb
            bomb.defuser_id = self.id
            break

    event_type = GuiEventType.DefusingBomb
    gui_events += [GuiEvent(event_type, agent_id=self.id, bomb=defusing_bomb, direction=command.direction)]
    return gui_events


def cancel_defuse(self, world, is_alive=True):
    bomb = next((bomb for bomb in world.bombs if bomb.defuser_id == self.id), None)
    if bomb != None:
        bomb.defuser_id = -1
        self.defusion_remaining_time = -1
        event_type = GuiEventType.CancelDefuse
        return [GuiEvent(event_type, bomb=bomb, is_alive=is_alive)]


def can_defuse_bomb(self, world, command):
    planted_position = self.position + directions[command.direction.name]

    for planted_bomb in world.bombs:

        # no police is defusing at the moment
        if planted_bomb.defuser_id == -1 or planted_bomb.defuser_id == self.id:
            # bomb exists and is exploding
            if planted_bomb.position == planted_position and planted_bomb.explosion_remaining_time != -1:
                return True

    # Otherwise return False!
    return False


def _base_die(self, world):
    gui_events = []
    self.status = EAgentStatus.Dead

    # check if terrorist was planting
    if self.defusion_remaining_time != -1:
        gui_events += self.cancel_defuse(world, False)

    return gui_events


def bomb_die(self, world, bomb):
    score.increase_eliminate_police_score(world)
    gui_events = self._base_die(world)
    gui_events.append(GuiEvent(GuiEventType.BombDeath, side='Police', agent=self, bomb=bomb))
    return gui_events


Police.defuse_bomb = defuse_bomb
Police.move = move
Police.cancel_defuse = cancel_defuse
Police.can_defuse_bomb = can_defuse_bomb
Police.can_move = base_can_move
Police._base_die = _base_die
Police.bomb_die = bomb_die

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Terrorist, Bomb, ECell, EAgentStatus
from .agent import directions, can_move as base_can_move, move as base_move
from ..gui_events import GuiEventType, GuiEvent
from ..helpers.logic.sounds import footsteps
from ..helpers.logic import score, vision


def move(self, world, command):
    gui_events = []
    if self.planting_remaining_time != -1:
        gui_events += self.cancel_plant(world)

    base_move(self, world, command)
    footsteps.update_police_intensities(world)
    gui_events += [GuiEvent(GuiEventType.MoveTerrorist, agent_id=self.id, agent_position=self.position, direction=command.direction)]
    return gui_events


def plant_bomb(self, world, command):
    gui_events = []
    if self.planting_remaining_time != -1:
        gui_events += self.cancel_plant(world)

    self.planting_remaining_time = world.constants.bomb_planting_time
    bomb_position = self.position + directions[command.direction.name]
    new_bomb = Bomb(position=bomb_position, explosion_remaining_time=-1,
                    planter_id=self.id, defuser_id=-1)
    world.bombs.append(new_bomb)

    event_type = GuiEventType.PlantingBomb
    gui_events += [GuiEvent(event_type, agent_id=self.id, bomb_position=self.position.add(directions[command.direction.name]), direction=command.direction)]
    return gui_events


def cancel_plant(self, world):
    bomb = next((bomb for bomb in world.bombs if bomb.planter_id == self.id), None)
    if bomb != None:
        bomb_position = bomb.position
        world.bombs.remove(bomb)
        self.planting_remaining_time = -1
        event_type = GuiEventType.CancelPlant
        return [GuiEvent(event_type, agent_id=self.id, bomb_position=bomb_position)]


def can_plant_bomb(self, world, command):
    new_bomb_position = self.position.add(directions[command.direction.name])

    # If it's not a bombsite return false
    if world.board[new_bomb_position.y][new_bomb_position.x] not in [ECell.SmallBombSite, ECell.MediumBombSite,
                                                                     ECell.LargeBombSite, ECell.VastBombSite]:
        return False

    # If it already has a bomb with different planter
    for planted_bomb in world.bombs:
        if planted_bomb.position == new_bomb_position and planted_bomb.planter_id != self.id:
            return False

        # if bomb is exploding
        if planted_bomb.position == new_bomb_position and planted_bomb.explosion_remaining_time != -1:
            return False

    # Otherwise return True!
    return True


def die(self, world):
    gui_events = []
    self.status = EAgentStatus.Dead
    score.increase_eliminate_terrorist_score(world)

    # check if terrorist was planting
    if self.planting_remaining_time != -1:
        gui_events += self.cancel_plant(world)

    world.visions["Terrorist"] = vision.compute_terrorists_visions(world)
    gui_events += [GuiEvent(GuiEventType.TerroristDeath,
                            terrorist_id=self.id,
                            position=self.position)]
    return gui_events


Terrorist.plant_bomb = plant_bomb
Terrorist.move = move
Terrorist.cancel_plant = cancel_plant
Terrorist.can_plant_bomb = can_plant_bomb
Terrorist.can_move = base_can_move
Terrorist.die = die

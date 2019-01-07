# -*- coding: utf-8 -*-

# python imports
from copy import deepcopy

# project imports
from ..helpers.logic.timers import bomb_timer
from ..helpers.logic import vision
from ..ks.models import ECell
from ..helpers.logic.sounds import bombbeep
from ..ks.models import ECell, AgentStatus


class LogicHandler:

    def __init__(self, world, sides):
        self.world = world
        self._sides = sides
        self._last_cycle_commands = {side: {} for side in self._sides}

    def store_command(self, side_name, command):
        agents = self.world.polices if side_name == 'Police' else self.world.terrorists

        # Dead Agents Should Not Be Removed From Agents List.
        if command.id < 0 or command.id >= len(agents):
            print('Invalid id in command: %s %i' % (side_name, command.id))
            return

        print('command: %s(%i)' % (side_name, command.id))
        self._last_cycle_commands[side_name][command.id] = command

    def initialize(self):
        # initialize world vision
        self.world.visions['Police'] = vision.compute_polices_visions(self.world)
        self.world.visions['Terrorist'] = vision.compute_terrorists_visions(self.world)

    def clear_commands(self):
        self._last_cycle_commands = {side: {} for side in self._sides}

    def process(self, current_cycle):
        gui_events = []
        gui_events += bomb_timer.update_bombs_timings(self.world)
        for side in self._sides:
            for command_id in self._last_cycle_commands[side]:
                gui_events += self.world.apply_command(side, self._last_cycle_commands[side][command_id])

        # check death terrorist
        for terrorist in self.world.terrorists:
            if terrorist.status == AgentStatus.Alive:
                if any(terrorist.position == vision_position for vision_position in self.world.visions['Police']):
                    gui_events += terrorist.die(self.world)

        bombbeep.update_police_bomb_sounds(self.world)

        return gui_events

    def get_client_world(self, side_name):
        client_world = deepcopy(self.world)

        if side_name == 'Police':
            client_world.terrorists = []
            client_world.bombs = []
            for vision_position in self.world.visions['Police']:
                for bomb in self.world.bombs:
                    if bomb.position == vision_position:
                        client_world.bombs.append(bomb)

            return client_world

        elif side_name == 'Terrorist':
            client_world.polices = []
            for vision_position in self.world.visions['Terrorist']:
                for police in self.world.polices:
                    if police.position == vision_position:
                        client_world.polices.append(police)
            return client_world

    def check_end_game(self, current_cycle):
        end_game = False
        winner_sidename = None

        # times up
        if current_cycle > self.world.constants.max_cycles:
            if self.world.scores['Terrorist'] > self.world.scores['Police']:
                winner_sidename = 'Terrorist'
            elif self.world.scores['Police'] > self.world.scores['Terrorist']:
                winner_sidename = 'Police'

        # all bombs exploded
        elif all(cell not in [ECell.SmallBombSite, ECell.MediumBombSite,
                              ECell.LargeBombSite, ECell.VastBombSite] for cell in sum(self.world.board, [])):
            end_game = True
            winner_sidename = 'Terrorist'

        # all terrorists are dead
        elif all(terrorist.status == AgentStatus.Dead for terrorist in self.world.terrorists):
            end_game = True
            winner_sidename = 'Police'

        # all polices are dead
        elif all(police.status == AgentStatus.Dead for police in self.world.polices):
            end_game = True
            winner_sidename = 'Terrorist'

        details = {
            'Scores': {
                'Police': str(self.world.scores['Police']),
                'Terrorist': str(self.world.scores['Terrorist'])
            }
        }

        return end_game, winner_sidename, details

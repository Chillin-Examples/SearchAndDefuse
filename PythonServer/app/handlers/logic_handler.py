# -*- coding: utf-8 -*-

# project imports
from ..helpers.timers import bomb_timer
from ..helpers import vision
from copy import deepcopy
from ..ks.models import ECell


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
        return gui_events

    def get_client_world(self, side_name):
        client_world = deepcopy(self.world)
        if side_name == 'Police':
            client_world.terrorists = []
            for vision_position in self.world.visions[side_name]:
                for terrorist in self.world.terrorists:
                    if terrorist.position == vision_position:
                        client_world.terrorists.append(terrorist)
            return client_world

        else:
            client_world = deepcopy(self.world)
            if side_name == 'Terrorist':
                client_world.polices = []
                for vision_position in self.world.visions[side_name]:
                    for police in self.world.polices:
                        if police.position == vision_position:
                            client_world.polices.append(police)
            return client_world

    def check_end_game(self, current_cycle):
        end_game = False

        # times up!
        if current_cycle > self.world.constants.max_cycles:
            end_game = True

        # TODO this condition should be changed.
        # all bombs exploded
        if all(cell not in [ECell.SmallBombSite, ECell.MediumBombSite,
                            ECell.LargeBombSite, ECell.VastBombSite] for cell in sum(self.world.board, [])):
            end_game = True

        winner_sidename = ''
        details = {}

        # Game Statuses Should Be Cached In Details too.
        if end_game:
            if self.world.scores['Terrorist'] > self.world.scores['Police']:
                winner_sidename = 'Terrorist'
            elif self.world.scores['Police'] > self.world.scores['Terrorist']:
                winner_sidename = 'Police'
            elif ECell.SmallBombSite not in self.world.board or ECell.MediumBombSite not in self.world.board or \
                    ECell.LargeBombSite not in self.world.board or ECell.VastBombSite not in self.world.board:
                winner_sidename = 'Terrorist'

            else:
                winner_sidename = None

            details = {
                'Scores': {
                    'Police': str(self.world.scores['Police']),
                    'Terrorist': str(self.world.scores['Terrorist'])
                }
            }

        return end_game, winner_sidename, details

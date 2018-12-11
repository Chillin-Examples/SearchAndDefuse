# -*- coding: utf-8 -*-

# project imports
from ..ks.models import ECell
from ..helpers.timer import BombTimer


class LogicHandler:

    def __init__(self, world, sides):
        self.world = world
        self._sides = sides
        self._last_cycle_commands = {side: {} for side in self._sides}
        self.bomb_timer = BombTimer()

    def store_command(self, side_name, command):
        agents = self.world.polices if side_name == 'Police' else self.world.terrorists

        # Dead Agents Should Not Be Removed From Agents List.
        if command.id < 0 or command.id >= len(agents):
            print('Invalid id in command: %s %i' % (side_name, command.id))
            return

        print('command: %s(%i)' % (side_name, command.id))
        self._last_cycle_commands[side_name][command.id] = command

    def clear_commands(self):
        self._last_cycle_commands = {side: {} for side in self._sides}

    def process(self, current_cycle):
        gui_events = []
        gui_events += self.bomb_timer.update_plant_timings(self.world)
        for side in self._sides:
            for command_id in self._last_cycle_commands[side]:
                gui_events += self.world.apply_command(side, self._last_cycle_commands[side][command_id])
        return gui_events

    def get_client_world(self, side_name):
        return self.world

    def check_end_game(self, current_cycle):
        end_game = False

        # times up!
        if current_cycle > self.world.constants.max_cycles:
            end_game = True

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
            else:
                winner_sidename = None

            details = {
                'Scores': {
                    'Police': str(self.world.scores['Police']),
                    'Terrorist': str(self.world.scores['Terrorist'])
                }
            }

        return end_game, winner_sidename, details

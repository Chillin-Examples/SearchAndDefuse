# -*- coding: utf-8 -*-

# project imports
from ..helpers.timer import GameTimer, BombTimer


class LogicHandler:

    def __init__(self, world, sides):
        self.world = world
        self._sides = sides
        self._last_cycle_commands = {side: {} for side in self._sides}
        self._game_timer = GameTimer(self.world)
        self.bomb_timer = BombTimer(self.world)

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

    def process(self):
        gui_events = []
        for side in self._sides:
            for command_id in self._last_cycle_commands[side]:
                gui_events += self.world.apply_command(side, self._last_cycle_commands[side][command_id])

        return gui_events

    def get_client_world(self, side_name):
        return self.world

    def check_end_game(self, current_cycle):
        pass

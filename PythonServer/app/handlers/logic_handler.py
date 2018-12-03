# -*- coding: utf-8 -*-


class LogicHandler:

    def __init__(self, world, sides):
        self.world = world
        self._sides = sides
        self._last_cycle_commands = {side: {} for side in self._sides}

    def store_command(self, side_name, command):
        agents = self.world.polices if side_name == 'Police' else self.world.terrorists

        if command.id < 0 or command.id >= len(agents):
            print('Invalid id in command: %s %i' % (side_name, command.id))
            return

        print('command: %s(%i)' % (side_name, command.id))
        self._last_cycle_commands[side_name][command.id] = command

    def clear_commands(self):
        self._last_cycle_commands = {side: {} for side in self._sides}

    def initialize(self):
        pass

    def process(self, current_cycle):
        gui_events = []
        for side in self._sides:
            for command_id in self._last_cycle_commands[side]:
                gui_events += self.world.apply_command(side, self._last_cycle_commands[side][command_id])

        return gui_events

    def get_client_world(self, side_name):
        return self.world

    def check_end_game(self):
        pass

# -*- coding: utf-8 -*-

# python imports
from __future__ import division

# chillin imports
from chillin_server import RealtimeGameHandler

# project imports
from .handlers import map_handler, logic_handler, gui_handler


class GameManager(RealtimeGameHandler):

    def on_recv_command(self, side_name, agent_name, command_type, command):
        if None in command.__dict__.values():
            print("None in command: %s - %s" % (side_name, command_type))
            return
        self._logic_handler.store_command(side_name, command)

    def on_initialize(self):
        print('initialize')
        self._map_handler = map_handler.MapHandler(self.sides)
        world = self._map_handler.load_map(self.config)
        self._logic_handler = logic_handler.LogicHandler(world, self.sides)

    def on_initialize_gui(self):
        print('initialize gui')
        self._gui_handler = gui_handler.GuiHandler(self._logic_handler.world, self.sides, self.canvas, self.config)
        self._gui_handler.initialize()
        # Apply actions
        self.canvas.apply_actions()

    def on_process_cycle(self):
        print('cycle %i' % (self.current_cycle,))
        self._gui_events = self._logic_handler.process()
        winner_sidename, details = self._logic_handler.check_end_game(self.current_cycle)
        self.end_game(winner_sidename=winner_sidename, details=details)
        self._logic_handler.clear_commands()

    def on_update_clients(self):
        print('update clients')
        for side_name in self.sides:
            self.send_snapshot(self._logic_handler.get_client_world(side_name), side_name=side_name)

    def on_update_gui(self):
        print('update gui')
        self._gui_handler.update(self._gui_events)
        self.canvas.apply_actions()

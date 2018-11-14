# -*- coding: utf-8 -*-

# python imports
from __future__ import division

# chillin imports
from chillin_server import TurnbasedGameHandler

from .handlers import map_handler, logic_handler
from .ks.models import *


# project imports


class GameHandler(TurnbasedGameHandler):
    _map_handler, _logic_handler, _gui_handler = None, None, None
    gui_event_tmp = None

    def on_recv_command(self, side_name, agent_name, command_type, command):
        if None in command.__dict__.values():
            print("None in command: %s - %s" % (side_name, command_type))
            return

    def on_initialize(self):
        print('initialize')
        self._map_handler = map_handler.MapHandler(self.sides)
        self.world, board = self._map_handler.load_map(Constants, self.map_config, self.config)
        self.world.board = [[ECell.Empty for _ in range(self.world.width)] for _ in range(self.world.height)]
        self._logic_handler = logic_handler.LogicHandler(self.world, self.sides, board)
        self.move_dirs, self.move_angle, self.plant_dirs, \
        self.plant_angle, self.defuse_dirs, self.defuse_angle = self._logic_handler.initialize()

    def on_initialize_gui(self):
        print('initialize gui')

    def on_process_cycle(self):
        print('cycle %i' % (self.current_cycle,))
        if self.world.validate_command(None, None):
            self.world.apply_command(None, None)

    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)

    def on_update_gui(self):
        print('update gui')
        self.canvas.apply_actions()

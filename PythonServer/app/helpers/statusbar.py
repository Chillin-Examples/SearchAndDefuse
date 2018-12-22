# -*- coding: utf-8 -*-


class StatusBar:

    def __init__(self):
        self.num_bombs_exploded = 0
        self.num_bombs_defused = 0
        self.num_bombs_planted = 0
        self.police_score = 0
        self.terrorist_score = 0
        self.remaining_cycles = 0

    def update_statusbar(self, world, current_cycle):
        # scores
        self.police_score = world.scores['Police']
        self.terrorist_score = world.scores['Terrorist']

        # cycles remaining
        self.remaining_cycles = world.constants.max_cycles - current_cycle

    def update_exploded_number(self):
        self.num_bombs_exploded += 1

    def update_defused_number(self):
        self.num_bombs_defused += 1

    def update_planted_number(self):
        self.num_bombs_planted = self.num_bombs_exploded + self.num_bombs_defused

# -*- coding: utf-8 -*-

# project imports
from ..helpers import score


class BombTimer(object):

    def __init__(self, world):
        super().__init__(world)

    def update_defuse_timings(self, world):
        self.world = world

        for bomb in self.world.bombs:
                # defuse command given in current cycle.
                if self.world.polices[bomb.defuser_id].defusion_remaining_time == -1:
                    self._update_defuse_timer_on_defuse(bomb.defuser_id)
                else:

                    # defusing timer is not zero yet,police should keep defusing
                    if self.world.polices[bomb.defuser_id].defusion_remaining_time > 0:
                        self.world.polices[bomb.defuser_id].defusion_remaining_time -= 1

                    elif self.world.polices[bomb.defuser_id].defusion_remaining_time == 0:
                        score.increase_score('defuse', world)
                        del self.world.bombs[bomb]
                        self.world.polices[bomb.defuser_id].defusion_remaining_time = -1

    def _update_defuse_timer_on_defuse(self, agent_id):
        self.world.polices[agent_id].defusion_remaining_time = self.world.constants.bomb_defusion_time

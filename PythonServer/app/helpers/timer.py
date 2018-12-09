# -*- coding: utf-8 -*-

# project imports
from ..helpers import score


class BombTimer(object):

    def update_defuse_timings(self, world):

        for bomb in world.bombs:
                # defuse command given in current cycle.
                if world.polices[bomb.defuser_id].defusion_remaining_time == -1:
                    self._update_defuse_timer_on_defuse(bomb.defuser_id, world)
                else:

                    # defusing timer is not zero yet,police should keep defusing
                    if world.polices[bomb.defuser_id].defusion_remaining_time > 0:
                        world.polices[bomb.defuser_id].defusion_remaining_time -= 1

                    elif world.polices[bomb.defuser_id].defusion_remaining_time == 0:
                        score.increase_score('defuse', world)
                        del world.bombs[bomb]
                        world.polices[bomb.defuser_id].defusion_remaining_time = -1

    def _update_defuse_timer_on_defuse(self, agent_id, world):
        world.polices[agent_id].defusion_remaining_time = world.constants.bomb_defusion_time

# -*- coding: utf-8 -*-

# project imports
from .. import score
from ...gui_events import GuiEvent, GuiEventType


def update_defuse_timings(world):

    for bomb in world.bombs:

        # some police is defusing
        if bomb.defuser_id != -1:
                # defuse command given in current cycle.
                if world.polices[bomb.defuser_id].defusion_remaining_time == -1:
                    print("police {} commanded defuse.".format(bomb.defuser_id))
                    _update_defuse_timer_on_defuse(bomb.defuser_id, world)
                    return []
                else:

                    # defusing timer is not zero yet,police should keep defusing
                    if world.polices[bomb.defuser_id].defusion_remaining_time > 0:
                        print("police {} is defusing.".format(bomb.defuser_id))
                        world.polices[bomb.defuser_id].defusion_remaining_time -= 1
                        return []
                    if world.polices[bomb.defuser_id].defusion_remaining_time == 0:
                        print("bomb defused.")
                        world.polices[bomb.defuser_id].defusion_remaining_time = -1
                        bomb_position = bomb.position
                        score.increase_police_score(score.OperationType.Defuse, world)
                        world.bombs.remove(bomb)
                        return [GuiEvent(GuiEventType.DefusedBomb, bomb_position=bomb_position)]
    return []


def _update_defuse_timer_on_defuse(agent_id, world):
    world.polices[agent_id].defusion_remaining_time = world.constants.bomb_defusion_time

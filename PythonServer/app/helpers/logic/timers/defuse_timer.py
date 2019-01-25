# -*- coding: utf-8 -*-

# project imports
from .. import score
from ....gui_events import GuiEvent, GuiEventType


def update_defuse_timings(world):
    defuse_events = []
    bombs_to_remove = []

    for bomb in world.bombs:
        # some police is defusing
        if bomb.defuser_id != -1:
            # defusing timer is not zero yet,police should keep defusing
            if world.polices[bomb.defuser_id].defusion_remaining_time > 1:
                print("police {} is defusing.".format(bomb.defuser_id))
                world.polices[bomb.defuser_id].defusion_remaining_time -= 1
            # end of defusing
            else:
                print("bomb defused.")
                world.polices[bomb.defuser_id].defusion_remaining_time = -1
                score.increase_defuse_score(world)
                bombs_to_remove.append(bomb)
                defuse_events += [GuiEvent(GuiEventType.DefusedBomb, bomb=bomb)]

    for bomb in bombs_to_remove:
        world.bombs.remove(bomb)

    return defuse_events

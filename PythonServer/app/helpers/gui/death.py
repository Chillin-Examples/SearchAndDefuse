# -*- coding: utf-8 -*-


def update_on_death_terrorist(handler, dead_agents):
    # for side in dead_agents:
    for agent in dead_agents["Terrorist"]:
        canvas_pos = handler.utils.get_canvas_position(agent['position'])

        handler.canvas.edit_image(handler.img_refs["Terrorist"][agent['terrorist_id']],
                                  6000, 6000,
                                  center_origin=True)
        handler.canvas.edit_image(handler.dead_img_refs["Terrorist"][agent['terrorist_id']],
                                  canvas_pos['x'], canvas_pos['y'],
                                  center_origin=True)


def update_on_death_police(handler, dead_agents):
    # for side in dead_agents:
    for agent in dead_agents["Police"]:
        canvas_pos = handler.utils.get_canvas_position(agent['position'])

        handler.canvas.edit_image(handler.img_refs["Police"][agent['police_id']],
                                  6000, 6000,
                                  center_origin=True)
        handler.canvas.edit_image(handler.dead_img_refs["Police"][agent['police_id']],
                                  canvas_pos['x'], canvas_pos['y'],
                                  center_origin=True)

# -*- coding: utf-8 -*-

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType


def update_statusbar(handler, statusbar):
    handler.canvas.edit_text(handler.statusbar[0][1][0]['ref'], text=str(statusbar.police_score))

    handler.canvas.edit_text(handler.statusbar[0][1][2]['ref'], str(statusbar.terrorist_score))

    handler.canvas.edit_text(handler.statusbar[0][2][0]['ref'], str(statusbar.num_bombs_defused))

    handler.canvas.edit_text(handler.statusbar[0][2][2]['ref'], str(statusbar.num_bombs_exploded))

    handler.canvas.edit_text(handler.statusbar[1][1]['ref'], str(statusbar.remaining_cycles))


def initialize_statusbar(handler):
    sides_status = [[[], [], []],
                    [[], [], []],
                    [[], [], []]]

    general_status = [[], [], [], []]

    handler.statusbar.append(sides_status)
    handler.statusbar.append(general_status)

    # side status
    for i_side_status in range(0, 3):
        for j_side_status in range(0, 3):
            handler.statusbar[0][i_side_status][j_side_status] = {
                "row": j_side_status,
                "col": i_side_status,
                "x": int(
                    (handler.canvas.width - (
                            (3 - i_side_status) * int(handler.world.statusbar_width / 3))) / 3 - 600),
                "y": int(((j_side_status * 250) + 0) / 1.5 + 2100),  # 10 is y0
                "ref": None
            }

    for i_general_status in range(0, 2):
        handler.statusbar[1][i_general_status] = {
            "row": 0,
            "col": i_general_status,
            "x": int(380),
            # int((handler.canvas.width - (2 - i_general_status) * int(handler.world.statusbar_width / 2))/3-60),
            "y": int(i_general_status * 340 + 2200)  # (600 + 0)/2 + 2000)
        }

    handler.statusbar[0][0][0]['ref'] = handler.canvas.create_image('PoliceLogo',
                                                                    handler.statusbar[0][0][0]['y'],
                                                                    handler.statusbar[0][0][0]['x'],
                                                                    center_origin=True,
                                                                    scale_type=ScaleType.ScaleToWidth,
                                                                    scale_value=handler.cell_size)

    handler.statusbar[0][0][1]['ref'] = handler.canvas.create_text('vs.',
                                                                   handler.statusbar[0][0][1]['y'],
                                                                   handler.statusbar[0][0][1]['x'],
                                                                   handler.canvas.make_rgba(0, 0, 0, 255),
                                                                   handler.font_size * 2,
                                                                   center_origin=True)
    handler.statusbar[0][0][2]['ref'] = handler.canvas.create_image('TerroristLogo',
                                                                    handler.statusbar[0][0][2]['y'],
                                                                    handler.statusbar[0][0][2]['x'],
                                                                    center_origin=True,
                                                                    scale_type=ScaleType.ScaleToWidth,
                                                                    scale_value=handler.cell_size)

    handler.statusbar[0][1][0]['ref'] = handler.canvas.create_text('0',
                                                                   handler.statusbar[0][1][0]['y'],
                                                                   handler.statusbar[0][1][0]['x'],
                                                                   handler.canvas.make_rgba(0, 0, 0, 255),
                                                                   handler.font_size * 2,
                                                                   center_origin=True)

    handler.statusbar[0][1][1]['ref'] = handler.canvas.create_text('score',
                                                                   handler.statusbar[0][1][1]['y'],
                                                                   handler.statusbar[0][1][1]['x'],
                                                                   handler.canvas.make_rgba(0, 0, 0, 255),
                                                                   handler.font_size * 2,
                                                                   center_origin=True)

    handler.statusbar[0][1][2]['ref'] = handler.canvas.create_text('0',
                                                                   handler.statusbar[0][1][2]['y'],
                                                                   handler.statusbar[0][1][2]['x'],
                                                                   handler.canvas.make_rgba(0, 0, 0, 255),
                                                                   handler.font_size * 2,
                                                                   center_origin=True)

    handler.statusbar[0][2][0]['ref'] = handler.canvas.create_text('0',
                                                                   handler.statusbar[0][2][0]['y'],
                                                                   handler.statusbar[0][2][0]['x'],
                                                                   handler.canvas.make_rgba(0, 0, 0, 255),
                                                                   handler.font_size * 2,
                                                                   center_origin=True)

    handler.statusbar[0][2][1]['ref'] = handler.canvas.create_text('bombs',
                                                                   handler.statusbar[0][2][1]['y'],
                                                                   handler.statusbar[0][2][1]['x'],
                                                                   handler.canvas.make_rgba(0, 0, 0, 255),
                                                                   handler.font_size * 2,
                                                                   center_origin=True)

    handler.statusbar[0][2][2]['ref'] = handler.canvas.create_text('0',
                                                                   handler.statusbar[0][2][2]['y'],
                                                                   handler.statusbar[0][2][2]['x'],
                                                                   handler.canvas.make_rgba(0, 0, 0, 255),
                                                                   handler.font_size * 2,
                                                                   center_origin=True)

    handler.statusbar[1][0]['ref'] = handler.canvas.create_text('remaining cycles:',
                                                                handler.statusbar[1][0]['y'],
                                                                handler.statusbar[1][0]['x'],
                                                                handler.canvas.make_rgba(0, 0, 0, 255),
                                                                handler.font_size * 2,
                                                                center_origin=True)

    handler.statusbar[1][1]['ref'] = handler.canvas.create_text(str(handler.world.constants.max_cycles),
                                                                handler.statusbar[1][1]['y'],
                                                                handler.statusbar[1][1]['x'],
                                                                handler.canvas.make_rgba(0, 0, 0, 255),
                                                                handler.font_size * 2,
                                                                center_origin=True)

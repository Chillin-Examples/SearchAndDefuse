# -*- coding: utf-8 -*-


def update_board_on_move(handler, terrorists_move, polices_move):
    for side in handler.sides:
        moves = polices_move if side == 'Police' else terrorists_move
        for move in moves:
            canvas_pos = handler.utils.get_canvas_position(move['agent_position'])
            # terrorist.angle = handler.angle[EDirection.Left.name]
            handler.canvas.edit_image(handler.img_refs[side][move['agent_id']],
                                      canvas_pos['x'], canvas_pos['y'],
                                      center_origin=True)

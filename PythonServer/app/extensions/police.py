# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Police
from .agent import move, directions


def defuse_bomb(self, world, command):
    defusing_bomb = None
    bomb_position = self.position.add(directions[command.direction.name])
    for bomb in world.bombs:
        if bomb.position == bomb_position:
            defusing_bomb = bomb
            bomb.defuser_id = self.id
            break

    # check redefusing condition
    if defusing_bomb.defuser_id == self.id:
        self.cancel_defuse()


def cancel_defuse(self):
    self.defusion_remaining_time = -1


Police.defuse_bomb = defuse_bomb
Police.move = move
Police.cancel_defuse = cancel_defuse

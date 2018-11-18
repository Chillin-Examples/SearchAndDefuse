# -*- coding: utf-8 -*-

# project imports
from ks.models import World


def apply_command(self, side_name, command):
    return True


World.apply_command = apply_command

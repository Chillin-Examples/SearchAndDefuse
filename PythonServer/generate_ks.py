#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python imports
from shutil import copy

# chillin imports
from koala_serializer import generate

all_args = [('python', 'app/ks', 'snake_case'),
            ('python', '../PythonClient/ks', 'snake_case'),
            ('python', '../PythonRandomClient/ks', 'snake_case'),
            ('cpp', '../CppClient/Game/ks', 'camelCase')]

for i in range(1, 4):
        copy('app/ks/models.ks', all_args[i][1])
        copy('app/ks/commands.ks', all_args[i][1])

for args in all_args:
    generate('app/ks/commands.ks', *args)
    generate('app/ks/models.ks', *args)

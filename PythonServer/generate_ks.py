#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python imports
from shutil import copyfile

# chillin imports
from koala_serializer import generate


commands_relative_dir = '/ks/commands.ks'
models_relative_dir = '/ks/models.ks'
destination = ['../PythonClient',
               '../PythonRandomClient',
               '../CppClient/Game']

for dest in destination:
    copyfile('app/ks/commands.ks', dest + commands_relative_dir)
    copyfile('app/ks/models.ks', dest + models_relative_dir)

all_args = [('python', 'app/ks', 'snake_case'),
            ('python', '../PythonClient/ks', 'snake_case'),
            ('python', '../PythonRandomClient/ks', 'snake_case'),
            ('cpp', '../CppClient/Game/ks', 'camelCase')]

for args in all_args:
    generate('app/ks/commands.ks', *args)
    generate('app/ks/models.ks', *args)

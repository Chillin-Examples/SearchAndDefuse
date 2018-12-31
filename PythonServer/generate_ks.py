#! /usr/bin/env python
# -*- coding: utf-8 -*-

from koala_serializer import generate
from shutil import copyfile

ks_reletive_dir = '/ks/commands.ks'
destination = ['../PythonClient' + ks_reletive_dir,
               '../PythonRandomClient' + ks_reletive_dir,
               '../CppClient/Game' + ks_reletive_dir]
for dest in destination:
    copyfile('app/ks/commands.ks', dest)

all_args = [('python', 'app/ks', 'snake_case'),
            ('python', '../PythonClient/ks', 'snake_case'),
            ('python', '../PythonRandomClient/ks', 'snake_case'),
            ('cpp', '../CppClient/Game/ks', 'camelCase')]

for args in all_args:
    generate('app/ks/commands.ks', *args)
    generate('app/ks/models.ks', *args)

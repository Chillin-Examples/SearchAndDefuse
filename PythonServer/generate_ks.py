#! /usr/bin/env python
# -*- coding: utf-8 -*-

# chillin imports
from koala_serializer import generate

all_args = [('python', 'app/ks', 'snake_case'), ('python', '../PythonClient/ks', 'snake_case'),
            ('python', '../PythonRandomClient/ks', 'snake_case'),
            ('cpp', '../CppClient/Game/ks', 'camelCase')]

for args in all_args:
    generate('app/ks/commands.ks', *args)
    generate('app/ks/models.ks', *args)

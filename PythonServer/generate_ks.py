#! /usr/bin/env python
# -*- coding: utf-8 -*-

# chillin imports
from koala_serializer import generate

all_args = [('python', 'app/ks'), ('python', '../PythonClient/ks'), ('python', '../PythonRandomClient/ks'), ('cpp', '../CppClient/Game/ks')]

for args in all_args:
    generate('app/ks/commands.ks', *args)
    generate('app/ks/models.ks', *args)

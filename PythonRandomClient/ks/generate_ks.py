#! /usr/bin/env python
# -*- coding: utf-8 -*-

from koala_serializer import generate
# import sys

# if len(sys.argv) > 1:
#     lang = sys.argv[1]

python_paths = ['app/ks', '../PythonClient/ks', '../PythonRandomClient/ks']
cpp_path = '../CppClient/Game/ks'

# serialize python
for path in python_paths:
    generate('app/ks/commands.ks', 'python', path)
    generate('app/ks/models.ks', 'python', path)

# serialize cpp
generate('app/ks/commands.ks', 'cpp', cpp_path)
generate('app/ks/models.ks', 'cpp', cpp_path)

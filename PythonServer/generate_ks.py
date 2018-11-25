#! /usr/bin/env python
# -*- coding: utf-8 -*-

from koala_serializer import generate
import sys

lang = 'python'
if len(sys.argv) > 1:
    lang = sys.argv[1]

generate('app/ks/commands.ks', lang, 'app/ks')
generate('app/ks/models.ks', lang, 'app/ks')

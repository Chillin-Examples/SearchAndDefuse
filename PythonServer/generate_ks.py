#! /usr/bin/env python
# -*- coding: utf-8 -*-

from koala_serializer import generate
import sys

lang = 'python'
if len(sys.argv) > 1:
    lang = sys.argv[1]

generate('ks/commands.ks', lang, 'ks')
generate('ks/models.ks', lang, 'ks')

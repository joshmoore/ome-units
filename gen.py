#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2014 Glencoe Software, Inc. All Rights Reserved.
# Use is subject to license terms supplied in LICENSE.txt
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Generator for Genshi templates of the Units
"""

import os
import sys
import fileinput

from collections import namedtuple
from genshi.template import NewTextTemplate

data = []
Unit = namedtuple('Unit', ['CODE', 'SYMBOL', 'SYSTEM'])
data_filename = sys.argv[1]
template_name = sys.argv[2]

with open(template_name) as f:
    template = f.read()
    basename = os.path.basename(data_filename)

    for line in fileinput.input([data_filename]):
        line = line.strip()
        if line:
            line = line.decode("utf-8")
            items = tuple(line.strip().split("\t"))
            units = Unit(*items)
            data.append(units)
    tmpl = NewTextTemplate(template, encoding="utf-8")
    content = tmpl.generate(name=basename, items=data)
    print content.render(encoding="utf-8")

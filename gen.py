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
import fileinput

from collections import namedtuple
from genshi.template import MarkupTemplate
from genshi.template import NewTextTemplate
from argparse import ArgumentParser

equations_file = "units/equations.py"
if os.path.exists(equations_file):
    execfile(equations_file)  # Sets EQUATIONS
try:
    EQUATIONS.get("test")
except:
    EQUATIONS = {}
Unit = namedtuple('Unit', ['CODE', 'SYMBOL', 'SYSTEM'])
Field = namedtuple('Field', ['CLASS', 'NAME', 'TYPE', 'DEFAULT'])


class Engine(object):

    def __init__(self, template_name, markup):
        self.template_name = template_name
        self.markup = markup
        with open(self.template_name) as f:
            self.template_text = f.read()
        self.fields = self.parse("units/Fields.txt", Type=Field)

    def basename(self, data_filename):
        basename = os.path.basename(data_filename)
        basename = basename[:-4]  # Remove ".txt"
        return basename

    def parse(self, data_filename, Type=Unit):
        data = []
        for line in fileinput.input([data_filename]):
            line = line.strip()
            if line:
                line = line.decode("utf-8")
                items = tuple(line.strip().split("\t"))
                try:
                    i = Type(*items)
                except:
                    raise Exception(items)
                data.append(i)
        return data

    def render(self, **kwargs):
        markup = kwargs.pop("markup")
        if markup:
            tmpl = MarkupTemplate(
                self.template_text, encoding="utf-8")
        else:
            tmpl = NewTextTemplate(
                self.template_text, encoding="utf-8")
        content = tmpl.generate(**kwargs)
        print content.render(encoding="utf-8")

    def combined_template(self, data_filenames):
        items = dict()
        for data_filename in data_filenames:
            basename = self.basename(data_filename)
            data = self.parse(data_filename)
            items[basename] = data
        self.render(markup=self.markup,
                    items=items, fields=self.fields,
                    equations=EQUATIONS)

    def individual_templates(self, data_filename):
        basename = self.basename(data_filename)
        data = self.parse(data_filename)
        key = basename.upper()
        val = EQUATIONS[key]
        self.render(markup=self.markup,
                    name=basename, items=data, fields=self.fields,
                    equations=val)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--combine",
        action="store_true",
        help="Combine all files into a single call")
    parser.add_argument(
        "--markup",
        action="store_true",
        help="Use XML markup rather than the text template")
    parser.add_argument(
        "template_name")
    parser.add_argument(
        "data_filenames",
        nargs="+")
    ns = parser.parse_args()
    if ns.combine:
        engine = Engine(ns.template_name, markup=ns.markup)
        engine.combined_template(ns.data_filenames)
    else:
        for data_filename in ns.data_filenames:
            engine = Engine(ns.template_name, markup=ns.markup)
            engine.individual_templates(data_filename)

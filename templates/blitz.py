{% python

def calculate(cfrom, cto, coffecients):
    if not coefficients:
        return "lambda: value"
    elif coefficients == (None,):
        return 'lambda: noconversion("%s", "%s")' % (cfrom, cto)

    sb = []
    for idx, coeffs in enumerate(coefficients):

        k, p = coeffs

        if k == 0:
            continue

        if p == 1:
            lhs = k
        else:
            lhs = "(%s ** %s)" % (k, p)

        if idx == 0:
            rhs = ""
        elif idx <= 1:
            rhs = " * value"
        else:
            rhs = " * (value ** %s)" % idx

        sb += ["%s%s" % (lhs, rhs)]
    return "lambda value: %s" % "+".join(sb)

%}\
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
Code-generated omero.model.${name} implementation,
based on omero.model.PermissionsI
"""


import Ice
import IceImport
IceImport.load("omero_model_${name}_ice")
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"

from omero_model_UnitBase import UnitBase
from omero.model.enums import Units${name}


def noconversion(cfrom, cto):
    raise Exception(("Unsupported conversion: "
                     "%s:%s") % cfrom, cto)


class ${name}I(_omero_model.${name}, UnitBase):

    CONVERSIONS = dict()
{% for cfrom in sorted(conversions) %}\
{% for cto, coefficients in sorted(conversions.get(cfrom, {}).items()) %}\
{% if cfrom != cto %}\
    CONVERSIONS["${cfrom}:${cto}"] = \\
        ${calculate(cfrom, cto, coefficients)}
{% end %}\
{% end %}\
{% end %}\

    def __init__(self, value=None, unit=None):
        _omero_model.${name}.__init__(self)
        if isinstance(value, _omero_model.${name}I):
            # This is a copy-constructor call.
            target = str(unit)
            source = str(value.getUnit())
            if target == source:
                self.setValue(value.getValue())
                self.setUnit(value.getUnit())
            else:
                c = self.CONVERSIONS.get("%s:%s" % (source, target))
                if c is None:
                    t = (value.getValue(), value.getUnit(), target)
                    msg = "%s %s cannot be converted to %s" % t
                    raise Exception(msg)
                self.setValue(c(value.getValue()))
                self.setUnit(getattr(Units${name}, str(target)))
        else:
            self.setValue(value)
            self.setUnit(unit)

    def getUnit(self, current=None):
        return self._unit

    def getValue(self, current=None):
        return self._value

    def setUnit(self, unit, current=None):
        self._unit = unit

    def setValue(self, value, current=None):
        self._value = value

    def __str__(self):
        return self._base_string(self.getValue(), self.getUnit())

_omero_model.${name}I = ${name}I\

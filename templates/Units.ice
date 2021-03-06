/*
 * Copyright (C) 2014 University of Dundee & Open Microscopy Environment.
 * All rights reserved.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

{% python

def blitz(items):
    constants = [x.CODE for x in items]
    j = ",\n" + (" " * 16)
    return j.join(constants)
%}

#ifndef CLASS_UNITS
#define CLASS_UNITS

module omero {

    module model {

        module enums {

{% for name in sorted(items) %}\
            enum Units${name} {
                ${blitz(items[name])}
            };

{% end %}\
        };

    };
};
#endif

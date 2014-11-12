/*
 * Copyright (C) 2014 University of Dundee & Open Microscopy Environment
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

package ome.formats.model;

import ome.units.unit.Unit;
{% for name in sorted(items) %}\
import omero.model.${name};
import omero.model.${name}I;
{% end %}\
{% for name in sorted(items) %}\
import omero.model.enums.Units${name};
{% end %}

/**
 * Utility class to generate and convert unit objects.
 *
 * Be especially careful when using methods which take a string
 * since there are 2 types of enumerations, CODE-based and
 * SYMBOL-based.
 */
public class UnitsFactory {

{% for name in sorted(items) %}
    //
    // ${name}
    //

    public static ome.xml.model.enums.Units${name} make${name}UnitXML(String unit) {
        return ${name}I.makeXMLUnit(unit);
    }

    public static ome.units.quantity.${name} make${name}XML(double d, String unit) {
        return ${name}I.makeXMLQuantity(d, unit);
    }

    public static ${name} make${name}(double d,
            Unit<ome.units.quantity.${name}> unit) {
        return new ${name}I(d, unit);
    }

    public static ${name} make${name}(double d, Units${name} unit) {
        return new ${name}I(d, unit);
    }

    /**
     * Convert a Bio-Formats {@link ${name}} to an OMERO ${name}. A null will be
     * returned if the input is null.
     */
    public static ${name} convert${name}(ome.units.quantity.${name} value) {
        if (value == null)
            return null;
        String internal = xml${name}EnumToOMERO(value.unit().getSymbol());
        Units${name} ul = Units${name}.valueOf(internal);
        return new omero.model.${name}I(value.value().doubleValue(), ul);
    }

    public static ome.units.quantity.${name} convert${name}(${name} t) {
        return ${name}I.convert(t);
    }

    public static ${name} convert${name}(${name} value, Unit<ome.units.quantity.${name}> ul) {
        return convert${name}XML(value, ul.getSymbol());
    }

    public static ${name} convert${name}XML(${name} value, String xml) {
        String omero = xml${name}EnumToOMERO(xml);
        return new ${name}I(value, omero);
    }

    public static String xml${name}EnumToOMERO(String xml) {
        return ome.model.enums.Units${name}.bySymbol(xml).toString();
    }

{% end %}

{% for field in fields %}\
    public static Units${field.TYPE} ${field.CLASS}_${field.NAME} = Units${field.TYPE}.valueOf(xml${field.TYPE}EnumToOMERO(ome.xml.model.${field.CLASS}.get${field.NAME}UnitXsdDefault()));
{% end %}
}

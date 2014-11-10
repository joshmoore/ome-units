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

import static omero.rtypes.rstring;
import static omero.rtypes.unwrap;
import ome.units.unit.Unit;
import ome.xml.model.enums.EnumerationException;
{% for name in sorted(items) %}\
import omero.model.${name};
import omero.model.${name}I;
{% end %}\
{% for name in sorted(items) %}\
import omero.model.enums.Units${name};
{% end %}

/**
 * Utility class to generate and convert unit objects.
 */
public class UnitsFactory {

{% for name in sorted(items) %}
    //
    // ${name}
    //

    public static ${name} make${name}(double d, String unit) {
        Units${name} ul = Units${name}.valueOf(unit);
        ${name} copy = new ${name}I();
        copy.setUnit(ul);
        copy.setValue(d);
        return copy;
    }

    public static ome.xml.model.enums.Units${name} make${name}UnitXML(String unit) {
        try {
            return ome.xml.model.enums.Units${name}
                    .fromString((String) unit);
        } catch (EnumerationException e) {
            throw new RuntimeException("Bad ${name} unit: " + unit, e);
        }
    }

    public static ome.units.quantity.${name} make${name}XML(double d, String unit) {
        ome.units.unit.Unit<ome.units.quantity.${name}> units =
                ome.xml.model.enums.handlers.Units${name}EnumHandler
                        .getBaseUnit(make${name}UnitXML(unit));
        return new ome.units.quantity.${name}(d, units);
    }

    public static ${name} make${name}(double d,
            Unit<ome.units.quantity.${name}> unit) {
        return make${name}(d, unit.getSymbol());
    }

    public static ${name} make${name}(double d, Units${name} unit) {
        ${name} copy = new ${name}I();
        copy.setUnit(unit);
        copy.setValue(d);
        return copy;
    }

    /**
     * Convert a Bio-Formats {@link ${name}} to an OMERO ${name}. A null will be
     * returned if the input is null.
     */
    public static ${name} convert${name}(ome.units.quantity.${name} value) {
        if (value == null)
            return null;
        Units${name} ul = Units${name}.valueOf(value.unit().getSymbol());
        omero.model.${name} l = new omero.model.${name}I();
        l.setValue(value.value().doubleValue());
        l.setUnit(ul);
        return l;
    }

   /**
    * FIXME: this should likely take a default so that locations which don't
    * want an exception can have
    *
    * log.warn("Using new PositiveFloat(1.0)!", e); return new
    * PositiveFloat(1.0);
    *
    * or similar.
    */
   public static ome.units.quantity.${name} convert${name}(${name} t) {
       if (t == null) {
           return null;
       }

       Double v = t.getValue();
       String u = t.getUnit().toString();
       ome.xml.model.enums.Units${name} units = make${name}UnitXML(u);
       ome.units.unit.Unit<ome.units.quantity.${name}> units2 =
               ome.xml.model.enums.handlers.Units${name}EnumHandler
                       .getBaseUnit(units);

       return new ome.units.quantity.${name}(v, units2);
   }

   public static ${name} convert${name}(${name} value, Unit<ome.units.quantity.${name}> ul) {
       return convert${name}(value, ul.getSymbol());
   }

   public static ${name} convert${name}(${name} value, String target) {
       String source = value.getUnit().toString();
       if (target.equals(source)) {
           return value;
       }
       throw new RuntimeException(String.format(
               "%d %s cannot be converted to %s", value.getValue(), source));
   }

{% end %}

}

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

package omero.model;

import ome.model.ModelBased;
import ome.units.unit.Unit;
import ome.util.Filterable;
import ome.util.ModelMapper;
import ome.util.ReverseModelMapper;
import ome.xml.model.enums.EnumerationException;

import omero.model.enums.Units${name};

/**
 * Blitz wrapper around the {@link ome.model.units.${name}} class.
 * Like {@link Details} and {@link Permissions}, this object
 * is embedded into other objects and does not have a full life
 * cycle of its own.
 *
 * @author Josh Moore, josh at glencoesoftware.com
 */
public class ${name}I extends ${name} implements ModelBased {

    private static final long serialVersionUID = 1L;

    public static final Ice.ObjectFactory makeFactory(final omero.client client) {

        return new Ice.ObjectFactory() {

            public Ice.Object create(String arg0) {
                return new ${name}I();
            }

            public void destroy() {
                // no-op
            }

        };
    };

    //
    // CONVERSIONS
    //

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
       // Use the code/symbol-mapping in the ome.model.enums files
       // to convert to the specification value.
       String u = ome.model.enums.Units${name}.valueOf(
               t.getUnit().toString()).getSymbol();
       ome.xml.model.enums.Units${name} units = make${name}UnitXML(u);
       ome.units.unit.Unit<ome.units.quantity.${name}> units2 =
               ome.xml.model.enums.handlers.Units${name}EnumHandler
                       .getBaseUnit(units);

       return new ome.units.quantity.${name}(v, units2);
   }


    //
    // REGULAR ICE CLASS
    //

    public final static Ice.ObjectFactory Factory = makeFactory(null);

    public ${name}I() {
        super();
    }

    public ${name}I(double d, Units${name} unit) {
        super();
        this.setUnit(unit);
        this.setValue(d);
    }

    public ${name}I(double d,
            Unit<ome.units.quantity.${name}> unit) {
        this(d, ome.model.enums.Units${name}.bySymbol(unit.getSymbol()));
    }

   /**
    * Copy constructor that converts the given {@link omero.model.${name}}
    * based on the given ome-xml enum
    */
   public ${name}I(${name} value, Unit<ome.units.quantity.${name}> ul) {
       this(value,
            ome.model.enums.Units${name}.bySymbol(ul.getSymbol()).toString());
   }

   public ${name}I(double d, ome.model.enums.Units${name} ul) {
        this(d, Units${name}.valueOf(ul.toString()));
    }

   /**
    * Copy constructor that converts the given {@link omero.model.${name}}
    * based on the given enum string.
    *
    * @param target String representation of the CODE enum
    */
    public ${name}I(${name} value, String target) {
       String source = value.getUnit().toString();
       if (!target.equals(source)) {
            throw new RuntimeException(String.format(
               "%f %s cannot be converted to %s",
               value.getValue(), value.getUnit(), target));
       }
       setValue(value.getValue());
       setUnit(value.getUnit());
    }

    /**
     * Convert a Bio-Formats {@link Length} to an OMERO Length.
     */
    public ${name}I(ome.units.quantity.${name} value) {
        ome.model.enums.Units${name} internal =
            ome.model.enums.Units${name}.bySymbol(value.unit().getSymbol());
        Units${name} ul = Units${name}.valueOf(internal.toString());
        setValue(value.value().doubleValue());
        setUnit(ul);
    }

    public double getValue(Ice.Current current) {
        return this.value;
    }

    public void setValue(double value , Ice.Current current) {
        this.value = value;
    }

    public Units${name} getUnit(Ice.Current current) {
        return this.unit;
    }

    public void setUnit(Units${name} unit, Ice.Current current) {
        this.unit = unit;
    }

    public ${name} copy(Ice.Current ignore) {
        ${name}I copy = new ${name}I();
        copy.setValue(getValue());
        copy.setUnit(getUnit());
        return copy;
    }

    @Override
    public void copyObject(Filterable model, ModelMapper mapper) {
        if (model instanceof ome.model.units.${name}) {
            ome.model.units.${name} t = (ome.model.units.${name}) model;
            this.value = t.getValue();
            this.unit = Units${name}.valueOf(t.getUnit().toString());
        } else {
            throw new IllegalArgumentException(
              "${name} cannot copy from " +
              (model==null ? "null" : model.getClass().getName()));
        }
    }

    @Override
    public Filterable fillObject(ReverseModelMapper mapper) {
        ome.model.enums.Units${name} ut = ome.model.enums.Units${name}.valueOf(getUnit().toString());
        ome.model.units.${name} t = new ome.model.units.${name}(getValue(), ut);
        return t;
    }

}

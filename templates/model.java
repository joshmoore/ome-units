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
def example(name):
    if name == "ElectricPotential":
        return ("detectorSettings", "volatage")
    elif name == "Frequency":
        return ("detectorSettings", "readOutRate")
    elif name == "Length":
        return ("pixels", "physicalSizeX")
    elif name == "Power":
        return ("lightSource", "power")
    elif name == "Pressure":
        return ("imagingEnvironment", "pressure")
    elif name == "Temperature":
        return ("imagingEnvironment", "temperature")
    elif name == "Time":
        return ("planeInfo", "exposureTime")
    else:
        raise Exception("Unknown: %s" % name)

def dotexample(name):
    return ".".join(example(name))

def getexample(name):
    t, f = example(name)
    return "%s.get%s()" % (t, f.capitalize())
%}
package ome.model.units;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;

import ome.units.unit.Unit;
import ome.xml.model.enums.EnumerationException;

import ome.model.enums.Units${name};
import ome.util.Filter;
import ome.util.Filterable;

import org.hibernate.annotations.Parameter;
import org.hibernate.annotations.Type;

/**
 * class storing both a ${name} and a unit for that ${name}
 * (e.g. m, in, ly, etc.) encapsulated in a {@link Units${name}} instance. As
 * also described in the remoting definition (.ice) for ${name}, this is an
 * embedded class meaning that the columns here do not appear in their own
 * table but exist directly on the containing object. Like Details and
 * Permissions, instances do not contain long identifiers and cannot be
 * persisted on their own.
 */
@Embeddable
public class ${name} implements Serializable, Filterable, ome.model.units.Unit {

    private static final long serialVersionUID = 1L;

    public final static String VALUE = "ome.model.units.${name}_value";

    public final static String UNIT = "ome.model.units.${name}_unit";

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
        String u = t.getUnit().getSymbol();
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
        String source = value.getUnit().getSymbol();
        if (target.equals(source)) {
            return value;
        }
        throw new RuntimeException(String.format(
                "%f %s cannot be converted to %s",
                value.getValue(), value.getUnit().getSymbol(), source));
    }

    // ~ Constructors
    // =========================================================================

    /**
     * no-arg constructor to keep Hibernate happy.
     */
    @Deprecated
    public ${name}() {
        // no-op
    }

    public ${name}(double d, String u) {
        this.value = d;
        this.unit = Units${name}.valueOf(u);
    }

    public ${name}(double d, Units${name} u) {
        this.value = d;
        this.unit = u;
    }

    public ${name}(double d,
            Unit<ome.units.quantity.${name}> unit) {
        this(d, Units${name}.bySymbol(unit.getSymbol()));
    }

    public ${name}(ome.units.quantity.${name} value) {
        this(value.value().doubleValue(),
            Units${name}.bySymbol(value.unit().getSymbol()));
    }

    // ~ Fields
    // =========================================================================

    /**
     * positive float representation of the ${name} represented by this
     * field.
     */
    private double value;

    /**
     * representation of the units which should be considering when
     * producing a representation of the {@link #value} field.
     */
    private Units${name} unit = null;

    // ~ Property accessors : used primarily by Hibernate
    // =========================================================================

    /**
     * value of this unit-field. It will be persisted to a column with the same
     * name as the containing field. For example, ${getexample(name)}
     * which is of type {@link ${name}} will be stored in a column "${example(name)}".
     **/
    @Column(name = "value", nullable = false)
    public double getValue() {
        return this.value;
    }

    /**
     * Many-to-one field ome.model.units.${name}.unit (ome.model.enums.Units${name}).
     * These values are stored in a column suffixed by "Unit". Whereas {@link #value}
     * for physicalSizeX will be stored as "${dotexample(name)}", the unit enum
     * will be stored as "${dotexample(name)}Unit".
     */
    @javax.persistence.Column(name="unit", nullable=false,
        unique=false, insertable=true, updatable=true)
    @Type(type="ome.model.units.GenericEnumType",
          parameters=@Parameter(name="unit", value="${name.upper()}"))
    public Units${name} getUnit() {
        return this.unit;
    }

    public void setValue(double value) {
        this.value = value;
    }

    public void setUnit(Units${name} unit) {
        this.unit = unit;
    }

    @Override
    public boolean acceptFilter(Filter filter) {
        this.unit = (Units${name}) filter.filter(UNIT, unit);
        this.value = (Double) filter.filter(VALUE,  value);
        return true;
    }

    // ~ Java overrides
    // =========================================================================

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((unit == null) ? 0 : unit.hashCode());
        long temp;
        temp = Double.doubleToLongBits(value);
        result = prime * result + (int) (temp ^ (temp >>> 32));
        return result;
    }

    @Override
    public String toString() {
        return "${name}(" + value + " " + unit + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        ${name} other = (${name}) obj;
        if (unit != other.unit)
            return false;
        if (Double.doubleToLongBits(value) != Double
                .doubleToLongBits(other.value))
            return false;
        return true;
    }

}

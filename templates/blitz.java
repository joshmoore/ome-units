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
import ome.util.Filterable;
import ome.util.ModelMapper;
import ome.util.ReverseModelMapper;

import omero.model.enums.Units${name};

/**
 * Blitz wrapper around the {@link ome.model.util.${name}} class.
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

    public final static Ice.ObjectFactory Factory = makeFactory(null);

    public ${name}I() {
        super();
    }

    public ${name}I(double d, Units${name} unit) {
        super();
        this.setUnit(unit);
        this.setValue(d);
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
        ome.model.units.${name} t = new ome.model.units.${name}();
        t.setValue(getValue());
        t.setUnit(ut);
        return t;
    }

}

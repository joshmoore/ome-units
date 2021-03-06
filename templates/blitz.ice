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
%}

#ifndef CLASS_${name.upper()}
#define CLASS_${name.upper()}

#include <omero/model/Units.ice>

module omero {

    module model {

      /**
       * Unit of ${name} which is used through the model. This is not
       * an [omero::model::IObject] implementation and as such does
       * not have an ID value. Instead, the entire object is embedded
       * into the containing class, so that the value and unit rows
       * can be found on the table itself (e.g. ${dotexample(name)}
       * and ${dotexample(name)}Unit).
       **/
    ["protected"] class ${name}
    {

      /**
       * PositiveFloat value
       */
      double value;

      omero::model::enums::Units${name} unit;

      /**
       * Actual value for this unit-based field. The interpretation of
       * the value is only possible along with the [omero::model::enums::Units${name}]
       * enum.
       **/
      double getValue();

      void setValue(double value);

      /**
       * [omero::model::enums::Units${name}] instance which is an [omero::model::IObject]
       * meaning that its ID is sufficient for identifying equality.
       **/
      omero::model::enums::Units${name} getUnit();

      void setUnit(omero::model::enums::Units${name} unit);

      /**
       * Returns the possibly unicode representation of the "unit"
       * value for display.
       **/
      string getSymbol();

      ${name} copy();

    };
  };
};
#endif

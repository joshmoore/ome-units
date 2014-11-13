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

#include <omero/model/${name}I.h>

::Ice::Object* IceInternal::upCast(::omero::model::${name}I* t) { return t; }

namespace omero {

    namespace model {

        ${name}I::~${name}I() {}

        ${name}I::${name}I() : ${name}() {
        }

        Ice::Double ${name}I::getValue(const Ice::Current& /* current */) {
            return value;
        }

        void ${name}I::setValue(Ice::Double _value, const Ice::Current& /* current */) {
            value = _value;
        }

        omero::model::enums::Units${name} ${name}I::getUnit(const Ice::Current& /* current */) {
            return unit;
        }

        void ${name}I::setUnit(omero::model::enums::Units${name} _unit, const Ice::Current& /* current */) {
            unit = _unit;
        }

        ${name}Ptr ${name}I::copy(const Ice::Current& /* current */) {
            ${name}Ptr copy = new ${name}I();
            copy->setValue(getValue());
            copy->setUnit(getUnit());
            return copy;
        }
    }
}

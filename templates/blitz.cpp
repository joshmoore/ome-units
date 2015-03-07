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
#include <omero/ClientErrors.h>

::Ice::Object* IceInternal::upCast(::omero::model::${name}I* t) { return t; }

using namespace omero::conversions;

typedef omero::conversion_types::ConversionPtr ConversionPtr;
typedef omero::model::enums::Units${name} Units${name};

namespace omero {

    namespace model {

{% for cfrom in sorted(equations) %}\
        static std::map<Units${name}, ConversionPtr> createMap${cfrom}() {
            std::map<Units${name}, ConversionPtr> c;
{% for cto, equation in sorted(equations.get(cfrom, {}).items()) %}\
{% if cfrom != cto %}\
            c[enums::${cto}] = ${equation};
{% end %}\
{% end %}\
            return c;
        }

{% end %}\
        static std::map<Units${name},
            std::map<Units${name}, ConversionPtr> > makeConversions() {
            std::map<Units${name}, std::map<Units${name}, ConversionPtr> > c;
{% for cfrom in sorted(equations) %}\
            c[enums::${cfrom}] = createMap${cfrom}();
{% end %}\
            return c;
        }

        static std::map<Units${name}, std::string> makeSymbols(){
            std::map<Units${name}, std::string> s;
{% for x in sorted(items) %}\
            s[enums::${x.CODE}] = "${x.SYMBOL}";
{% end %}\
            return s;
        }

        std::map<Units${name},
            std::map<Units${name}, ConversionPtr> > ${name}I::CONVERSIONS = makeConversions();

        std::map<Units${name}, std::string> ${name}I::SYMBOLS = makeSymbols();

        ${name}I::~${name}I() {}

        ${name}I::${name}I() : ${name}() {
        }

        ${name}I::${name}I(const ${name}Ptr& value, const Units${name}& target) : ${name}() {
            double orig = value->getValue();
            Units${name} source = value->getUnit();
            if (target == source) {
                // No conversion needed
                setValue(orig);
                setUnit(target);
            } else {
                ConversionPtr conversion = CONVERSIONS[target][source];
                if (!conversion) {
                    std::stringstream ss;
                    ss << orig << " " << source;
                    ss << "cannot be converted to " << target;
                    throw omero::ClientError(__FILE__, __LINE__, ss.str().c_str());
                }
                double converted = conversion->convert(orig);
                setValue(converted);
                setUnit(target);
            }
        }

        Ice::Double ${name}I::getValue(const Ice::Current& /* current */) {
            return value;
        }

        void ${name}I::setValue(Ice::Double _value, const Ice::Current& /* current */) {
            value = _value;
        }

        Units${name} ${name}I::getUnit(const Ice::Current& /* current */) {
            return unit;
        }

        void ${name}I::setUnit(Units${name} _unit, const Ice::Current& /* current */) {
            unit = _unit;
        }

        std::string ${name}I::getSymbol(const Ice::Current& /* current */) {
            return SYMBOLS[unit];
        }

        ${name}Ptr ${name}I::copy(const Ice::Current& /* current */) {
            ${name}Ptr copy = new ${name}I();
            copy->setValue(getValue());
            copy->setUnit(getUnit());
            return copy;
        }
    }
}

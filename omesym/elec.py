#!/usr/bin/env python

from base import add_si
from base import print_conversions

from sympy.physics.units import centi
from sympy.physics.units import deci
from sympy.physics.units import kilo
from sympy.physics.units import mega
from sympy.physics.units import milli

from sympy import symbols as symbols
from sympy import Eq
from sympy import tan


NAME = "ELECTRICPOTENTIAL"

v = symbols("v")

equations = [
]

units = {
    v: "VOLT",
}

add_si(v, "VOLT", units, equations)

if __name__ == "__main__":
    import sys
    print_conversions(sys.modules[__name__])

#!/usr/bin/env python

from base import add_si
from base import print_conversions

from sympy import symbols as symbols
from sympy import Eq
from sympy import tan


NAME = "FREQUENCY"

hz = symbols("hz")
dummy = symbols("dummy")

equations = [
]

units = {
    hz: "HERTZ",
}

add_si(hz, "HERTZ", units, equations)

if __name__ == "__main__":
    import sys
    print_conversions(sys.modules[__name__])

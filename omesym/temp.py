#!/usr/bin/env python

from sympy import symbols as symbols
from sympy import Eq

NAME = "TEMPERATURE"

k, c, f, r = symbols("k c f r")

equations = (
    Eq(f, 9 * c / 5 + 32),
    Eq(f, r - 459.67),
    Eq(c, k - 273.15),
)

units = {
    k: "KELVIN",
    c: "CELSIUS",
    f: "FAHRENHEIT",
    r: "RANKINE",
}

if __name__ == "__main__":
    import sys
    from base import print_conversions
    print_conversions(sys.modules[__name__])

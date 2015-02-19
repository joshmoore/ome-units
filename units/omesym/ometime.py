#!/usr/bin/env python

from base import print_table
from sympy import symbols as symbols
from sympy import Eq
from sympy import pi

s, m, h, d = symbols("s m h d")

equations = (
    Eq(m, s * 60),
    Eq(h, m * 60),
    Eq(d, h * 24),
)

units = {
    s: "S",
    m: "m",
    h: "h",
    d: "d",
}

print_table(units, equations)

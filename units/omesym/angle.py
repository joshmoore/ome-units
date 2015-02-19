#!/usr/bin/env python

from base import print_table
from sympy import symbols as symbols
from sympy import Eq
from sympy import pi

r, d, g = symbols("r d g")

equations = (
    Eq(d, r / pi * 180),
    Eq(g, r / pi * 200),
)

units = {
    r: "R",
    d: "D",
    g: "G",
}

print_table(units, equations)

#!/usr/bin/env python

from base import print_table
from sympy import symbols as symbols
from sympy import Eq

k, c, f, r = symbols("k c f r")

equations = (
    Eq(c, k + 273.15),
    Eq(r, k * 5 / 9),
    Eq(f, r + 459.67),
)

units = {
    k: "K",
    c: "C",
    f: "F",
    r: "R",
}

print_table(units, equations)

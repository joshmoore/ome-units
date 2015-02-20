#!/usr/bin/env python

from sympy import symbols as symbols
from sympy import Eq
from sympy import pi

NAME = "ANGLE"

r, d, g = symbols("r d g")

equations = (
    Eq(d, r / pi * 180),
    Eq(g, r / pi * 200),
)

units = {
    r: "RADIAN",
    d: "DEGREE",
    g: "GRADIAN",
}

#!/usr/bin/env python

from base import add_si

from sympy import symbols as symbols
from sympy import Eq

NAME = "TIME"

s, m, h, d = symbols("s m h d")

equations = [
    Eq(m, s * 60),
    Eq(h, m * 60),
    Eq(d, h * 24),
]

units = {
    s: "SECOND",
    m: "MINUTE",
    h: "HOUR",
    d: "DAY",
}

add_si(s, "SECOND", units, equations)

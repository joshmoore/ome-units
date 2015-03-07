#!/usr/bin/env python

from base import add_si

from sympy import symbols as symbols
from sympy import Eq

NAME = "TIME"

s, m, h, d = symbols("s m h d")

equations = [
    Eq(s, m * 60),
    Eq(m, h * 60),
    Eq(h, d * 24),
]

units = {
    s: "SECOND",
    m: "MINUTE",
    h: "HOUR",
    d: "DAY",
}

add_si(s, "SECOND", units, equations)

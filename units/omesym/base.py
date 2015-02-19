#!/usr/bin/env python

from sympy import solve


def print_table(units, equations):
    sz = len(units.keys())
    fmt = "%16s\t" * (sz+1)
    print fmt % tuple(["."] + units.keys())
    for source in units.keys():
        data = [source]
        x = solve(equations, exclude=[source],
                  map=True,
                  rational=True)
        for target in units.keys():
            if source == target:
                data.append(" ")
            else:
                data.append(x[target])
        data = tuple(data)
        print fmt % data

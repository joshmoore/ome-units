#!/usr/bin/env python

from sympy import Eq
from sympy import solve
from sympy import Symbol

import sympy.physics.unitsystems.prefixes as sp


def for_each():
    for name, prefix in sp.PREFIXES.items():
        yield name, prefix.name, prefix.factor


def add_si(key, value, units, equations):
    for viz, sym, factor in for_each():
        x = "%s%s" % (sym, key)
        s = Symbol(x)
        units[s] = sym.upper() + value
        eq = Eq(s, factor * key)
        equations.append(eq)


def solve_for(equations, source):
    try:
        x = solve(
            equations,
            exclude=[source],
            map=True,
            rational=True)
        if isinstance(x, list):
            return x[0]
        else:
            return x
    except KeyboardInterrupt:
        import sys
        sys.exit(1)


def print_table(units, equations):
    sz = len(units.keys())
    fmt = "%16s\t" * (sz+1)
    print fmt % tuple(["."] + units.keys())
    for source in units.keys():
        data = [source]
        x = solve_for(equations, source)
        for target in units.keys():
            if source == target:
                data.append(" ")
            else:
                data.append(x[target])
        data = tuple(data)
        print fmt % data


def gen_conv(units, equations):
    for source in units.keys():
        x = solve_for(equations, source)
        for target in units.keys():
            if source == target:
                continue
            elif target not in x:
                continue
            yield units[source], units[target], x[target]


def module_conversions(module):
    for x in gen_conv(module.units, module.equations):
        yield x

def print_conversions(*modules):
    for mod in modules:
        for x in module_conversions(mod):
            print mod.NAME + ":%s:%s:%s" % x

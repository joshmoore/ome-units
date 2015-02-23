#!/usr/bin/env python

from sympy import Eq
from sympy import solve
from sympy import Symbol

from sympy.core.expr import Expr
from sympy.core.numbers import Integer
from sympy.core.numbers import Pi
from sympy.core.numbers import Rational
from sympy.core.symbol import Symbol

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
        if units[source] in ("REFERENCEFRAME", "PIXEL"):
            # HACK: to do this properly it's
            # likely necessary to check the
            # resulting equations for the
            # source variable.
            continue
        x = solve_for(equations, source)
        for target in units.keys():
            if source == target:
                continue
            elif target not in x:
                continue
            eqn = x[target]
            to_check = [eqn.args]
            for chk in to_check:
                for arg in chk:
                    # Assume top-level is Add or Mul
                    if isinstance(arg, (Integer, Pi, Rational)):
                        continue
                    elif isinstance(arg, Symbol):
                        if source == arg:
                            continue
                    elif isinstance(arg, Expr):
                        to_check.append(arg.args)
                        continue
                    raise Exception(
                        "%s:%s -> %s Found %s (%s)\n%s" % (
                            source, target, eqn, arg, type(arg),
                            "\n".join([str(x) for x in x.items()])
                        )
                    )
            yield units[source], units[target], eqn


def module_conversions(module):
    for x in gen_conv(module.units, module.equations):
        yield x

def print_conversions(*modules):
    for mod in modules:
        for x in module_conversions(mod):
            print mod.NAME + ":%s:%s:%s" % x

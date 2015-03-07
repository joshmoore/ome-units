#!/usr/bin/env python

from argparse import ArgumentParser

from base import print_conversions
from base import print_python

import os

import angle
import elec
import freq
import length
import power
import pressure
import temp
import _time

ALL = (
        angle, elec, freq, length,
        pressure, power, temp, _time
      )

LOOKUP = dict()
for e in ALL:
    LOOKUP[e.NAME] = e


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--load",
                        action="store_true")
    parser.add_argument("--type")
    parser.add_argument("--python",
                        action="store_true")
    parser.add_argument("--plain",
                        action="store_true")
    ns = parser.parse_args()
    which = None
    if ns.type:
        which = (LOOKUP[ns.type],)
    else:
        which = ALL

    if ns.load:
        dir = os.path.dirname(__file__)
        efile = os.path.join(dir, "equations.py")
        execfile(efile)
        for x in which:
            print x.NAME
            sources = EQUATIONS[x.NAME]
            for source, targets in sorted(sources.items()):
                for target, eqn in sorted(targets.items()):
                    print source, target, eqn
    else:
        if ns.python:
            print_python(*which)
        elif ns.plain:
            print_conversions(*which)

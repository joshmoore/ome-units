#!/usr/bin/env python

from argparse import ArgumentParser

from base import print_conversions
from base import print_python

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

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--python",
                        action="store_true")
    parser.add_argument("--plain",
                        action="store_true")
    ns = parser.parse_args()
    which = None
    if ns.type:
        for x in ALL:
            if ns.type == x.NAME:
                which = (x,)
        if not which:
            raise Exception("Unknown: %s" % ns.type)
    else:
        which = ALL

    if ns.python:
        print_python(*which)
    elif ns.plain:
        print_conversions(*which)

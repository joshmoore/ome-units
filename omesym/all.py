#!/usr/bin/env python

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

print_python(*ALL)

if False:
    print_conversions(*ALL)

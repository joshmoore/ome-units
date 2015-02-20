#!/usr/bin/env python

from base import add_si
from base import print_conversions

from sympy.physics.units import centi
from sympy.physics.units import deci
from sympy.physics.units import kilo
from sympy.physics.units import mega
from sympy.physics.units import milli

from sympy import symbols as symbols
from sympy import Eq
from sympy import tan


NAME = "PRESSURE"

pa, atm, mmhg, psi= symbols("pa atm mmhg psi")

bar, megabar, kbar, dbar, cbar, mbar = symbols(
    "bar, megabar, kbar, dbar, cbar, mbar")

torr, mtorr = symbols("torr mtorr")

equations = [
    Eq(bar, pa * 100000),
    Eq(megabar, mega * bar),
    Eq(kbar, kilo * bar),
    Eq(dbar, deci * bar),
    Eq(cbar, centi * bar),
    Eq(mbar, milli * bar),
    Eq(atm, pa * 101325),
    Eq(torr, atm / 760),
    Eq(mtorr, milli * torr),
    Eq(mmhg, pa * 133.322387415),
    Eq(psi, pa * 6894.75729316836142),  # Approx.
]

units = {
    pa: "PASCAL",
    bar: "BAR",
    megabar: "MEGABAR",
    kbar: "KILOBAR",
    dbar: "DECIBAR",
    cbar: "CENTIBAR",
    mbar: "MILLIBAR",
    atm: "ATHMOSPHERE",
    psi: "PSI",
    torr: "TORR",
    mtorr: "MILLITORR",
    mmhg: "MMHG",
}

add_si(pa, "PASCAL", units, equations)

if __name__ == "__main__":
    import sys
    print_conversions(sys.modules[__name__])

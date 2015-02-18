# Each of the tuples below is of the form:
#
# x = ((A0, B0, A1, B1, ...), (C0, D0, C1, D1, ...))
#
# where each tuple represents a degree of a polynomial.
# The tuple itself can be used to determine the coefficients.
#
# E.g.:
#
#   A0, B0, A1, B1 = x[0]
#   C0, D0, C1, D1 = x[1]
#   f = (A0**B0 * A1**B1) + (C0**D0 * C1**D1) * X**1
#
# The reason for the multiple multipled terms is to
# allow a late-rounding way to divide, such as:
# (10**18 * 60**-1)

from math import pi

Conversions = {
  "Angle": {
    "DEGREE": {
        "DEGREE": (),  # Same
        "GRADIAN": ((0, 1), (9/10, 1)),
        "RADIAN": ((0, 1), (180/pi, 1)),

    },
    "GRADIAN": {
        "DEGREE": ((0, 1), (10/9, 1)),
        "GRADIAN": (),  # Same
        "RADIAN": ((0, 1), (200/pi, 1)),

    },
    "RADIAN": {
        "DEGREE": ((0, 1), (pi/180, 1)),
        "GRADIAN": ((0, 1), (pi/200, 1)),
        "RADIAN": (),  # Same

    },

  },
  "ElectricPotential": {
    "ATTOVOLT": {
        "ATTOVOLT": (), # Same
        "CENTIVOLT": ((0, 1), (10, -16)),
        "DECAVOLT": ((0, 1), (10, -19)),
        "DECIVOLT": ((0, 1), (10, -17)),
        "EXAVOLT": ((0, 1), (10, -36)),
        "FEMTOVOLT": ((0, 1), (10, -3)),
        "GIGAVOLT": ((0, 1), (10, -27)),
        "HECTOVOLT": ((0, 1), (10, -20)),
        "KILOVOLT": ((0, 1), (10, -21)),
        "MEGAVOLT": ((0, 1), (10, -24)),
        "MICROVOLT": ((0, 1), (10, -12)),
        "MILLIVOLT": ((0, 1), (10, -15)),
        "NANOVOLT": ((0, 1), (10, -9)),
        "PETAVOLT": ((0, 1), (10, -33)),
        "PICOVOLT": ((0, 1), (10, -6)),
        "TERAVOLT": ((0, 1), (10, -30)),
        "VOLT": ((0, 1), (10, -18)),
        "YOTTAVOLT": ((0, 1), (10, -42)),
        "YOCTOVOLT": ((0, 1), (10, 6)),
        "ZETTAVOLT": ((0, 1), (10, -39)),
        "ZEPTOVOLT": ((0, 1), (10, 3)),

    },
    "CENTIVOLT": {
        "ATTOVOLT": ((0, 1), (10, 16)),
        "CENTIVOLT": (), # Same
        "DECAVOLT": ((0, 1), (10, -3)),
        "DECIVOLT": ((0, 1), (10, -1)),
        "EXAVOLT": ((0, 1), (10, -20)),
        "FEMTOVOLT": ((0, 1), (10, 13)),
        "GIGAVOLT": ((0, 1), (10, -11)),
        "HECTOVOLT": ((0, 1), (10, -4)),
        "KILOVOLT": ((0, 1), (10, -5)),
        "MEGAVOLT": ((0, 1), (10, -8)),
        "MICROVOLT": ((0, 1), (10, 4)),
        "MILLIVOLT": ((0, 1), (10, 1)),
        "NANOVOLT": ((0, 1), (10, 7)),
        "PETAVOLT": ((0, 1), (10, -17)),
        "PICOVOLT": ((0, 1), (10, 10)),
        "TERAVOLT": ((0, 1), (10, -14)),
        "VOLT": ((0, 1), (10, -2)),
        "YOTTAVOLT": ((0, 1), (10, -26)),
        "YOCTOVOLT": ((0, 1), (10, 22)),
        "ZETTAVOLT": ((0, 1), (10, -23)),
        "ZEPTOVOLT": ((0, 1), (10, 19)),

    },
    "DECAVOLT": {
        "ATTOVOLT": ((0, 1), (10, 19)),
        "CENTIVOLT": ((0, 1), (10, 3)),
        "DECAVOLT": (), # Same
        "DECIVOLT": ((0, 1), (10, 2)),
        "EXAVOLT": ((0, 1), (10, -17)),
        "FEMTOVOLT": ((0, 1), (10, 16)),
        "GIGAVOLT": ((0, 1), (10, -8)),
        "HECTOVOLT": ((0, 1), (10, -1)),
        "KILOVOLT": ((0, 1), (10, -2)),
        "MEGAVOLT": ((0, 1), (10, -5)),
        "MICROVOLT": ((0, 1), (10, 7)),
        "MILLIVOLT": ((0, 1), (10, 4)),
        "NANOVOLT": ((0, 1), (10, 10)),
        "PETAVOLT": ((0, 1), (10, -14)),
        "PICOVOLT": ((0, 1), (10, 13)),
        "TERAVOLT": ((0, 1), (10, -11)),
        "VOLT": ((0, 1), (10, 1)),
        "YOTTAVOLT": ((0, 1), (10, -23)),
        "YOCTOVOLT": ((0, 1), (10, 25)),
        "ZETTAVOLT": ((0, 1), (10, -20)),
        "ZEPTOVOLT": ((0, 1), (10, 22)),

    },
    "DECIVOLT": {
        "ATTOVOLT": ((0, 1), (10, 17)),
        "CENTIVOLT": ((0, 1), (10, 1)),
        "DECAVOLT": ((0, 1), (10, -2)),
        "DECIVOLT": (), # Same
        "EXAVOLT": ((0, 1), (10, -19)),
        "FEMTOVOLT": ((0, 1), (10, 14)),
        "GIGAVOLT": ((0, 1), (10, -10)),
        "HECTOVOLT": ((0, 1), (10, -3)),
        "KILOVOLT": ((0, 1), (10, -4)),
        "MEGAVOLT": ((0, 1), (10, -7)),
        "MICROVOLT": ((0, 1), (10, 5)),
        "MILLIVOLT": ((0, 1), (10, 2)),
        "NANOVOLT": ((0, 1), (10, 8)),
        "PETAVOLT": ((0, 1), (10, -16)),
        "PICOVOLT": ((0, 1), (10, 11)),
        "TERAVOLT": ((0, 1), (10, -13)),
        "VOLT": ((0, 1), (10, -1)),
        "YOTTAVOLT": ((0, 1), (10, -25)),
        "YOCTOVOLT": ((0, 1), (10, 23)),
        "ZETTAVOLT": ((0, 1), (10, -22)),
        "ZEPTOVOLT": ((0, 1), (10, 20)),

    },
    "EXAVOLT": {
        "ATTOVOLT": ((0, 1), (10, 36)),
        "CENTIVOLT": ((0, 1), (10, 20)),
        "DECAVOLT": ((0, 1), (10, 17)),
        "DECIVOLT": ((0, 1), (10, 19)),
        "EXAVOLT": (), # Same
        "FEMTOVOLT": ((0, 1), (10, 33)),
        "GIGAVOLT": ((0, 1), (10, 9)),
        "HECTOVOLT": ((0, 1), (10, 16)),
        "KILOVOLT": ((0, 1), (10, 15)),
        "MEGAVOLT": ((0, 1), (10, 12)),
        "MICROVOLT": ((0, 1), (10, 24)),
        "MILLIVOLT": ((0, 1), (10, 21)),
        "NANOVOLT": ((0, 1), (10, 27)),
        "PETAVOLT": ((0, 1), (10, 3)),
        "PICOVOLT": ((0, 1), (10, 30)),
        "TERAVOLT": ((0, 1), (10, 6)),
        "VOLT": ((0, 1), (10, 18)),
        "YOTTAVOLT": ((0, 1), (10, -6)),
        "YOCTOVOLT": ((0, 1), (10, 42)),
        "ZETTAVOLT": ((0, 1), (10, -3)),
        "ZEPTOVOLT": ((0, 1), (10, 39)),

    },
    "FEMTOVOLT": {
        "ATTOVOLT": ((0, 1), (10, 3)),
        "CENTIVOLT": ((0, 1), (10, -13)),
        "DECAVOLT": ((0, 1), (10, -16)),
        "DECIVOLT": ((0, 1), (10, -14)),
        "EXAVOLT": ((0, 1), (10, -33)),
        "FEMTOVOLT": (), # Same
        "GIGAVOLT": ((0, 1), (10, -24)),
        "HECTOVOLT": ((0, 1), (10, -17)),
        "KILOVOLT": ((0, 1), (10, -18)),
        "MEGAVOLT": ((0, 1), (10, -21)),
        "MICROVOLT": ((0, 1), (10, -9)),
        "MILLIVOLT": ((0, 1), (10, -12)),
        "NANOVOLT": ((0, 1), (10, -6)),
        "PETAVOLT": ((0, 1), (10, -30)),
        "PICOVOLT": ((0, 1), (10, -3)),
        "TERAVOLT": ((0, 1), (10, -27)),
        "VOLT": ((0, 1), (10, -15)),
        "YOTTAVOLT": ((0, 1), (10, -39)),
        "YOCTOVOLT": ((0, 1), (10, 9)),
        "ZETTAVOLT": ((0, 1), (10, -36)),
        "ZEPTOVOLT": ((0, 1), (10, 6)),

    },
    "GIGAVOLT": {
        "ATTOVOLT": ((0, 1), (10, 27)),
        "CENTIVOLT": ((0, 1), (10, 11)),
        "DECAVOLT": ((0, 1), (10, 8)),
        "DECIVOLT": ((0, 1), (10, 10)),
        "EXAVOLT": ((0, 1), (10, -9)),
        "FEMTOVOLT": ((0, 1), (10, 24)),
        "GIGAVOLT": (), # Same
        "HECTOVOLT": ((0, 1), (10, 7)),
        "KILOVOLT": ((0, 1), (10, 6)),
        "MEGAVOLT": ((0, 1), (10, 3)),
        "MICROVOLT": ((0, 1), (10, 15)),
        "MILLIVOLT": ((0, 1), (10, 12)),
        "NANOVOLT": ((0, 1), (10, 18)),
        "PETAVOLT": ((0, 1), (10, -6)),
        "PICOVOLT": ((0, 1), (10, 21)),
        "TERAVOLT": ((0, 1), (10, -3)),
        "VOLT": ((0, 1), (10, 9)),
        "YOTTAVOLT": ((0, 1), (10, -15)),
        "YOCTOVOLT": ((0, 1), (10, 33)),
        "ZETTAVOLT": ((0, 1), (10, -12)),
        "ZEPTOVOLT": ((0, 1), (10, 30)),

    },
    "HECTOVOLT": {
        "ATTOVOLT": ((0, 1), (10, 20)),
        "CENTIVOLT": ((0, 1), (10, 4)),
        "DECAVOLT": ((0, 1), (10, 1)),
        "DECIVOLT": ((0, 1), (10, 3)),
        "EXAVOLT": ((0, 1), (10, -16)),
        "FEMTOVOLT": ((0, 1), (10, 17)),
        "GIGAVOLT": ((0, 1), (10, -7)),
        "HECTOVOLT": (), # Same
        "KILOVOLT": ((0, 1), (10, -1)),
        "MEGAVOLT": ((0, 1), (10, -4)),
        "MICROVOLT": ((0, 1), (10, 8)),
        "MILLIVOLT": ((0, 1), (10, 5)),
        "NANOVOLT": ((0, 1), (10, 11)),
        "PETAVOLT": ((0, 1), (10, -13)),
        "PICOVOLT": ((0, 1), (10, 14)),
        "TERAVOLT": ((0, 1), (10, -10)),
        "VOLT": ((0, 1), (10, 2)),
        "YOTTAVOLT": ((0, 1), (10, -22)),
        "YOCTOVOLT": ((0, 1), (10, 26)),
        "ZETTAVOLT": ((0, 1), (10, -19)),
        "ZEPTOVOLT": ((0, 1), (10, 23)),

    },
    "KILOVOLT": {
        "ATTOVOLT": ((0, 1), (10, 21)),
        "CENTIVOLT": ((0, 1), (10, 5)),
        "DECAVOLT": ((0, 1), (10, 2)),
        "DECIVOLT": ((0, 1), (10, 4)),
        "EXAVOLT": ((0, 1), (10, -15)),
        "FEMTOVOLT": ((0, 1), (10, 18)),
        "GIGAVOLT": ((0, 1), (10, -6)),
        "HECTOVOLT": ((0, 1), (10, 1)),
        "KILOVOLT": (), # Same
        "MEGAVOLT": ((0, 1), (10, -3)),
        "MICROVOLT": ((0, 1), (10, 9)),
        "MILLIVOLT": ((0, 1), (10, 6)),
        "NANOVOLT": ((0, 1), (10, 12)),
        "PETAVOLT": ((0, 1), (10, -12)),
        "PICOVOLT": ((0, 1), (10, 15)),
        "TERAVOLT": ((0, 1), (10, -9)),
        "VOLT": ((0, 1), (10, 3)),
        "YOTTAVOLT": ((0, 1), (10, -21)),
        "YOCTOVOLT": ((0, 1), (10, 27)),
        "ZETTAVOLT": ((0, 1), (10, -18)),
        "ZEPTOVOLT": ((0, 1), (10, 24)),

    },
    "MEGAVOLT": {
        "ATTOVOLT": ((0, 1), (10, 24)),
        "CENTIVOLT": ((0, 1), (10, 8)),
        "DECAVOLT": ((0, 1), (10, 5)),
        "DECIVOLT": ((0, 1), (10, 7)),
        "EXAVOLT": ((0, 1), (10, -12)),
        "FEMTOVOLT": ((0, 1), (10, 21)),
        "GIGAVOLT": ((0, 1), (10, -3)),
        "HECTOVOLT": ((0, 1), (10, 4)),
        "KILOVOLT": ((0, 1), (10, 3)),
        "MEGAVOLT": (), # Same
        "MICROVOLT": ((0, 1), (10, 12)),
        "MILLIVOLT": ((0, 1), (10, 9)),
        "NANOVOLT": ((0, 1), (10, 15)),
        "PETAVOLT": ((0, 1), (10, -9)),
        "PICOVOLT": ((0, 1), (10, 18)),
        "TERAVOLT": ((0, 1), (10, -6)),
        "VOLT": ((0, 1), (10, 6)),
        "YOTTAVOLT": ((0, 1), (10, -18)),
        "YOCTOVOLT": ((0, 1), (10, 30)),
        "ZETTAVOLT": ((0, 1), (10, -15)),
        "ZEPTOVOLT": ((0, 1), (10, 27)),

    },
    "MICROVOLT": {
        "ATTOVOLT": ((0, 1), (10, 12)),
        "CENTIVOLT": ((0, 1), (10, -4)),
        "DECAVOLT": ((0, 1), (10, -7)),
        "DECIVOLT": ((0, 1), (10, -5)),
        "EXAVOLT": ((0, 1), (10, -24)),
        "FEMTOVOLT": ((0, 1), (10, 9)),
        "GIGAVOLT": ((0, 1), (10, -15)),
        "HECTOVOLT": ((0, 1), (10, -8)),
        "KILOVOLT": ((0, 1), (10, -9)),
        "MEGAVOLT": ((0, 1), (10, -12)),
        "MICROVOLT": (), # Same
        "MILLIVOLT": ((0, 1), (10, -3)),
        "NANOVOLT": ((0, 1), (10, 3)),
        "PETAVOLT": ((0, 1), (10, -21)),
        "PICOVOLT": ((0, 1), (10, 6)),
        "TERAVOLT": ((0, 1), (10, -18)),
        "VOLT": ((0, 1), (10, -6)),
        "YOTTAVOLT": ((0, 1), (10, -30)),
        "YOCTOVOLT": ((0, 1), (10, 18)),
        "ZETTAVOLT": ((0, 1), (10, -27)),
        "ZEPTOVOLT": ((0, 1), (10, 15)),

    },
    "MILLIVOLT": {
        "ATTOVOLT": ((0, 1), (10, 15)),
        "CENTIVOLT": ((0, 1), (10, -1)),
        "DECAVOLT": ((0, 1), (10, -4)),
        "DECIVOLT": ((0, 1), (10, -2)),
        "EXAVOLT": ((0, 1), (10, -21)),
        "FEMTOVOLT": ((0, 1), (10, 12)),
        "GIGAVOLT": ((0, 1), (10, -12)),
        "HECTOVOLT": ((0, 1), (10, -5)),
        "KILOVOLT": ((0, 1), (10, -6)),
        "MEGAVOLT": ((0, 1), (10, -9)),
        "MICROVOLT": ((0, 1), (10, 3)),
        "MILLIVOLT": (), # Same
        "NANOVOLT": ((0, 1), (10, 6)),
        "PETAVOLT": ((0, 1), (10, -18)),
        "PICOVOLT": ((0, 1), (10, 9)),
        "TERAVOLT": ((0, 1), (10, -15)),
        "VOLT": ((0, 1), (10, -3)),
        "YOTTAVOLT": ((0, 1), (10, -27)),
        "YOCTOVOLT": ((0, 1), (10, 21)),
        "ZETTAVOLT": ((0, 1), (10, -24)),
        "ZEPTOVOLT": ((0, 1), (10, 18)),

    },
    "NANOVOLT": {
        "ATTOVOLT": ((0, 1), (10, 9)),
        "CENTIVOLT": ((0, 1), (10, -7)),
        "DECAVOLT": ((0, 1), (10, -10)),
        "DECIVOLT": ((0, 1), (10, -8)),
        "EXAVOLT": ((0, 1), (10, -27)),
        "FEMTOVOLT": ((0, 1), (10, 6)),
        "GIGAVOLT": ((0, 1), (10, -18)),
        "HECTOVOLT": ((0, 1), (10, -11)),
        "KILOVOLT": ((0, 1), (10, -12)),
        "MEGAVOLT": ((0, 1), (10, -15)),
        "MICROVOLT": ((0, 1), (10, -3)),
        "MILLIVOLT": ((0, 1), (10, -6)),
        "NANOVOLT": (), # Same
        "PETAVOLT": ((0, 1), (10, -24)),
        "PICOVOLT": ((0, 1), (10, 3)),
        "TERAVOLT": ((0, 1), (10, -21)),
        "VOLT": ((0, 1), (10, -9)),
        "YOTTAVOLT": ((0, 1), (10, -33)),
        "YOCTOVOLT": ((0, 1), (10, 15)),
        "ZETTAVOLT": ((0, 1), (10, -30)),
        "ZEPTOVOLT": ((0, 1), (10, 12)),

    },
    "PETAVOLT": {
        "ATTOVOLT": ((0, 1), (10, 33)),
        "CENTIVOLT": ((0, 1), (10, 17)),
        "DECAVOLT": ((0, 1), (10, 14)),
        "DECIVOLT": ((0, 1), (10, 16)),
        "EXAVOLT": ((0, 1), (10, -3)),
        "FEMTOVOLT": ((0, 1), (10, 30)),
        "GIGAVOLT": ((0, 1), (10, 6)),
        "HECTOVOLT": ((0, 1), (10, 13)),
        "KILOVOLT": ((0, 1), (10, 12)),
        "MEGAVOLT": ((0, 1), (10, 9)),
        "MICROVOLT": ((0, 1), (10, 21)),
        "MILLIVOLT": ((0, 1), (10, 18)),
        "NANOVOLT": ((0, 1), (10, 24)),
        "PETAVOLT": (), # Same
        "PICOVOLT": ((0, 1), (10, 27)),
        "TERAVOLT": ((0, 1), (10, 3)),
        "VOLT": ((0, 1), (10, 15)),
        "YOTTAVOLT": ((0, 1), (10, -9)),
        "YOCTOVOLT": ((0, 1), (10, 39)),
        "ZETTAVOLT": ((0, 1), (10, -6)),
        "ZEPTOVOLT": ((0, 1), (10, 36)),

    },
    "PICOVOLT": {
        "ATTOVOLT": ((0, 1), (10, 6)),
        "CENTIVOLT": ((0, 1), (10, -10)),
        "DECAVOLT": ((0, 1), (10, -13)),
        "DECIVOLT": ((0, 1), (10, -11)),
        "EXAVOLT": ((0, 1), (10, -30)),
        "FEMTOVOLT": ((0, 1), (10, 3)),
        "GIGAVOLT": ((0, 1), (10, -21)),
        "HECTOVOLT": ((0, 1), (10, -14)),
        "KILOVOLT": ((0, 1), (10, -15)),
        "MEGAVOLT": ((0, 1), (10, -18)),
        "MICROVOLT": ((0, 1), (10, -6)),
        "MILLIVOLT": ((0, 1), (10, -9)),
        "NANOVOLT": ((0, 1), (10, -3)),
        "PETAVOLT": ((0, 1), (10, -27)),
        "PICOVOLT": (), # Same
        "TERAVOLT": ((0, 1), (10, -24)),
        "VOLT": ((0, 1), (10, -12)),
        "YOTTAVOLT": ((0, 1), (10, -36)),
        "YOCTOVOLT": ((0, 1), (10, 12)),
        "ZETTAVOLT": ((0, 1), (10, -33)),
        "ZEPTOVOLT": ((0, 1), (10, 9)),

    },
    "TERAVOLT": {
        "ATTOVOLT": ((0, 1), (10, 30)),
        "CENTIVOLT": ((0, 1), (10, 14)),
        "DECAVOLT": ((0, 1), (10, 11)),
        "DECIVOLT": ((0, 1), (10, 13)),
        "EXAVOLT": ((0, 1), (10, -6)),
        "FEMTOVOLT": ((0, 1), (10, 27)),
        "GIGAVOLT": ((0, 1), (10, 3)),
        "HECTOVOLT": ((0, 1), (10, 10)),
        "KILOVOLT": ((0, 1), (10, 9)),
        "MEGAVOLT": ((0, 1), (10, 6)),
        "MICROVOLT": ((0, 1), (10, 18)),
        "MILLIVOLT": ((0, 1), (10, 15)),
        "NANOVOLT": ((0, 1), (10, 21)),
        "PETAVOLT": ((0, 1), (10, -3)),
        "PICOVOLT": ((0, 1), (10, 24)),
        "TERAVOLT": (), # Same
        "VOLT": ((0, 1), (10, 12)),
        "YOTTAVOLT": ((0, 1), (10, -12)),
        "YOCTOVOLT": ((0, 1), (10, 36)),
        "ZETTAVOLT": ((0, 1), (10, -9)),
        "ZEPTOVOLT": ((0, 1), (10, 33)),

    },
    "VOLT": {
        "ATTOVOLT": ((0, 1), (10, 18)),
        "CENTIVOLT": ((0, 1), (10, 2)),
        "DECAVOLT": ((0, 1), (10, -1)),
        "DECIVOLT": ((0, 1), (10, 1)),
        "EXAVOLT": ((0, 1), (10, -18)),
        "FEMTOVOLT": ((0, 1), (10, 15)),
        "GIGAVOLT": ((0, 1), (10, -9)),
        "HECTOVOLT": ((0, 1), (10, -2)),
        "KILOVOLT": ((0, 1), (10, -3)),
        "MEGAVOLT": ((0, 1), (10, -6)),
        "MICROVOLT": ((0, 1), (10, 6)),
        "MILLIVOLT": ((0, 1), (10, 3)),
        "NANOVOLT": ((0, 1), (10, 9)),
        "PETAVOLT": ((0, 1), (10, -15)),
        "PICOVOLT": ((0, 1), (10, 12)),
        "TERAVOLT": ((0, 1), (10, -12)),
        "VOLT": (), # Same
        "YOTTAVOLT": ((0, 1), (10, -24)),
        "YOCTOVOLT": ((0, 1), (10, 24)),
        "ZETTAVOLT": ((0, 1), (10, -21)),
        "ZEPTOVOLT": ((0, 1), (10, 21)),

    },
    "YOTTAVOLT": {
        "ATTOVOLT": ((0, 1), (10, 42)),
        "CENTIVOLT": ((0, 1), (10, 26)),
        "DECAVOLT": ((0, 1), (10, 23)),
        "DECIVOLT": ((0, 1), (10, 25)),
        "EXAVOLT": ((0, 1), (10, 6)),
        "FEMTOVOLT": ((0, 1), (10, 39)),
        "GIGAVOLT": ((0, 1), (10, 15)),
        "HECTOVOLT": ((0, 1), (10, 22)),
        "KILOVOLT": ((0, 1), (10, 21)),
        "MEGAVOLT": ((0, 1), (10, 18)),
        "MICROVOLT": ((0, 1), (10, 30)),
        "MILLIVOLT": ((0, 1), (10, 27)),
        "NANOVOLT": ((0, 1), (10, 33)),
        "PETAVOLT": ((0, 1), (10, 9)),
        "PICOVOLT": ((0, 1), (10, 36)),
        "TERAVOLT": ((0, 1), (10, 12)),
        "VOLT": ((0, 1), (10, 24)),
        "YOTTAVOLT": (), # Same
        "YOCTOVOLT": ((0, 1), (10, 48)),
        "ZETTAVOLT": ((0, 1), (10, 3)),
        "ZEPTOVOLT": ((0, 1), (10, 45)),

    },
    "YOCTOVOLT": {
        "ATTOVOLT": ((0, 1), (10, -6)),
        "CENTIVOLT": ((0, 1), (10, -22)),
        "DECAVOLT": ((0, 1), (10, -25)),
        "DECIVOLT": ((0, 1), (10, -23)),
        "EXAVOLT": ((0, 1), (10, -42)),
        "FEMTOVOLT": ((0, 1), (10, -9)),
        "GIGAVOLT": ((0, 1), (10, -33)),
        "HECTOVOLT": ((0, 1), (10, -26)),
        "KILOVOLT": ((0, 1), (10, -27)),
        "MEGAVOLT": ((0, 1), (10, -30)),
        "MICROVOLT": ((0, 1), (10, -18)),
        "MILLIVOLT": ((0, 1), (10, -21)),
        "NANOVOLT": ((0, 1), (10, -15)),
        "PETAVOLT": ((0, 1), (10, -39)),
        "PICOVOLT": ((0, 1), (10, -12)),
        "TERAVOLT": ((0, 1), (10, -36)),
        "VOLT": ((0, 1), (10, -24)),
        "YOTTAVOLT": ((0, 1), (10, -48)),
        "YOCTOVOLT": (), # Same
        "ZETTAVOLT": ((0, 1), (10, -45)),
        "ZEPTOVOLT": ((0, 1), (10, -3)),

    },
    "ZETTAVOLT": {
        "ATTOVOLT": ((0, 1), (10, 39)),
        "CENTIVOLT": ((0, 1), (10, 23)),
        "DECAVOLT": ((0, 1), (10, 20)),
        "DECIVOLT": ((0, 1), (10, 22)),
        "EXAVOLT": ((0, 1), (10, 3)),
        "FEMTOVOLT": ((0, 1), (10, 36)),
        "GIGAVOLT": ((0, 1), (10, 12)),
        "HECTOVOLT": ((0, 1), (10, 19)),
        "KILOVOLT": ((0, 1), (10, 18)),
        "MEGAVOLT": ((0, 1), (10, 15)),
        "MICROVOLT": ((0, 1), (10, 27)),
        "MILLIVOLT": ((0, 1), (10, 24)),
        "NANOVOLT": ((0, 1), (10, 30)),
        "PETAVOLT": ((0, 1), (10, 6)),
        "PICOVOLT": ((0, 1), (10, 33)),
        "TERAVOLT": ((0, 1), (10, 9)),
        "VOLT": ((0, 1), (10, 21)),
        "YOTTAVOLT": ((0, 1), (10, -3)),
        "YOCTOVOLT": ((0, 1), (10, 45)),
        "ZETTAVOLT": (), # Same
        "ZEPTOVOLT": ((0, 1), (10, 42)),

    },
    "ZEPTOVOLT": {
        "ATTOVOLT": ((0, 1), (10, -3)),
        "CENTIVOLT": ((0, 1), (10, -19)),
        "DECAVOLT": ((0, 1), (10, -22)),
        "DECIVOLT": ((0, 1), (10, -20)),
        "EXAVOLT": ((0, 1), (10, -39)),
        "FEMTOVOLT": ((0, 1), (10, -6)),
        "GIGAVOLT": ((0, 1), (10, -30)),
        "HECTOVOLT": ((0, 1), (10, -23)),
        "KILOVOLT": ((0, 1), (10, -24)),
        "MEGAVOLT": ((0, 1), (10, -27)),
        "MICROVOLT": ((0, 1), (10, -15)),
        "MILLIVOLT": ((0, 1), (10, -18)),
        "NANOVOLT": ((0, 1), (10, -12)),
        "PETAVOLT": ((0, 1), (10, -36)),
        "PICOVOLT": ((0, 1), (10, -9)),
        "TERAVOLT": ((0, 1), (10, -33)),
        "VOLT": ((0, 1), (10, -21)),
        "YOTTAVOLT": ((0, 1), (10, -45)),
        "YOCTOVOLT": ((0, 1), (10, 3)),
        "ZETTAVOLT": ((0, 1), (10, -42)),
        "ZEPTOVOLT": (), # Same

    },

  },
  "Frequency": {
    "ATTOHERTZ": {
        "ATTOHERTZ": (), # Same
        "CENTIHERTZ": ((0, 1), (10, -16)),
        "DECAHERTZ": ((0, 1), (10, -19)),
        "DECIHERTZ": ((0, 1), (10, -17)),
        "EXAHERTZ": ((0, 1), (10, -36)),
        "FEMTOHERTZ": ((0, 1), (10, -3)),
        "GIGAHERTZ": ((0, 1), (10, -27)),
        "HECTOHERTZ": ((0, 1), (10, -20)),
        "HERTZ": ((0, 1), (10, -18)),
        "KILOHERTZ": ((0, 1), (10, -21)),
        "MEGAHERTZ": ((0, 1), (10, -24)),
        "MILLIHERTZ": ((0, 1), (10, -15)),
        "MICROHERTZ": ((0, 1), (10, -12)),
        "NANOHERTZ": ((0, 1), (10, -9)),
        "PETAHERTZ": ((0, 1), (10, -33)),
        "PICOHERTZ": ((0, 1), (10, -6)),
        "TERAHERTZ": ((0, 1), (10, -30)),
        "YOCTOHERTZ": ((0, 1), (10, 6)),
        "YOTTAHERTZ": ((0, 1), (10, -42)),
        "ZETTAHERTZ": ((0, 1), (10, -39)),
        "ZEPTOHERTZ": ((0, 1), (10, 3)),

    },
    "CENTIHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 16)),
        "CENTIHERTZ": (), # Same
        "DECAHERTZ": ((0, 1), (10, -3)),
        "DECIHERTZ": ((0, 1), (10, -1)),
        "EXAHERTZ": ((0, 1), (10, -20)),
        "FEMTOHERTZ": ((0, 1), (10, 13)),
        "GIGAHERTZ": ((0, 1), (10, -11)),
        "HECTOHERTZ": ((0, 1), (10, -4)),
        "HERTZ": ((0, 1), (10, -2)),
        "KILOHERTZ": ((0, 1), (10, -5)),
        "MEGAHERTZ": ((0, 1), (10, -8)),
        "MILLIHERTZ": ((0, 1), (10, 1)),
        "MICROHERTZ": ((0, 1), (10, 4)),
        "NANOHERTZ": ((0, 1), (10, 7)),
        "PETAHERTZ": ((0, 1), (10, -17)),
        "PICOHERTZ": ((0, 1), (10, 10)),
        "TERAHERTZ": ((0, 1), (10, -14)),
        "YOCTOHERTZ": ((0, 1), (10, 22)),
        "YOTTAHERTZ": ((0, 1), (10, -26)),
        "ZETTAHERTZ": ((0, 1), (10, -23)),
        "ZEPTOHERTZ": ((0, 1), (10, 19)),

    },
    "DECAHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 19)),
        "CENTIHERTZ": ((0, 1), (10, 3)),
        "DECAHERTZ": (), # Same
        "DECIHERTZ": ((0, 1), (10, 2)),
        "EXAHERTZ": ((0, 1), (10, -17)),
        "FEMTOHERTZ": ((0, 1), (10, 16)),
        "GIGAHERTZ": ((0, 1), (10, -8)),
        "HECTOHERTZ": ((0, 1), (10, -1)),
        "HERTZ": ((0, 1), (10, 1)),
        "KILOHERTZ": ((0, 1), (10, -2)),
        "MEGAHERTZ": ((0, 1), (10, -5)),
        "MILLIHERTZ": ((0, 1), (10, 4)),
        "MICROHERTZ": ((0, 1), (10, 7)),
        "NANOHERTZ": ((0, 1), (10, 10)),
        "PETAHERTZ": ((0, 1), (10, -14)),
        "PICOHERTZ": ((0, 1), (10, 13)),
        "TERAHERTZ": ((0, 1), (10, -11)),
        "YOCTOHERTZ": ((0, 1), (10, 25)),
        "YOTTAHERTZ": ((0, 1), (10, -23)),
        "ZETTAHERTZ": ((0, 1), (10, -20)),
        "ZEPTOHERTZ": ((0, 1), (10, 22)),

    },
    "DECIHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 17)),
        "CENTIHERTZ": ((0, 1), (10, 1)),
        "DECAHERTZ": ((0, 1), (10, -2)),
        "DECIHERTZ": (), # Same
        "EXAHERTZ": ((0, 1), (10, -19)),
        "FEMTOHERTZ": ((0, 1), (10, 14)),
        "GIGAHERTZ": ((0, 1), (10, -10)),
        "HECTOHERTZ": ((0, 1), (10, -3)),
        "HERTZ": ((0, 1), (10, -1)),
        "KILOHERTZ": ((0, 1), (10, -4)),
        "MEGAHERTZ": ((0, 1), (10, -7)),
        "MILLIHERTZ": ((0, 1), (10, 2)),
        "MICROHERTZ": ((0, 1), (10, 5)),
        "NANOHERTZ": ((0, 1), (10, 8)),
        "PETAHERTZ": ((0, 1), (10, -16)),
        "PICOHERTZ": ((0, 1), (10, 11)),
        "TERAHERTZ": ((0, 1), (10, -13)),
        "YOCTOHERTZ": ((0, 1), (10, 23)),
        "YOTTAHERTZ": ((0, 1), (10, -25)),
        "ZETTAHERTZ": ((0, 1), (10, -22)),
        "ZEPTOHERTZ": ((0, 1), (10, 20)),

    },
    "EXAHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 36)),
        "CENTIHERTZ": ((0, 1), (10, 20)),
        "DECAHERTZ": ((0, 1), (10, 17)),
        "DECIHERTZ": ((0, 1), (10, 19)),
        "EXAHERTZ": (), # Same
        "FEMTOHERTZ": ((0, 1), (10, 33)),
        "GIGAHERTZ": ((0, 1), (10, 9)),
        "HECTOHERTZ": ((0, 1), (10, 16)),
        "HERTZ": ((0, 1), (10, 18)),
        "KILOHERTZ": ((0, 1), (10, 15)),
        "MEGAHERTZ": ((0, 1), (10, 12)),
        "MILLIHERTZ": ((0, 1), (10, 21)),
        "MICROHERTZ": ((0, 1), (10, 24)),
        "NANOHERTZ": ((0, 1), (10, 27)),
        "PETAHERTZ": ((0, 1), (10, 3)),
        "PICOHERTZ": ((0, 1), (10, 30)),
        "TERAHERTZ": ((0, 1), (10, 6)),
        "YOCTOHERTZ": ((0, 1), (10, 42)),
        "YOTTAHERTZ": ((0, 1), (10, -6)),
        "ZETTAHERTZ": ((0, 1), (10, -3)),
        "ZEPTOHERTZ": ((0, 1), (10, 39)),

    },
    "FEMTOHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 3)),
        "CENTIHERTZ": ((0, 1), (10, -13)),
        "DECAHERTZ": ((0, 1), (10, -16)),
        "DECIHERTZ": ((0, 1), (10, -14)),
        "EXAHERTZ": ((0, 1), (10, -33)),
        "FEMTOHERTZ": (), # Same
        "GIGAHERTZ": ((0, 1), (10, -24)),
        "HECTOHERTZ": ((0, 1), (10, -17)),
        "HERTZ": ((0, 1), (10, -15)),
        "KILOHERTZ": ((0, 1), (10, -18)),
        "MEGAHERTZ": ((0, 1), (10, -21)),
        "MILLIHERTZ": ((0, 1), (10, -12)),
        "MICROHERTZ": ((0, 1), (10, -9)),
        "NANOHERTZ": ((0, 1), (10, -6)),
        "PETAHERTZ": ((0, 1), (10, -30)),
        "PICOHERTZ": ((0, 1), (10, -3)),
        "TERAHERTZ": ((0, 1), (10, -27)),
        "YOCTOHERTZ": ((0, 1), (10, 9)),
        "YOTTAHERTZ": ((0, 1), (10, -39)),
        "ZETTAHERTZ": ((0, 1), (10, -36)),
        "ZEPTOHERTZ": ((0, 1), (10, 6)),

    },
    "GIGAHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 27)),
        "CENTIHERTZ": ((0, 1), (10, 11)),
        "DECAHERTZ": ((0, 1), (10, 8)),
        "DECIHERTZ": ((0, 1), (10, 10)),
        "EXAHERTZ": ((0, 1), (10, -9)),
        "FEMTOHERTZ": ((0, 1), (10, 24)),
        "GIGAHERTZ": (), # Same
        "HECTOHERTZ": ((0, 1), (10, 7)),
        "HERTZ": ((0, 1), (10, 9)),
        "KILOHERTZ": ((0, 1), (10, 6)),
        "MEGAHERTZ": ((0, 1), (10, 3)),
        "MILLIHERTZ": ((0, 1), (10, 12)),
        "MICROHERTZ": ((0, 1), (10, 15)),
        "NANOHERTZ": ((0, 1), (10, 18)),
        "PETAHERTZ": ((0, 1), (10, -6)),
        "PICOHERTZ": ((0, 1), (10, 21)),
        "TERAHERTZ": ((0, 1), (10, -3)),
        "YOCTOHERTZ": ((0, 1), (10, 33)),
        "YOTTAHERTZ": ((0, 1), (10, -15)),
        "ZETTAHERTZ": ((0, 1), (10, -12)),
        "ZEPTOHERTZ": ((0, 1), (10, 30)),

    },
    "HECTOHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 20)),
        "CENTIHERTZ": ((0, 1), (10, 4)),
        "DECAHERTZ": ((0, 1), (10, 1)),
        "DECIHERTZ": ((0, 1), (10, 3)),
        "EXAHERTZ": ((0, 1), (10, -16)),
        "FEMTOHERTZ": ((0, 1), (10, 17)),
        "GIGAHERTZ": ((0, 1), (10, -7)),
        "HECTOHERTZ": (), # Same
        "HERTZ": ((0, 1), (10, 2)),
        "KILOHERTZ": ((0, 1), (10, -1)),
        "MEGAHERTZ": ((0, 1), (10, -4)),
        "MILLIHERTZ": ((0, 1), (10, 5)),
        "MICROHERTZ": ((0, 1), (10, 8)),
        "NANOHERTZ": ((0, 1), (10, 11)),
        "PETAHERTZ": ((0, 1), (10, -13)),
        "PICOHERTZ": ((0, 1), (10, 14)),
        "TERAHERTZ": ((0, 1), (10, -10)),
        "YOCTOHERTZ": ((0, 1), (10, 26)),
        "YOTTAHERTZ": ((0, 1), (10, -22)),
        "ZETTAHERTZ": ((0, 1), (10, -19)),
        "ZEPTOHERTZ": ((0, 1), (10, 23)),

    },
    "HERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 18)),
        "CENTIHERTZ": ((0, 1), (10, 2)),
        "DECAHERTZ": ((0, 1), (10, -1)),
        "DECIHERTZ": ((0, 1), (10, 1)),
        "EXAHERTZ": ((0, 1), (10, -18)),
        "FEMTOHERTZ": ((0, 1), (10, 15)),
        "GIGAHERTZ": ((0, 1), (10, -9)),
        "HECTOHERTZ": ((0, 1), (10, -2)),
        "HERTZ": (), # Same
        "KILOHERTZ": ((0, 1), (10, -3)),
        "MEGAHERTZ": ((0, 1), (10, -6)),
        "MILLIHERTZ": ((0, 1), (10, 3)),
        "MICROHERTZ": ((0, 1), (10, 6)),
        "NANOHERTZ": ((0, 1), (10, 9)),
        "PETAHERTZ": ((0, 1), (10, -15)),
        "PICOHERTZ": ((0, 1), (10, 12)),
        "TERAHERTZ": ((0, 1), (10, -12)),
        "YOCTOHERTZ": ((0, 1), (10, 24)),
        "YOTTAHERTZ": ((0, 1), (10, -24)),
        "ZETTAHERTZ": ((0, 1), (10, -21)),
        "ZEPTOHERTZ": ((0, 1), (10, 21)),

    },
    "KILOHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 21)),
        "CENTIHERTZ": ((0, 1), (10, 5)),
        "DECAHERTZ": ((0, 1), (10, 2)),
        "DECIHERTZ": ((0, 1), (10, 4)),
        "EXAHERTZ": ((0, 1), (10, -15)),
        "FEMTOHERTZ": ((0, 1), (10, 18)),
        "GIGAHERTZ": ((0, 1), (10, -6)),
        "HECTOHERTZ": ((0, 1), (10, 1)),
        "HERTZ": ((0, 1), (10, 3)),
        "KILOHERTZ": (), # Same
        "MEGAHERTZ": ((0, 1), (10, -3)),
        "MILLIHERTZ": ((0, 1), (10, 6)),
        "MICROHERTZ": ((0, 1), (10, 9)),
        "NANOHERTZ": ((0, 1), (10, 12)),
        "PETAHERTZ": ((0, 1), (10, -12)),
        "PICOHERTZ": ((0, 1), (10, 15)),
        "TERAHERTZ": ((0, 1), (10, -9)),
        "YOCTOHERTZ": ((0, 1), (10, 27)),
        "YOTTAHERTZ": ((0, 1), (10, -21)),
        "ZETTAHERTZ": ((0, 1), (10, -18)),
        "ZEPTOHERTZ": ((0, 1), (10, 24)),

    },
    "MEGAHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 24)),
        "CENTIHERTZ": ((0, 1), (10, 8)),
        "DECAHERTZ": ((0, 1), (10, 5)),
        "DECIHERTZ": ((0, 1), (10, 7)),
        "EXAHERTZ": ((0, 1), (10, -12)),
        "FEMTOHERTZ": ((0, 1), (10, 21)),
        "GIGAHERTZ": ((0, 1), (10, -3)),
        "HECTOHERTZ": ((0, 1), (10, 4)),
        "HERTZ": ((0, 1), (10, 6)),
        "KILOHERTZ": ((0, 1), (10, 3)),
        "MEGAHERTZ": (), # Same
        "MILLIHERTZ": ((0, 1), (10, 9)),
        "MICROHERTZ": ((0, 1), (10, 12)),
        "NANOHERTZ": ((0, 1), (10, 15)),
        "PETAHERTZ": ((0, 1), (10, -9)),
        "PICOHERTZ": ((0, 1), (10, 18)),
        "TERAHERTZ": ((0, 1), (10, -6)),
        "YOCTOHERTZ": ((0, 1), (10, 30)),
        "YOTTAHERTZ": ((0, 1), (10, -18)),
        "ZETTAHERTZ": ((0, 1), (10, -15)),
        "ZEPTOHERTZ": ((0, 1), (10, 27)),

    },
    "MILLIHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 15)),
        "CENTIHERTZ": ((0, 1), (10, -1)),
        "DECAHERTZ": ((0, 1), (10, -4)),
        "DECIHERTZ": ((0, 1), (10, -2)),
        "EXAHERTZ": ((0, 1), (10, -21)),
        "FEMTOHERTZ": ((0, 1), (10, 12)),
        "GIGAHERTZ": ((0, 1), (10, -12)),
        "HECTOHERTZ": ((0, 1), (10, -5)),
        "HERTZ": ((0, 1), (10, -3)),
        "KILOHERTZ": ((0, 1), (10, -6)),
        "MEGAHERTZ": ((0, 1), (10, -9)),
        "MILLIHERTZ": (), # Same
        "MICROHERTZ": ((0, 1), (10, 3)),
        "NANOHERTZ": ((0, 1), (10, 6)),
        "PETAHERTZ": ((0, 1), (10, -18)),
        "PICOHERTZ": ((0, 1), (10, 9)),
        "TERAHERTZ": ((0, 1), (10, -15)),
        "YOCTOHERTZ": ((0, 1), (10, 21)),
        "YOTTAHERTZ": ((0, 1), (10, -27)),
        "ZETTAHERTZ": ((0, 1), (10, -24)),
        "ZEPTOHERTZ": ((0, 1), (10, 18)),

    },
    "MICROHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 12)),
        "CENTIHERTZ": ((0, 1), (10, -4)),
        "DECAHERTZ": ((0, 1), (10, -7)),
        "DECIHERTZ": ((0, 1), (10, -5)),
        "EXAHERTZ": ((0, 1), (10, -24)),
        "FEMTOHERTZ": ((0, 1), (10, 9)),
        "GIGAHERTZ": ((0, 1), (10, -15)),
        "HECTOHERTZ": ((0, 1), (10, -8)),
        "HERTZ": ((0, 1), (10, -6)),
        "KILOHERTZ": ((0, 1), (10, -9)),
        "MEGAHERTZ": ((0, 1), (10, -12)),
        "MILLIHERTZ": ((0, 1), (10, -3)),
        "MICROHERTZ": (), # Same
        "NANOHERTZ": ((0, 1), (10, 3)),
        "PETAHERTZ": ((0, 1), (10, -21)),
        "PICOHERTZ": ((0, 1), (10, 6)),
        "TERAHERTZ": ((0, 1), (10, -18)),
        "YOCTOHERTZ": ((0, 1), (10, 18)),
        "YOTTAHERTZ": ((0, 1), (10, -30)),
        "ZETTAHERTZ": ((0, 1), (10, -27)),
        "ZEPTOHERTZ": ((0, 1), (10, 15)),

    },
    "NANOHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 9)),
        "CENTIHERTZ": ((0, 1), (10, -7)),
        "DECAHERTZ": ((0, 1), (10, -10)),
        "DECIHERTZ": ((0, 1), (10, -8)),
        "EXAHERTZ": ((0, 1), (10, -27)),
        "FEMTOHERTZ": ((0, 1), (10, 6)),
        "GIGAHERTZ": ((0, 1), (10, -18)),
        "HECTOHERTZ": ((0, 1), (10, -11)),
        "HERTZ": ((0, 1), (10, -9)),
        "KILOHERTZ": ((0, 1), (10, -12)),
        "MEGAHERTZ": ((0, 1), (10, -15)),
        "MILLIHERTZ": ((0, 1), (10, -6)),
        "MICROHERTZ": ((0, 1), (10, -3)),
        "NANOHERTZ": (), # Same
        "PETAHERTZ": ((0, 1), (10, -24)),
        "PICOHERTZ": ((0, 1), (10, 3)),
        "TERAHERTZ": ((0, 1), (10, -21)),
        "YOCTOHERTZ": ((0, 1), (10, 15)),
        "YOTTAHERTZ": ((0, 1), (10, -33)),
        "ZETTAHERTZ": ((0, 1), (10, -30)),
        "ZEPTOHERTZ": ((0, 1), (10, 12)),

    },
    "PETAHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 33)),
        "CENTIHERTZ": ((0, 1), (10, 17)),
        "DECAHERTZ": ((0, 1), (10, 14)),
        "DECIHERTZ": ((0, 1), (10, 16)),
        "EXAHERTZ": ((0, 1), (10, -3)),
        "FEMTOHERTZ": ((0, 1), (10, 30)),
        "GIGAHERTZ": ((0, 1), (10, 6)),
        "HECTOHERTZ": ((0, 1), (10, 13)),
        "HERTZ": ((0, 1), (10, 15)),
        "KILOHERTZ": ((0, 1), (10, 12)),
        "MEGAHERTZ": ((0, 1), (10, 9)),
        "MILLIHERTZ": ((0, 1), (10, 18)),
        "MICROHERTZ": ((0, 1), (10, 21)),
        "NANOHERTZ": ((0, 1), (10, 24)),
        "PETAHERTZ": (), # Same
        "PICOHERTZ": ((0, 1), (10, 27)),
        "TERAHERTZ": ((0, 1), (10, 3)),
        "YOCTOHERTZ": ((0, 1), (10, 39)),
        "YOTTAHERTZ": ((0, 1), (10, -9)),
        "ZETTAHERTZ": ((0, 1), (10, -6)),
        "ZEPTOHERTZ": ((0, 1), (10, 36)),

    },
    "PICOHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 6)),
        "CENTIHERTZ": ((0, 1), (10, -10)),
        "DECAHERTZ": ((0, 1), (10, -13)),
        "DECIHERTZ": ((0, 1), (10, -11)),
        "EXAHERTZ": ((0, 1), (10, -30)),
        "FEMTOHERTZ": ((0, 1), (10, 3)),
        "GIGAHERTZ": ((0, 1), (10, -21)),
        "HECTOHERTZ": ((0, 1), (10, -14)),
        "HERTZ": ((0, 1), (10, -12)),
        "KILOHERTZ": ((0, 1), (10, -15)),
        "MEGAHERTZ": ((0, 1), (10, -18)),
        "MILLIHERTZ": ((0, 1), (10, -9)),
        "MICROHERTZ": ((0, 1), (10, -6)),
        "NANOHERTZ": ((0, 1), (10, -3)),
        "PETAHERTZ": ((0, 1), (10, -27)),
        "PICOHERTZ": (), # Same
        "TERAHERTZ": ((0, 1), (10, -24)),
        "YOCTOHERTZ": ((0, 1), (10, 12)),
        "YOTTAHERTZ": ((0, 1), (10, -36)),
        "ZETTAHERTZ": ((0, 1), (10, -33)),
        "ZEPTOHERTZ": ((0, 1), (10, 9)),

    },
    "TERAHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 30)),
        "CENTIHERTZ": ((0, 1), (10, 14)),
        "DECAHERTZ": ((0, 1), (10, 11)),
        "DECIHERTZ": ((0, 1), (10, 13)),
        "EXAHERTZ": ((0, 1), (10, -6)),
        "FEMTOHERTZ": ((0, 1), (10, 27)),
        "GIGAHERTZ": ((0, 1), (10, 3)),
        "HECTOHERTZ": ((0, 1), (10, 10)),
        "HERTZ": ((0, 1), (10, 12)),
        "KILOHERTZ": ((0, 1), (10, 9)),
        "MEGAHERTZ": ((0, 1), (10, 6)),
        "MILLIHERTZ": ((0, 1), (10, 15)),
        "MICROHERTZ": ((0, 1), (10, 18)),
        "NANOHERTZ": ((0, 1), (10, 21)),
        "PETAHERTZ": ((0, 1), (10, -3)),
        "PICOHERTZ": ((0, 1), (10, 24)),
        "TERAHERTZ": (), # Same
        "YOCTOHERTZ": ((0, 1), (10, 36)),
        "YOTTAHERTZ": ((0, 1), (10, -12)),
        "ZETTAHERTZ": ((0, 1), (10, -9)),
        "ZEPTOHERTZ": ((0, 1), (10, 33)),

    },
    "YOCTOHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, -6)),
        "CENTIHERTZ": ((0, 1), (10, -22)),
        "DECAHERTZ": ((0, 1), (10, -25)),
        "DECIHERTZ": ((0, 1), (10, -23)),
        "EXAHERTZ": ((0, 1), (10, -42)),
        "FEMTOHERTZ": ((0, 1), (10, -9)),
        "GIGAHERTZ": ((0, 1), (10, -33)),
        "HECTOHERTZ": ((0, 1), (10, -26)),
        "HERTZ": ((0, 1), (10, -24)),
        "KILOHERTZ": ((0, 1), (10, -27)),
        "MEGAHERTZ": ((0, 1), (10, -30)),
        "MILLIHERTZ": ((0, 1), (10, -21)),
        "MICROHERTZ": ((0, 1), (10, -18)),
        "NANOHERTZ": ((0, 1), (10, -15)),
        "PETAHERTZ": ((0, 1), (10, -39)),
        "PICOHERTZ": ((0, 1), (10, -12)),
        "TERAHERTZ": ((0, 1), (10, -36)),
        "YOCTOHERTZ": (), # Same
        "YOTTAHERTZ": ((0, 1), (10, -48)),
        "ZETTAHERTZ": ((0, 1), (10, -45)),
        "ZEPTOHERTZ": ((0, 1), (10, -3)),

    },
    "YOTTAHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 42)),
        "CENTIHERTZ": ((0, 1), (10, 26)),
        "DECAHERTZ": ((0, 1), (10, 23)),
        "DECIHERTZ": ((0, 1), (10, 25)),
        "EXAHERTZ": ((0, 1), (10, 6)),
        "FEMTOHERTZ": ((0, 1), (10, 39)),
        "GIGAHERTZ": ((0, 1), (10, 15)),
        "HECTOHERTZ": ((0, 1), (10, 22)),
        "HERTZ": ((0, 1), (10, 24)),
        "KILOHERTZ": ((0, 1), (10, 21)),
        "MEGAHERTZ": ((0, 1), (10, 18)),
        "MILLIHERTZ": ((0, 1), (10, 27)),
        "MICROHERTZ": ((0, 1), (10, 30)),
        "NANOHERTZ": ((0, 1), (10, 33)),
        "PETAHERTZ": ((0, 1), (10, 9)),
        "PICOHERTZ": ((0, 1), (10, 36)),
        "TERAHERTZ": ((0, 1), (10, 12)),
        "YOCTOHERTZ": ((0, 1), (10, 48)),
        "YOTTAHERTZ": (), # Same
        "ZETTAHERTZ": ((0, 1), (10, 3)),
        "ZEPTOHERTZ": ((0, 1), (10, 45)),

    },
    "ZETTAHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, 39)),
        "CENTIHERTZ": ((0, 1), (10, 23)),
        "DECAHERTZ": ((0, 1), (10, 20)),
        "DECIHERTZ": ((0, 1), (10, 22)),
        "EXAHERTZ": ((0, 1), (10, 3)),
        "FEMTOHERTZ": ((0, 1), (10, 36)),
        "GIGAHERTZ": ((0, 1), (10, 12)),
        "HECTOHERTZ": ((0, 1), (10, 19)),
        "HERTZ": ((0, 1), (10, 21)),
        "KILOHERTZ": ((0, 1), (10, 18)),
        "MEGAHERTZ": ((0, 1), (10, 15)),
        "MILLIHERTZ": ((0, 1), (10, 24)),
        "MICROHERTZ": ((0, 1), (10, 27)),
        "NANOHERTZ": ((0, 1), (10, 30)),
        "PETAHERTZ": ((0, 1), (10, 6)),
        "PICOHERTZ": ((0, 1), (10, 33)),
        "TERAHERTZ": ((0, 1), (10, 9)),
        "YOCTOHERTZ": ((0, 1), (10, 45)),
        "YOTTAHERTZ": ((0, 1), (10, -3)),
        "ZETTAHERTZ": (), # Same
        "ZEPTOHERTZ": ((0, 1), (10, 42)),

    },
    "ZEPTOHERTZ": {
        "ATTOHERTZ": ((0, 1), (10, -3)),
        "CENTIHERTZ": ((0, 1), (10, -19)),
        "DECAHERTZ": ((0, 1), (10, -22)),
        "DECIHERTZ": ((0, 1), (10, -20)),
        "EXAHERTZ": ((0, 1), (10, -39)),
        "FEMTOHERTZ": ((0, 1), (10, -6)),
        "GIGAHERTZ": ((0, 1), (10, -30)),
        "HECTOHERTZ": ((0, 1), (10, -23)),
        "HERTZ": ((0, 1), (10, -21)),
        "KILOHERTZ": ((0, 1), (10, -24)),
        "MEGAHERTZ": ((0, 1), (10, -27)),
        "MILLIHERTZ": ((0, 1), (10, -18)),
        "MICROHERTZ": ((0, 1), (10, -15)),
        "NANOHERTZ": ((0, 1), (10, -12)),
        "PETAHERTZ": ((0, 1), (10, -36)),
        "PICOHERTZ": ((0, 1), (10, -9)),
        "TERAHERTZ": ((0, 1), (10, -33)),
        "YOCTOHERTZ": ((0, 1), (10, 3)),
        "YOTTAHERTZ": ((0, 1), (10, -45)),
        "ZETTAHERTZ": ((0, 1), (10, -42)),
        "ZEPTOHERTZ": (), # Same

    },

  },
  "Length": {
    "ATTOMETER": {
        "ATTOMETER": (), # Same
        "ANGSTROM": ((0, 1), (10, -8)),
        "CENTIMETER": ((0, 1), (10, -16)),
        "DECAMETER": ((0, 1), (10, -19)),
        "DECIMETER": ((0, 1), (10, -17)),
        "EXAMETER": ((0, 1), (10, -36)),
        "FEMTOMETER": ((0, 1), (10, -3)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -27)),
        "HECTOMETER": ((0, 1), (10, -20)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -21)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -18)),
        "MEGAMETER": ((0, 1), (10, -24)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, -12)),
        "MILLIMETER": ((0, 1), (10, -15)),
        "NANOMETER": ((0, 1), (10, -9)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -33)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, -6)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -30)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 6)),
        "YOTTAMETER": ((0, 1), (10, -42)),
        "ZETTAMETER": ((0, 1), (10, -39)),
        "ZEPTOMETER": ((0, 1), (10, 3)),

    },
    "ANGSTROM": {
        "ATTOMETER": ((0, 1), (10, 8)),
        "ANGSTROM": (), # Same
        "CENTIMETER": ((0, 1), (10, -8)),
        "DECAMETER": ((0, 1), (10, -11)),
        "DECIMETER": ((0, 1), (10, -9)),
        "EXAMETER": ((0, 1), (10, -28)),
        "FEMTOMETER": ((0, 1), (10, 5)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -19)),
        "HECTOMETER": ((0, 1), (10, -12)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -13)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -10)),
        "MEGAMETER": ((0, 1), (10, -16)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, -4)),
        "MILLIMETER": ((0, 1), (10, -7)),
        "NANOMETER": ((0, 1), (10, -1)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -25)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 2)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -22)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 14)),
        "YOTTAMETER": ((0, 1), (10, -34)),
        "ZETTAMETER": ((0, 1), (10, -31)),
        "ZEPTOMETER": ((0, 1), (10, 11)),
    },
    "CENTIMETER": {
        "ATTOMETER": ((0, 1), (10, 16)),
        "ANGSTROM": ((0, 1), (10, 8)),
        "CENTIMETER": (), # Same
        "DECAMETER": ((0, 1), (10, -3)),
        "DECIMETER": ((0, 1), (10, -1)),
        "EXAMETER": ((0, 1), (10, -20)),
        "FEMTOMETER": ((0, 1), (10, 13)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -11)),
        "HECTOMETER": ((0, 1), (10, -4)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -5)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -2)),
        "MEGAMETER": ((0, 1), (10, -8)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 4)),
        "MILLIMETER": ((0, 1), (10, 1)),
        "NANOMETER": ((0, 1), (10, 7)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -17)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 10)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -14)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 22)),
        "YOTTAMETER": ((0, 1), (10, -26)),
        "ZETTAMETER": ((0, 1), (10, -23)),
        "ZEPTOMETER": ((0, 1), (10, 19)),

    },
    "DECAMETER": {
        "ATTOMETER": ((0, 1), (10, 19)),
        "ANGSTROM": ((0, 1), (10, 11)),
        "CENTIMETER": ((0, 1), (10, 3)),
        "DECAMETER": (), # Same
        "DECIMETER": ((0, 1), (10, 2)),
        "EXAMETER": ((0, 1), (10, -17)),
        "FEMTOMETER": ((0, 1), (10, 16)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -8)),
        "HECTOMETER": ((0, 1), (10, -1)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -2)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 1)),
        "MEGAMETER": ((0, 1), (10, -5)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 7)),
        "MILLIMETER": ((0, 1), (10, 4)),
        "NANOMETER": ((0, 1), (10, 10)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -14)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 13)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -11)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 25)),
        "YOTTAMETER": ((0, 1), (10, -23)),
        "ZETTAMETER": ((0, 1), (10, -20)),
        "ZEPTOMETER": ((0, 1), (10, 22)),

    },
    "DECIMETER": {
        "ATTOMETER": ((0, 1), (10, 17)),
        "ANGSTROM": ((0, 1), (10, 9)),
        "CENTIMETER": ((0, 1), (10, 1)),
        "DECAMETER": ((0, 1), (10, -2)),
        "DECIMETER": (), # Same
        "EXAMETER": ((0, 1), (10, -19)),
        "FEMTOMETER": ((0, 1), (10, 14)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -10)),
        "HECTOMETER": ((0, 1), (10, -3)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -4)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -1)),
        "MEGAMETER": ((0, 1), (10, -7)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 5)),
        "MILLIMETER": ((0, 1), (10, 2)),
        "NANOMETER": ((0, 1), (10, 8)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -16)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 11)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -13)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 23)),
        "YOTTAMETER": ((0, 1), (10, -25)),
        "ZETTAMETER": ((0, 1), (10, -22)),
        "ZEPTOMETER": ((0, 1), (10, 20)),

    },
    "EXAMETER": {
        "ATTOMETER": ((0, 1), (10, 36)),
        "ANGSTROM": ((0, 1), (10, 28)),
        "CENTIMETER": ((0, 1), (10, 20)),
        "DECAMETER": ((0, 1), (10, 17)),
        "DECIMETER": ((0, 1), (10, 19)),
        "EXAMETER": (), # Same
        "FEMTOMETER": ((0, 1), (10, 33)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, 9)),
        "HECTOMETER": ((0, 1), (10, 16)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, 15)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 18)),
        "MEGAMETER": ((0, 1), (10, 12)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 24)),
        "MILLIMETER": ((0, 1), (10, 21)),
        "NANOMETER": ((0, 1), (10, 27)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, 3)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 30)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, 6)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 42)),
        "YOTTAMETER": ((0, 1), (10, -6)),
        "ZETTAMETER": ((0, 1), (10, -3)),
        "ZEPTOMETER": ((0, 1), (10, 39)),

    },
    "FEMTOMETER": {
        "ATTOMETER": ((0, 1), (10, 3)),
        "ANGSTROM": ((0, 1), (10, -5)),
        "CENTIMETER": ((0, 1), (10, -13)),
        "DECAMETER": ((0, 1), (10, -16)),
        "DECIMETER": ((0, 1), (10, -14)),
        "EXAMETER": ((0, 1), (10, -33)),
        "FEMTOMETER": (), # Same
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -24)),
        "HECTOMETER": ((0, 1), (10, -17)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -18)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -15)),
        "MEGAMETER": ((0, 1), (10, -21)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, -9)),
        "MILLIMETER": ((0, 1), (10, -12)),
        "NANOMETER": ((0, 1), (10, -6)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -30)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, -3)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -27)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 9)),
        "YOTTAMETER": ((0, 1), (10, -39)),
        "ZETTAMETER": ((0, 1), (10, -36)),
        "ZEPTOMETER": ((0, 1), (10, 6)),

    },
    "FT": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (), # Same
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "GIGAMETER": {
        "ATTOMETER": ((0, 1), (10, 27)),
        "ANGSTROM": ((0, 1), (10, 19)),
        "CENTIMETER": ((0, 1), (10, 11)),
        "DECAMETER": ((0, 1), (10, 8)),
        "DECIMETER": ((0, 1), (10, 10)),
        "EXAMETER": ((0, 1), (10, -9)),
        "FEMTOMETER": ((0, 1), (10, 24)),
        "FT": (None,),  # Undefined
        "GIGAMETER": (), # Same
        "HECTOMETER": ((0, 1), (10, 7)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, 6)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 9)),
        "MEGAMETER": ((0, 1), (10, 3)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 15)),
        "MILLIMETER": ((0, 1), (10, 12)),
        "NANOMETER": ((0, 1), (10, 18)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -6)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 21)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -3)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 33)),
        "YOTTAMETER": ((0, 1), (10, -15)),
        "ZETTAMETER": ((0, 1), (10, -12)),
        "ZEPTOMETER": ((0, 1), (10, 30)),

    },
    "HECTOMETER": {
        "ATTOMETER": ((0, 1), (10, 20)),
        "ANGSTROM": ((0, 1), (10, 12)),
        "CENTIMETER": ((0, 1), (10, 4)),
        "DECAMETER": ((0, 1), (10, 1)),
        "DECIMETER": ((0, 1), (10, 3)),
        "EXAMETER": ((0, 1), (10, -16)),
        "FEMTOMETER": ((0, 1), (10, 17)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -7)),
        "HECTOMETER": (), # Same
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -1)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 2)),
        "MEGAMETER": ((0, 1), (10, -4)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 8)),
        "MILLIMETER": ((0, 1), (10, 5)),
        "NANOMETER": ((0, 1), (10, 11)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -13)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 14)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -10)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 26)),
        "YOTTAMETER": ((0, 1), (10, -22)),
        "ZETTAMETER": ((0, 1), (10, -19)),
        "ZEPTOMETER": ((0, 1), (10, 23)),

    },
    "IN": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (), # Same
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "KILOMETER": {
        "ATTOMETER": ((0, 1), (10, 21)),
        "ANGSTROM": ((0, 1), (10, 13)),
        "CENTIMETER": ((0, 1), (10, 5)),
        "DECAMETER": ((0, 1), (10, 2)),
        "DECIMETER": ((0, 1), (10, 4)),
        "EXAMETER": ((0, 1), (10, -15)),
        "FEMTOMETER": ((0, 1), (10, 18)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -6)),
        "HECTOMETER": ((0, 1), (10, 1)),
        "IN": (None,),  # Undefined
        "KILOMETER": (), # Same
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 3)),
        "MEGAMETER": ((0, 1), (10, -3)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 9)),
        "MILLIMETER": ((0, 1), (10, 6)),
        "NANOMETER": ((0, 1), (10, 12)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -12)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 15)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -9)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 27)),
        "YOTTAMETER": ((0, 1), (10, -21)),
        "ZETTAMETER": ((0, 1), (10, -18)),
        "ZEPTOMETER": ((0, 1), (10, 24)),

    },
    "LI": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (), # Same
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "LIGHTYEAR": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (), # Same
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "METER": {
        "ATTOMETER": ((0, 1), (10, 18)),
        "ANGSTROM": ((0, 1), (10, 10)),
        "CENTIMETER": ((0, 1), (10, 2)),
        "DECAMETER": ((0, 1), (10, -1)),
        "DECIMETER": ((0, 1), (10, 1)),
        "EXAMETER": ((0, 1), (10, -18)),
        "FEMTOMETER": ((0, 1), (10, 15)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -9)),
        "HECTOMETER": ((0, 1), (10, -2)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -3)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (), # Same
        "MEGAMETER": ((0, 1), (10, -6)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 6)),
        "MILLIMETER": ((0, 1), (10, 3)),
        "NANOMETER": ((0, 1), (10, 9)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -15)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 12)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -12)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 24)),
        "YOTTAMETER": ((0, 1), (10, -24)),
        "ZETTAMETER": ((0, 1), (10, -21)),
        "ZEPTOMETER": ((0, 1), (10, 21)),

    },
    "MEGAMETER": {
        "ATTOMETER": ((0, 1), (10, 24)),
        "ANGSTROM": ((0, 1), (10, 16)),
        "CENTIMETER": ((0, 1), (10, 8)),
        "DECAMETER": ((0, 1), (10, 5)),
        "DECIMETER": ((0, 1), (10, 7)),
        "EXAMETER": ((0, 1), (10, -12)),
        "FEMTOMETER": ((0, 1), (10, 21)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -3)),
        "HECTOMETER": ((0, 1), (10, 4)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, 3)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 6)),
        "MEGAMETER": (), # Same
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 12)),
        "MILLIMETER": ((0, 1), (10, 9)),
        "NANOMETER": ((0, 1), (10, 15)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -9)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 18)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -6)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 30)),
        "YOTTAMETER": ((0, 1), (10, -18)),
        "ZETTAMETER": ((0, 1), (10, -15)),
        "ZEPTOMETER": ((0, 1), (10, 27)),

    },
    "MI": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (), # Same
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "MICROMETER": {
        "ATTOMETER": ((0, 1), (10, 12)),
        "ANGSTROM": ((0, 1), (10, 4)),
        "CENTIMETER": ((0, 1), (10, -4)),
        "DECAMETER": ((0, 1), (10, -7)),
        "DECIMETER": ((0, 1), (10, -5)),
        "EXAMETER": ((0, 1), (10, -24)),
        "FEMTOMETER": ((0, 1), (10, 9)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -15)),
        "HECTOMETER": ((0, 1), (10, -8)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -9)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -6)),
        "MEGAMETER": ((0, 1), (10, -12)),
        "MI": (None,),  # Undefined
        "MICROMETER": (), # Same
        "MILLIMETER": ((0, 1), (10, -3)),
        "NANOMETER": ((0, 1), (10, 3)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -21)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 6)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -18)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 18)),
        "YOTTAMETER": ((0, 1), (10, -30)),
        "ZETTAMETER": ((0, 1), (10, -27)),
        "ZEPTOMETER": ((0, 1), (10, 15)),

    },
    "MILLIMETER": {
        "ATTOMETER": ((0, 1), (10, 15)),
        "ANGSTROM": ((0, 1), (10, 7)),
        "CENTIMETER": ((0, 1), (10, -1)),
        "DECAMETER": ((0, 1), (10, -4)),
        "DECIMETER": ((0, 1), (10, -2)),
        "EXAMETER": ((0, 1), (10, -21)),
        "FEMTOMETER": ((0, 1), (10, 12)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -12)),
        "HECTOMETER": ((0, 1), (10, -5)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -6)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -3)),
        "MEGAMETER": ((0, 1), (10, -9)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 3)),
        "MILLIMETER": (), # Same
        "NANOMETER": ((0, 1), (10, 6)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -18)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 9)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -15)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 21)),
        "YOTTAMETER": ((0, 1), (10, -27)),
        "ZETTAMETER": ((0, 1), (10, -24)),
        "ZEPTOMETER": ((0, 1), (10, 18)),

    },
    "NANOMETER": {
        "ATTOMETER": ((0, 1), (10, 9)),
        "ANGSTROM": ((0, 1), (10, 1)),
        "CENTIMETER": ((0, 1), (10, -7)),
        "DECAMETER": ((0, 1), (10, -10)),
        "DECIMETER": ((0, 1), (10, -8)),
        "EXAMETER": ((0, 1), (10, -27)),
        "FEMTOMETER": ((0, 1), (10, 6)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -18)),
        "HECTOMETER": ((0, 1), (10, -11)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -12)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -9)),
        "MEGAMETER": ((0, 1), (10, -15)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, -3)),
        "MILLIMETER": ((0, 1), (10, -6)),
        "NANOMETER": (), # Same
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -24)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 3)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -21)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 15)),
        "YOTTAMETER": ((0, 1), (10, -33)),
        "ZETTAMETER": ((0, 1), (10, -30)),
        "ZEPTOMETER": ((0, 1), (10, 12)),

    },
    "PARSEC": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (), # Same
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "PETAMETER": {
        "ATTOMETER": ((0, 1), (10, 33)),
        "ANGSTROM": ((0, 1), (10, 25)),
        "CENTIMETER": ((0, 1), (10, 17)),
        "DECAMETER": ((0, 1), (10, 14)),
        "DECIMETER": ((0, 1), (10, 16)),
        "EXAMETER": ((0, 1), (10, -3)),
        "FEMTOMETER": ((0, 1), (10, 30)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, 6)),
        "HECTOMETER": ((0, 1), (10, 13)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, 12)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 15)),
        "MEGAMETER": ((0, 1), (10, 9)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 21)),
        "MILLIMETER": ((0, 1), (10, 18)),
        "NANOMETER": ((0, 1), (10, 24)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (), # Same
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 27)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, 3)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 39)),
        "YOTTAMETER": ((0, 1), (10, -9)),
        "ZETTAMETER": ((0, 1), (10, -6)),
        "ZEPTOMETER": ((0, 1), (10, 36)),

    },
    "PIXEL": {
        "ATTOMETER": (None,),  # Impossible
        "ANGSTROM": (None,),  # Impossible
        "CENTIMETER": (None,),  # Impossible
        "DECAMETER": (None,),  # Impossible
        "DECIMETER": (None,),  # Impossible
        "EXAMETER": (None,),  # Impossible
        "FEMTOMETER": (None,),  # Impossible
        "FT": (None,),  # Impossible
        "GIGAMETER": (None,),  # Impossible
        "HECTOMETER": (None,),  # Impossible
        "IN": (None,),  # Impossible
        "KILOMETER": (None,),  # Impossible
        "LI": (None,),  # Impossible
        "LIGHTYEAR": (None,),  # Impossible
        "METER": (None,),  # Impossible
        "MEGAMETER": (None,),  # Impossible
        "MI": (None,),  # Impossible
        "MICROMETER": (None,),  # Impossible
        "MILLIMETER": (None,),  # Impossible
        "NANOMETER": (None,),  # Impossible
        "PARSEC": (None,),  # Impossible
        "PETAMETER": (None,),  # Impossible
        "PIXEL": (), # Same
        "PICOMETER": (None,),  # Impossible
        "PT": (None,),  # Impossible
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Impossible
        "THOU": (None,),  # Impossible
        "ASTRONOMICALUNIT": (None,),  # Impossible
        "YD": (None,),  # Impossible
        "YOCTOMETER": (None,),  # Impossible
        "YOTTAMETER": (None,),  # Impossible
        "ZETTAMETER": (None,),  # Impossible
        "ZEPTOMETER": (None,),  # Impossible

    },
    "PICOMETER": {
        "ATTOMETER": ((0, 1), (10, 6)),
        "ANGSTROM": ((0, 1), (10, -2)),
        "CENTIMETER": ((0, 1), (10, -10)),
        "DECAMETER": ((0, 1), (10, -13)),
        "DECIMETER": ((0, 1), (10, -11)),
        "EXAMETER": ((0, 1), (10, -30)),
        "FEMTOMETER": ((0, 1), (10, 3)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -21)),
        "HECTOMETER": ((0, 1), (10, -14)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -15)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -12)),
        "MEGAMETER": ((0, 1), (10, -18)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, -6)),
        "MILLIMETER": ((0, 1), (10, -9)),
        "NANOMETER": ((0, 1), (10, -3)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -27)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (), # Same
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -24)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 12)),
        "YOTTAMETER": ((0, 1), (10, -36)),
        "ZETTAMETER": ((0, 1), (10, -33)),
        "ZEPTOMETER": ((0, 1), (10, 9)),

    },
    "PT": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (), # Same
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "REFERENCEFRAME": {
        "ATTOMETER": (None,),  # Impossible
        "ANGSTROM": (None,),  # Impossible
        "CENTIMETER": (None,),  # Impossible
        "DECAMETER": (None,),  # Impossible
        "DECIMETER": (None,),  # Impossible
        "EXAMETER": (None,),  # Impossible
        "FEMTOMETER": (None,),  # Impossible
        "FT": (None,),  # Impossible
        "GIGAMETER": (None,),  # Impossible
        "HECTOMETER": (None,),  # Impossible
        "IN": (None,),  # Impossible
        "KILOMETER": (None,),  # Impossible
        "LI": (None,),  # Impossible
        "LIGHTYEAR": (None,),  # Impossible
        "METER": (None,),  # Impossible
        "MEGAMETER": (None,),  # Impossible
        "MI": (None,),  # Impossible
        "MICROMETER": (None,),  # Impossible
        "MILLIMETER": (None,),  # Impossible
        "NANOMETER": (None,),  # Impossible
        "PARSEC": (None,),  # Impossible
        "PETAMETER": (None,),  # Impossible
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Impossible
        "PT": (None,),  # Impossible
        "REFERENCEFRAME": (), # Same
        "TERAMETER": (None,),  # Impossible
        "THOU": (None,),  # Impossible
        "ASTRONOMICALUNIT": (None,),  # Impossible
        "YD": (None,),  # Impossible
        "YOCTOMETER": (None,),  # Impossible
        "YOTTAMETER": (None,),  # Impossible
        "ZETTAMETER": (None,),  # Impossible
        "ZEPTOMETER": (None,),  # Impossible

    },
    "TERAMETER": {
        "ATTOMETER": ((0, 1), (10, 30)),
        "ANGSTROM": ((0, 1), (10, 22)),
        "CENTIMETER": ((0, 1), (10, 14)),
        "DECAMETER": ((0, 1), (10, 11)),
        "DECIMETER": ((0, 1), (10, 13)),
        "EXAMETER": ((0, 1), (10, -6)),
        "FEMTOMETER": ((0, 1), (10, 27)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, 3)),
        "HECTOMETER": ((0, 1), (10, 10)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, 9)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 12)),
        "MEGAMETER": ((0, 1), (10, 6)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 18)),
        "MILLIMETER": ((0, 1), (10, 15)),
        "NANOMETER": ((0, 1), (10, 21)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -3)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 24)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (), # Same
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 36)),
        "YOTTAMETER": ((0, 1), (10, -12)),
        "ZETTAMETER": ((0, 1), (10, -9)),
        "ZEPTOMETER": ((0, 1), (10, 33)),

    },
    "THOU": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (), # Same
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "ASTRONOMICALUNIT": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (), # Same
        "YD": (None,),  # Undefined
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "YD": {
        "ATTOMETER": (None,),  # Undefined
        "ANGSTROM": (None,),  # Undefined
        "CENTIMETER": (None,),  # Undefined
        "DECAMETER": (None,),  # Undefined
        "DECIMETER": (None,),  # Undefined
        "EXAMETER": (None,),  # Undefined
        "FEMTOMETER": (None,),  # Undefined
        "FT": (None,),  # Undefined
        "GIGAMETER": (None,),  # Undefined
        "HECTOMETER": (None,),  # Undefined
        "IN": (None,),  # Undefined
        "KILOMETER": (None,),  # Undefined
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": (None,),  # Undefined
        "MEGAMETER": (None,),  # Undefined
        "MI": (None,),  # Undefined
        "MICROMETER": (None,),  # Undefined
        "MILLIMETER": (None,),  # Undefined
        "NANOMETER": (None,),  # Undefined
        "PARSEC": (None,),  # Undefined
        "PETAMETER": (None,),  # Undefined
        "PIXEL": (None,),  # Impossible
        "PICOMETER": (None,),  # Undefined
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": (None,),  # Undefined
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (), # Same
        "YOCTOMETER": (None,),  # Undefined
        "YOTTAMETER": (None,),  # Undefined
        "ZETTAMETER": (None,),  # Undefined
        "ZEPTOMETER": (None,),  # Undefined

    },
    "YOCTOMETER": {
        "ATTOMETER": ((0, 1), (10, -6)),
        "ANGSTROM": ((0, 1), (10, -14)),
        "CENTIMETER": ((0, 1), (10, -22)),
        "DECAMETER": ((0, 1), (10, -25)),
        "DECIMETER": ((0, 1), (10, -23)),
        "EXAMETER": ((0, 1), (10, -42)),
        "FEMTOMETER": ((0, 1), (10, -9)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -33)),
        "HECTOMETER": ((0, 1), (10, -26)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -27)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -24)),
        "MEGAMETER": ((0, 1), (10, -30)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, -18)),
        "MILLIMETER": ((0, 1), (10, -21)),
        "NANOMETER": ((0, 1), (10, -15)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -39)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, -12)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -36)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": (), # Same
        "YOTTAMETER": ((0, 1), (10, -48)),
        "ZETTAMETER": ((0, 1), (10, -45)),
        "ZEPTOMETER": ((0, 1), (10, -3)),

    },
    "YOTTAMETER": {
        "ATTOMETER": ((0, 1), (10, 42)),
        "ANGSTROM": ((0, 1), (10, 34)),
        "CENTIMETER": ((0, 1), (10, 26)),
        "DECAMETER": ((0, 1), (10, 23)),
        "DECIMETER": ((0, 1), (10, 25)),
        "EXAMETER": ((0, 1), (10, 6)),
        "FEMTOMETER": ((0, 1), (10, 39)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, 15)),
        "HECTOMETER": ((0, 1), (10, 22)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, 21)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 24)),
        "MEGAMETER": ((0, 1), (10, 18)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 30)),
        "MILLIMETER": ((0, 1), (10, 27)),
        "NANOMETER": ((0, 1), (10, 33)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, 9)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 36)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, 12)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 48)),
        "YOTTAMETER": (), # Same
        "ZETTAMETER": ((0, 1), (10, 3)),
        "ZEPTOMETER": ((0, 1), (10, 45)),

    },
    "ZETTAMETER": {
        "ATTOMETER": ((0, 1), (10, 39)),
        "ANGSTROM": ((0, 1), (10, 31)),
        "CENTIMETER": ((0, 1), (10, 23)),
        "DECAMETER": ((0, 1), (10, 20)),
        "DECIMETER": ((0, 1), (10, 22)),
        "EXAMETER": ((0, 1), (10, 3)),
        "FEMTOMETER": ((0, 1), (10, 36)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, 12)),
        "HECTOMETER": ((0, 1), (10, 19)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, 18)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, 21)),
        "MEGAMETER": ((0, 1), (10, 15)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, 27)),
        "MILLIMETER": ((0, 1), (10, 24)),
        "NANOMETER": ((0, 1), (10, 30)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, 6)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, 33)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, 9)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 45)),
        "YOTTAMETER": ((0, 1), (10, -3)),
        "ZETTAMETER": (), # Same
        "ZEPTOMETER": ((0, 1), (10, 42)),

    },
    "ZEPTOMETER": {
        "ATTOMETER": ((0, 1), (10, -3)),
        "ANGSTROM": ((0, 1), (10, -11)),
        "CENTIMETER": ((0, 1), (10, -19)),
        "DECAMETER": ((0, 1), (10, -22)),
        "DECIMETER": ((0, 1), (10, -20)),
        "EXAMETER": ((0, 1), (10, -39)),
        "FEMTOMETER": ((0, 1), (10, -6)),
        "FT": (None,),  # Undefined
        "GIGAMETER": ((0, 1), (10, -30)),
        "HECTOMETER": ((0, 1), (10, -23)),
        "IN": (None,),  # Undefined
        "KILOMETER": ((0, 1), (10, -24)),
        "LI": (None,),  # Undefined
        "LIGHTYEAR": (None,),  # Undefined
        "METER": ((0, 1), (10, -21)),
        "MEGAMETER": ((0, 1), (10, -27)),
        "MI": (None,),  # Undefined
        "MICROMETER": ((0, 1), (10, -15)),
        "MILLIMETER": ((0, 1), (10, -18)),
        "NANOMETER": ((0, 1), (10, -12)),
        "PARSEC": (None,),  # Undefined
        "PETAMETER": ((0, 1), (10, -36)),
        "PIXEL": (None,),  # Impossible
        "PICOMETER": ((0, 1), (10, -9)),
        "PT": (None,),  # Undefined
        "REFERENCEFRAME": (None,),  # Impossible
        "TERAMETER": ((0, 1), (10, -33)),
        "THOU": (None,),  # Undefined
        "ASTRONOMICALUNIT": (None,),  # Undefined
        "YD": (None,),  # Undefined
        "YOCTOMETER": ((0, 1), (10, 3)),
        "YOTTAMETER": ((0, 1), (10, -45)),
        "ZETTAMETER": ((0, 1), (10, -42)),
        "ZEPTOMETER": (), # Same

    },

  },
  "Power": {
    "ATTOWATT": {
        "ATTOWATT": (), # Same
        "CENTIWATT": ((0, 1), (10, -16)),
        "DECAWATT": ((0, 1), (10, -19)),
        "DECIWATT": ((0, 1), (10, -17)),
        "EXAWATT": ((0, 1), (10, -36)),
        "FEMTOWATT": ((0, 1), (10, -3)),
        "GIGAWATT": ((0, 1), (10, -27)),
        "HECTOWATT": ((0, 1), (10, -20)),
        "KILOWATT": ((0, 1), (10, -21)),
        "MEGAWATT": ((0, 1), (10, -24)),
        "MICROWATT": ((0, 1), (10, -12)),
        "MILLIWATT": ((0, 1), (10, -15)),
        "NANOWATT": ((0, 1), (10, -9)),
        "PETAWATT": ((0, 1), (10, -33)),
        "PICOWATT": ((0, 1), (10, -6)),
        "TERAWATT": ((0, 1), (10, -30)),
        "WATT": ((0, 1), (10, -18)),
        "YOTTAWATT": ((0, 1), (10, -42)),
        "YOCTOWATT": ((0, 1), (10, 6)),
        "ZETTAWATT": ((0, 1), (10, -39)),
        "ZEPTOWATT": ((0, 1), (10, 3)),

    },
    "CENTIWATT": {
        "ATTOWATT": ((0, 1), (10, 16)),
        "CENTIWATT": (), # Same
        "DECAWATT": ((0, 1), (10, -3)),
        "DECIWATT": ((0, 1), (10, -1)),
        "EXAWATT": ((0, 1), (10, -20)),
        "FEMTOWATT": ((0, 1), (10, 13)),
        "GIGAWATT": ((0, 1), (10, -11)),
        "HECTOWATT": ((0, 1), (10, -4)),
        "KILOWATT": ((0, 1), (10, -5)),
        "MEGAWATT": ((0, 1), (10, -8)),
        "MICROWATT": ((0, 1), (10, 4)),
        "MILLIWATT": ((0, 1), (10, 1)),
        "NANOWATT": ((0, 1), (10, 7)),
        "PETAWATT": ((0, 1), (10, -17)),
        "PICOWATT": ((0, 1), (10, 10)),
        "TERAWATT": ((0, 1), (10, -14)),
        "WATT": ((0, 1), (10, -2)),
        "YOTTAWATT": ((0, 1), (10, -26)),
        "YOCTOWATT": ((0, 1), (10, 22)),
        "ZETTAWATT": ((0, 1), (10, -23)),
        "ZEPTOWATT": ((0, 1), (10, 19)),

    },
    "DECAWATT": {
        "ATTOWATT": ((0, 1), (10, 19)),
        "CENTIWATT": ((0, 1), (10, 3)),
        "DECAWATT": (), # Same
        "DECIWATT": ((0, 1), (10, 2)),
        "EXAWATT": ((0, 1), (10, -17)),
        "FEMTOWATT": ((0, 1), (10, 16)),
        "GIGAWATT": ((0, 1), (10, -8)),
        "HECTOWATT": ((0, 1), (10, -1)),
        "KILOWATT": ((0, 1), (10, -2)),
        "MEGAWATT": ((0, 1), (10, -5)),
        "MICROWATT": ((0, 1), (10, 7)),
        "MILLIWATT": ((0, 1), (10, 4)),
        "NANOWATT": ((0, 1), (10, 10)),
        "PETAWATT": ((0, 1), (10, -14)),
        "PICOWATT": ((0, 1), (10, 13)),
        "TERAWATT": ((0, 1), (10, -11)),
        "WATT": ((0, 1), (10, 1)),
        "YOTTAWATT": ((0, 1), (10, -23)),
        "YOCTOWATT": ((0, 1), (10, 25)),
        "ZETTAWATT": ((0, 1), (10, -20)),
        "ZEPTOWATT": ((0, 1), (10, 22)),

    },
    "DECIWATT": {
        "ATTOWATT": ((0, 1), (10, 17)),
        "CENTIWATT": ((0, 1), (10, 1)),
        "DECAWATT": ((0, 1), (10, -2)),
        "DECIWATT": (), # Same
        "EXAWATT": ((0, 1), (10, -19)),
        "FEMTOWATT": ((0, 1), (10, 14)),
        "GIGAWATT": ((0, 1), (10, -10)),
        "HECTOWATT": ((0, 1), (10, -3)),
        "KILOWATT": ((0, 1), (10, -4)),
        "MEGAWATT": ((0, 1), (10, -7)),
        "MICROWATT": ((0, 1), (10, 5)),
        "MILLIWATT": ((0, 1), (10, 2)),
        "NANOWATT": ((0, 1), (10, 8)),
        "PETAWATT": ((0, 1), (10, -16)),
        "PICOWATT": ((0, 1), (10, 11)),
        "TERAWATT": ((0, 1), (10, -13)),
        "WATT": ((0, 1), (10, -1)),
        "YOTTAWATT": ((0, 1), (10, -25)),
        "YOCTOWATT": ((0, 1), (10, 23)),
        "ZETTAWATT": ((0, 1), (10, -22)),
        "ZEPTOWATT": ((0, 1), (10, 20)),

    },
    "EXAWATT": {
        "ATTOWATT": ((0, 1), (10, 36)),
        "CENTIWATT": ((0, 1), (10, 20)),
        "DECAWATT": ((0, 1), (10, 17)),
        "DECIWATT": ((0, 1), (10, 19)),
        "EXAWATT": (), # Same
        "FEMTOWATT": ((0, 1), (10, 33)),
        "GIGAWATT": ((0, 1), (10, 9)),
        "HECTOWATT": ((0, 1), (10, 16)),
        "KILOWATT": ((0, 1), (10, 15)),
        "MEGAWATT": ((0, 1), (10, 12)),
        "MICROWATT": ((0, 1), (10, 24)),
        "MILLIWATT": ((0, 1), (10, 21)),
        "NANOWATT": ((0, 1), (10, 27)),
        "PETAWATT": ((0, 1), (10, 3)),
        "PICOWATT": ((0, 1), (10, 30)),
        "TERAWATT": ((0, 1), (10, 6)),
        "WATT": ((0, 1), (10, 18)),
        "YOTTAWATT": ((0, 1), (10, -6)),
        "YOCTOWATT": ((0, 1), (10, 42)),
        "ZETTAWATT": ((0, 1), (10, -3)),
        "ZEPTOWATT": ((0, 1), (10, 39)),

    },
    "FEMTOWATT": {
        "ATTOWATT": ((0, 1), (10, 3)),
        "CENTIWATT": ((0, 1), (10, -13)),
        "DECAWATT": ((0, 1), (10, -16)),
        "DECIWATT": ((0, 1), (10, -14)),
        "EXAWATT": ((0, 1), (10, -33)),
        "FEMTOWATT": (), # Same
        "GIGAWATT": ((0, 1), (10, -24)),
        "HECTOWATT": ((0, 1), (10, -17)),
        "KILOWATT": ((0, 1), (10, -18)),
        "MEGAWATT": ((0, 1), (10, -21)),
        "MICROWATT": ((0, 1), (10, -9)),
        "MILLIWATT": ((0, 1), (10, -12)),
        "NANOWATT": ((0, 1), (10, -6)),
        "PETAWATT": ((0, 1), (10, -30)),
        "PICOWATT": ((0, 1), (10, -3)),
        "TERAWATT": ((0, 1), (10, -27)),
        "WATT": ((0, 1), (10, -15)),
        "YOTTAWATT": ((0, 1), (10, -39)),
        "YOCTOWATT": ((0, 1), (10, 9)),
        "ZETTAWATT": ((0, 1), (10, -36)),
        "ZEPTOWATT": ((0, 1), (10, 6)),

    },
    "GIGAWATT": {
        "ATTOWATT": ((0, 1), (10, 27)),
        "CENTIWATT": ((0, 1), (10, 11)),
        "DECAWATT": ((0, 1), (10, 8)),
        "DECIWATT": ((0, 1), (10, 10)),
        "EXAWATT": ((0, 1), (10, -9)),
        "FEMTOWATT": ((0, 1), (10, 24)),
        "GIGAWATT": (), # Same
        "HECTOWATT": ((0, 1), (10, 7)),
        "KILOWATT": ((0, 1), (10, 6)),
        "MEGAWATT": ((0, 1), (10, 3)),
        "MICROWATT": ((0, 1), (10, 15)),
        "MILLIWATT": ((0, 1), (10, 12)),
        "NANOWATT": ((0, 1), (10, 18)),
        "PETAWATT": ((0, 1), (10, -6)),
        "PICOWATT": ((0, 1), (10, 21)),
        "TERAWATT": ((0, 1), (10, -3)),
        "WATT": ((0, 1), (10, 9)),
        "YOTTAWATT": ((0, 1), (10, -15)),
        "YOCTOWATT": ((0, 1), (10, 33)),
        "ZETTAWATT": ((0, 1), (10, -12)),
        "ZEPTOWATT": ((0, 1), (10, 30)),

    },
    "HECTOWATT": {
        "ATTOWATT": ((0, 1), (10, 20)),
        "CENTIWATT": ((0, 1), (10, 4)),
        "DECAWATT": ((0, 1), (10, 1)),
        "DECIWATT": ((0, 1), (10, 3)),
        "EXAWATT": ((0, 1), (10, -16)),
        "FEMTOWATT": ((0, 1), (10, 17)),
        "GIGAWATT": ((0, 1), (10, -7)),
        "HECTOWATT": (), # Same
        "KILOWATT": ((0, 1), (10, -1)),
        "MEGAWATT": ((0, 1), (10, -4)),
        "MICROWATT": ((0, 1), (10, 8)),
        "MILLIWATT": ((0, 1), (10, 5)),
        "NANOWATT": ((0, 1), (10, 11)),
        "PETAWATT": ((0, 1), (10, -13)),
        "PICOWATT": ((0, 1), (10, 14)),
        "TERAWATT": ((0, 1), (10, -10)),
        "WATT": ((0, 1), (10, 2)),
        "YOTTAWATT": ((0, 1), (10, -22)),
        "YOCTOWATT": ((0, 1), (10, 26)),
        "ZETTAWATT": ((0, 1), (10, -19)),
        "ZEPTOWATT": ((0, 1), (10, 23)),

    },
    "KILOWATT": {
        "ATTOWATT": ((0, 1), (10, 21)),
        "CENTIWATT": ((0, 1), (10, 5)),
        "DECAWATT": ((0, 1), (10, 2)),
        "DECIWATT": ((0, 1), (10, 4)),
        "EXAWATT": ((0, 1), (10, -15)),
        "FEMTOWATT": ((0, 1), (10, 18)),
        "GIGAWATT": ((0, 1), (10, -6)),
        "HECTOWATT": ((0, 1), (10, 1)),
        "KILOWATT": (), # Same
        "MEGAWATT": ((0, 1), (10, -3)),
        "MICROWATT": ((0, 1), (10, 9)),
        "MILLIWATT": ((0, 1), (10, 6)),
        "NANOWATT": ((0, 1), (10, 12)),
        "PETAWATT": ((0, 1), (10, -12)),
        "PICOWATT": ((0, 1), (10, 15)),
        "TERAWATT": ((0, 1), (10, -9)),
        "WATT": ((0, 1), (10, 3)),
        "YOTTAWATT": ((0, 1), (10, -21)),
        "YOCTOWATT": ((0, 1), (10, 27)),
        "ZETTAWATT": ((0, 1), (10, -18)),
        "ZEPTOWATT": ((0, 1), (10, 24)),

    },
    "MEGAWATT": {
        "ATTOWATT": ((0, 1), (10, 24)),
        "CENTIWATT": ((0, 1), (10, 8)),
        "DECAWATT": ((0, 1), (10, 5)),
        "DECIWATT": ((0, 1), (10, 7)),
        "EXAWATT": ((0, 1), (10, -12)),
        "FEMTOWATT": ((0, 1), (10, 21)),
        "GIGAWATT": ((0, 1), (10, -3)),
        "HECTOWATT": ((0, 1), (10, 4)),
        "KILOWATT": ((0, 1), (10, 3)),
        "MEGAWATT": (), # Same
        "MICROWATT": ((0, 1), (10, 12)),
        "MILLIWATT": ((0, 1), (10, 9)),
        "NANOWATT": ((0, 1), (10, 15)),
        "PETAWATT": ((0, 1), (10, -9)),
        "PICOWATT": ((0, 1), (10, 18)),
        "TERAWATT": ((0, 1), (10, -6)),
        "WATT": ((0, 1), (10, 6)),
        "YOTTAWATT": ((0, 1), (10, -18)),
        "YOCTOWATT": ((0, 1), (10, 30)),
        "ZETTAWATT": ((0, 1), (10, -15)),
        "ZEPTOWATT": ((0, 1), (10, 27)),

    },
    "MICROWATT": {
        "ATTOWATT": ((0, 1), (10, 12)),
        "CENTIWATT": ((0, 1), (10, -4)),
        "DECAWATT": ((0, 1), (10, -7)),
        "DECIWATT": ((0, 1), (10, -5)),
        "EXAWATT": ((0, 1), (10, -24)),
        "FEMTOWATT": ((0, 1), (10, 9)),
        "GIGAWATT": ((0, 1), (10, -15)),
        "HECTOWATT": ((0, 1), (10, -8)),
        "KILOWATT": ((0, 1), (10, -9)),
        "MEGAWATT": ((0, 1), (10, -12)),
        "MICROWATT": (), # Same
        "MILLIWATT": ((0, 1), (10, -3)),
        "NANOWATT": ((0, 1), (10, 3)),
        "PETAWATT": ((0, 1), (10, -21)),
        "PICOWATT": ((0, 1), (10, 6)),
        "TERAWATT": ((0, 1), (10, -18)),
        "WATT": ((0, 1), (10, -6)),
        "YOTTAWATT": ((0, 1), (10, -30)),
        "YOCTOWATT": ((0, 1), (10, 18)),
        "ZETTAWATT": ((0, 1), (10, -27)),
        "ZEPTOWATT": ((0, 1), (10, 15)),

    },
    "MILLIWATT": {
        "ATTOWATT": ((0, 1), (10, 15)),
        "CENTIWATT": ((0, 1), (10, -1)),
        "DECAWATT": ((0, 1), (10, -4)),
        "DECIWATT": ((0, 1), (10, -2)),
        "EXAWATT": ((0, 1), (10, -21)),
        "FEMTOWATT": ((0, 1), (10, 12)),
        "GIGAWATT": ((0, 1), (10, -12)),
        "HECTOWATT": ((0, 1), (10, -5)),
        "KILOWATT": ((0, 1), (10, -6)),
        "MEGAWATT": ((0, 1), (10, -9)),
        "MICROWATT": ((0, 1), (10, 3)),
        "MILLIWATT": (), # Same
        "NANOWATT": ((0, 1), (10, 6)),
        "PETAWATT": ((0, 1), (10, -18)),
        "PICOWATT": ((0, 1), (10, 9)),
        "TERAWATT": ((0, 1), (10, -15)),
        "WATT": ((0, 1), (10, -3)),
        "YOTTAWATT": ((0, 1), (10, -27)),
        "YOCTOWATT": ((0, 1), (10, 21)),
        "ZETTAWATT": ((0, 1), (10, -24)),
        "ZEPTOWATT": ((0, 1), (10, 18)),

    },
    "NANOWATT": {
        "ATTOWATT": ((0, 1), (10, 9)),
        "CENTIWATT": ((0, 1), (10, -7)),
        "DECAWATT": ((0, 1), (10, -10)),
        "DECIWATT": ((0, 1), (10, -8)),
        "EXAWATT": ((0, 1), (10, -27)),
        "FEMTOWATT": ((0, 1), (10, 6)),
        "GIGAWATT": ((0, 1), (10, -18)),
        "HECTOWATT": ((0, 1), (10, -11)),
        "KILOWATT": ((0, 1), (10, -12)),
        "MEGAWATT": ((0, 1), (10, -15)),
        "MICROWATT": ((0, 1), (10, -3)),
        "MILLIWATT": ((0, 1), (10, -6)),
        "NANOWATT": (), # Same
        "PETAWATT": ((0, 1), (10, -24)),
        "PICOWATT": ((0, 1), (10, 3)),
        "TERAWATT": ((0, 1), (10, -21)),
        "WATT": ((0, 1), (10, -9)),
        "YOTTAWATT": ((0, 1), (10, -33)),
        "YOCTOWATT": ((0, 1), (10, 15)),
        "ZETTAWATT": ((0, 1), (10, -30)),
        "ZEPTOWATT": ((0, 1), (10, 12)),

    },
    "PETAWATT": {
        "ATTOWATT": ((0, 1), (10, 33)),
        "CENTIWATT": ((0, 1), (10, 17)),
        "DECAWATT": ((0, 1), (10, 14)),
        "DECIWATT": ((0, 1), (10, 16)),
        "EXAWATT": ((0, 1), (10, -3)),
        "FEMTOWATT": ((0, 1), (10, 30)),
        "GIGAWATT": ((0, 1), (10, 6)),
        "HECTOWATT": ((0, 1), (10, 13)),
        "KILOWATT": ((0, 1), (10, 12)),
        "MEGAWATT": ((0, 1), (10, 9)),
        "MICROWATT": ((0, 1), (10, 21)),
        "MILLIWATT": ((0, 1), (10, 18)),
        "NANOWATT": ((0, 1), (10, 24)),
        "PETAWATT": (), # Same
        "PICOWATT": ((0, 1), (10, 27)),
        "TERAWATT": ((0, 1), (10, 3)),
        "WATT": ((0, 1), (10, 15)),
        "YOTTAWATT": ((0, 1), (10, -9)),
        "YOCTOWATT": ((0, 1), (10, 39)),
        "ZETTAWATT": ((0, 1), (10, -6)),
        "ZEPTOWATT": ((0, 1), (10, 36)),

    },
    "PICOWATT": {
        "ATTOWATT": ((0, 1), (10, 6)),
        "CENTIWATT": ((0, 1), (10, -10)),
        "DECAWATT": ((0, 1), (10, -13)),
        "DECIWATT": ((0, 1), (10, -11)),
        "EXAWATT": ((0, 1), (10, -30)),
        "FEMTOWATT": ((0, 1), (10, 3)),
        "GIGAWATT": ((0, 1), (10, -21)),
        "HECTOWATT": ((0, 1), (10, -14)),
        "KILOWATT": ((0, 1), (10, -15)),
        "MEGAWATT": ((0, 1), (10, -18)),
        "MICROWATT": ((0, 1), (10, -6)),
        "MILLIWATT": ((0, 1), (10, -9)),
        "NANOWATT": ((0, 1), (10, -3)),
        "PETAWATT": ((0, 1), (10, -27)),
        "PICOWATT": (), # Same
        "TERAWATT": ((0, 1), (10, -24)),
        "WATT": ((0, 1), (10, -12)),
        "YOTTAWATT": ((0, 1), (10, -36)),
        "YOCTOWATT": ((0, 1), (10, 12)),
        "ZETTAWATT": ((0, 1), (10, -33)),
        "ZEPTOWATT": ((0, 1), (10, 9)),

    },
    "TERAWATT": {
        "ATTOWATT": ((0, 1), (10, 30)),
        "CENTIWATT": ((0, 1), (10, 14)),
        "DECAWATT": ((0, 1), (10, 11)),
        "DECIWATT": ((0, 1), (10, 13)),
        "EXAWATT": ((0, 1), (10, -6)),
        "FEMTOWATT": ((0, 1), (10, 27)),
        "GIGAWATT": ((0, 1), (10, 3)),
        "HECTOWATT": ((0, 1), (10, 10)),
        "KILOWATT": ((0, 1), (10, 9)),
        "MEGAWATT": ((0, 1), (10, 6)),
        "MICROWATT": ((0, 1), (10, 18)),
        "MILLIWATT": ((0, 1), (10, 15)),
        "NANOWATT": ((0, 1), (10, 21)),
        "PETAWATT": ((0, 1), (10, -3)),
        "PICOWATT": ((0, 1), (10, 24)),
        "TERAWATT": (), # Same
        "WATT": ((0, 1), (10, 12)),
        "YOTTAWATT": ((0, 1), (10, -12)),
        "YOCTOWATT": ((0, 1), (10, 36)),
        "ZETTAWATT": ((0, 1), (10, -9)),
        "ZEPTOWATT": ((0, 1), (10, 33)),

    },
    "WATT": {
        "ATTOWATT": ((0, 1), (10, 18)),
        "CENTIWATT": ((0, 1), (10, 2)),
        "DECAWATT": ((0, 1), (10, -1)),
        "DECIWATT": ((0, 1), (10, 1)),
        "EXAWATT": ((0, 1), (10, -18)),
        "FEMTOWATT": ((0, 1), (10, 15)),
        "GIGAWATT": ((0, 1), (10, -9)),
        "HECTOWATT": ((0, 1), (10, -2)),
        "KILOWATT": ((0, 1), (10, -3)),
        "MEGAWATT": ((0, 1), (10, -6)),
        "MICROWATT": ((0, 1), (10, 6)),
        "MILLIWATT": ((0, 1), (10, 3)),
        "NANOWATT": ((0, 1), (10, 9)),
        "PETAWATT": ((0, 1), (10, -15)),
        "PICOWATT": ((0, 1), (10, 12)),
        "TERAWATT": ((0, 1), (10, -12)),
        "WATT": (), # Same
        "YOTTAWATT": ((0, 1), (10, -24)),
        "YOCTOWATT": ((0, 1), (10, 24)),
        "ZETTAWATT": ((0, 1), (10, -21)),
        "ZEPTOWATT": ((0, 1), (10, 21)),

    },
    "YOTTAWATT": {
        "ATTOWATT": ((0, 1), (10, 42)),
        "CENTIWATT": ((0, 1), (10, 26)),
        "DECAWATT": ((0, 1), (10, 23)),
        "DECIWATT": ((0, 1), (10, 25)),
        "EXAWATT": ((0, 1), (10, 6)),
        "FEMTOWATT": ((0, 1), (10, 39)),
        "GIGAWATT": ((0, 1), (10, 15)),
        "HECTOWATT": ((0, 1), (10, 22)),
        "KILOWATT": ((0, 1), (10, 21)),
        "MEGAWATT": ((0, 1), (10, 18)),
        "MICROWATT": ((0, 1), (10, 30)),
        "MILLIWATT": ((0, 1), (10, 27)),
        "NANOWATT": ((0, 1), (10, 33)),
        "PETAWATT": ((0, 1), (10, 9)),
        "PICOWATT": ((0, 1), (10, 36)),
        "TERAWATT": ((0, 1), (10, 12)),
        "WATT": ((0, 1), (10, 24)),
        "YOTTAWATT": (), # Same
        "YOCTOWATT": ((0, 1), (10, 48)),
        "ZETTAWATT": ((0, 1), (10, 3)),
        "ZEPTOWATT": ((0, 1), (10, 45)),

    },
    "YOCTOWATT": {
        "ATTOWATT": ((0, 1), (10, -6)),
        "CENTIWATT": ((0, 1), (10, -22)),
        "DECAWATT": ((0, 1), (10, -25)),
        "DECIWATT": ((0, 1), (10, -23)),
        "EXAWATT": ((0, 1), (10, -42)),
        "FEMTOWATT": ((0, 1), (10, -9)),
        "GIGAWATT": ((0, 1), (10, -33)),
        "HECTOWATT": ((0, 1), (10, -26)),
        "KILOWATT": ((0, 1), (10, -27)),
        "MEGAWATT": ((0, 1), (10, -30)),
        "MICROWATT": ((0, 1), (10, -18)),
        "MILLIWATT": ((0, 1), (10, -21)),
        "NANOWATT": ((0, 1), (10, -15)),
        "PETAWATT": ((0, 1), (10, -39)),
        "PICOWATT": ((0, 1), (10, -12)),
        "TERAWATT": ((0, 1), (10, -36)),
        "WATT": ((0, 1), (10, -24)),
        "YOTTAWATT": ((0, 1), (10, -48)),
        "YOCTOWATT": (), # Same
        "ZETTAWATT": ((0, 1), (10, -45)),
        "ZEPTOWATT": ((0, 1), (10, -3)),

    },
    "ZETTAWATT": {
        "ATTOWATT": ((0, 1), (10, 39)),
        "CENTIWATT": ((0, 1), (10, 23)),
        "DECAWATT": ((0, 1), (10, 20)),
        "DECIWATT": ((0, 1), (10, 22)),
        "EXAWATT": ((0, 1), (10, 3)),
        "FEMTOWATT": ((0, 1), (10, 36)),
        "GIGAWATT": ((0, 1), (10, 12)),
        "HECTOWATT": ((0, 1), (10, 19)),
        "KILOWATT": ((0, 1), (10, 18)),
        "MEGAWATT": ((0, 1), (10, 15)),
        "MICROWATT": ((0, 1), (10, 27)),
        "MILLIWATT": ((0, 1), (10, 24)),
        "NANOWATT": ((0, 1), (10, 30)),
        "PETAWATT": ((0, 1), (10, 6)),
        "PICOWATT": ((0, 1), (10, 33)),
        "TERAWATT": ((0, 1), (10, 9)),
        "WATT": ((0, 1), (10, 21)),
        "YOTTAWATT": ((0, 1), (10, -3)),
        "YOCTOWATT": ((0, 1), (10, 45)),
        "ZETTAWATT": (), # Same
        "ZEPTOWATT": ((0, 1), (10, 42)),

    },
    "ZEPTOWATT": {
        "ATTOWATT": ((0, 1), (10, -3)),
        "CENTIWATT": ((0, 1), (10, -19)),
        "DECAWATT": ((0, 1), (10, -22)),
        "DECIWATT": ((0, 1), (10, -20)),
        "EXAWATT": ((0, 1), (10, -39)),
        "FEMTOWATT": ((0, 1), (10, -6)),
        "GIGAWATT": ((0, 1), (10, -30)),
        "HECTOWATT": ((0, 1), (10, -23)),
        "KILOWATT": ((0, 1), (10, -24)),
        "MEGAWATT": ((0, 1), (10, -27)),
        "MICROWATT": ((0, 1), (10, -15)),
        "MILLIWATT": ((0, 1), (10, -18)),
        "NANOWATT": ((0, 1), (10, -12)),
        "PETAWATT": ((0, 1), (10, -36)),
        "PICOWATT": ((0, 1), (10, -9)),
        "TERAWATT": ((0, 1), (10, -33)),
        "WATT": ((0, 1), (10, -21)),
        "YOTTAWATT": ((0, 1), (10, -45)),
        "YOCTOWATT": ((0, 1), (10, 3)),
        "ZETTAWATT": ((0, 1), (10, -42)),
        "ZEPTOWATT": (), # Same

    },

  },
  "Pressure": {
    "ATTOPASCAL": {
        "ATTOPASCAL": (), # Same
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, -16)),
        "DECAPASCAL": ((0, 1), (10, -19)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -17)),
        "EXAPASCAL": ((0, 1), (10, -36)),
        "FEMTOPASCAL": ((0, 1), (10, -3)),
        "GIGAPASCAL": ((0, 1), (10, -27)),
        "HECTOPASCAL": ((0, 1), (10, -20)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -21)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -24)),
        "MICROPASCAL": ((0, 1), (10, -12)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, -15)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, -9)),
        "Pascal": ((0, 1), (10, -18)),
        "PETAPASCAL": ((0, 1), (10, -33)),
        "PICOPASCAL": ((0, 1), (10, -6)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -30)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -42)),
        "YOCTOPASCAL": ((0, 1), (10, 6)),
        "ZETTAPASCAL": ((0, 1), (10, -39)),
        "ZEPTOPASCAL": ((0, 1), (10, 3)),

    },
    "ATMOSPHERE": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (), # Same
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "BAR": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (), # Same
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "CENTIBAR": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (), # Same
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "CENTIPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 16)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (), # Same
        "DECAPASCAL": ((0, 1), (10, -3)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -1)),
        "EXAPASCAL": ((0, 1), (10, -20)),
        "FEMTOPASCAL": ((0, 1), (10, 13)),
        "GIGAPASCAL": ((0, 1), (10, -11)),
        "HECTOPASCAL": ((0, 1), (10, -4)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -5)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -8)),
        "MICROPASCAL": ((0, 1), (10, 4)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 1)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 7)),
        "Pascal": ((0, 1), (10, -2)),
        "PETAPASCAL": ((0, 1), (10, -17)),
        "PICOPASCAL": ((0, 1), (10, 10)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -14)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -26)),
        "YOCTOPASCAL": ((0, 1), (10, 22)),
        "ZETTAPASCAL": ((0, 1), (10, -23)),
        "ZEPTOPASCAL": ((0, 1), (10, 19)),

    },
    "DECAPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 19)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 3)),
        "DECAPASCAL": (), # Same
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 2)),
        "EXAPASCAL": ((0, 1), (10, -17)),
        "FEMTOPASCAL": ((0, 1), (10, 16)),
        "GIGAPASCAL": ((0, 1), (10, -8)),
        "HECTOPASCAL": ((0, 1), (10, -1)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -2)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -5)),
        "MICROPASCAL": ((0, 1), (10, 7)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 4)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 10)),
        "Pascal": ((0, 1), (10, 1)),
        "PETAPASCAL": ((0, 1), (10, -14)),
        "PICOPASCAL": ((0, 1), (10, 13)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -11)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -23)),
        "YOCTOPASCAL": ((0, 1), (10, 25)),
        "ZETTAPASCAL": ((0, 1), (10, -20)),
        "ZEPTOPASCAL": ((0, 1), (10, 22)),

    },
    "DECIBAR": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (), # Same
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "DECIPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 17)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 1)),
        "DECAPASCAL": ((0, 1), (10, -2)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (), # Same
        "EXAPASCAL": ((0, 1), (10, -19)),
        "FEMTOPASCAL": ((0, 1), (10, 14)),
        "GIGAPASCAL": ((0, 1), (10, -10)),
        "HECTOPASCAL": ((0, 1), (10, -3)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -4)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -7)),
        "MICROPASCAL": ((0, 1), (10, 5)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 2)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 8)),
        "Pascal": ((0, 1), (10, -1)),
        "PETAPASCAL": ((0, 1), (10, -16)),
        "PICOPASCAL": ((0, 1), (10, 11)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -13)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -25)),
        "YOCTOPASCAL": ((0, 1), (10, 23)),
        "ZETTAPASCAL": ((0, 1), (10, -22)),
        "ZEPTOPASCAL": ((0, 1), (10, 20)),

    },
    "EXAPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 36)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 20)),
        "DECAPASCAL": ((0, 1), (10, 17)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 19)),
        "EXAPASCAL": (), # Same
        "FEMTOPASCAL": ((0, 1), (10, 33)),
        "GIGAPASCAL": ((0, 1), (10, 9)),
        "HECTOPASCAL": ((0, 1), (10, 16)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, 15)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, 12)),
        "MICROPASCAL": ((0, 1), (10, 24)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 21)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 27)),
        "Pascal": ((0, 1), (10, 18)),
        "PETAPASCAL": ((0, 1), (10, 3)),
        "PICOPASCAL": ((0, 1), (10, 30)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, 6)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -6)),
        "YOCTOPASCAL": ((0, 1), (10, 42)),
        "ZETTAPASCAL": ((0, 1), (10, -3)),
        "ZEPTOPASCAL": ((0, 1), (10, 39)),

    },
    "FEMTOPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 3)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, -13)),
        "DECAPASCAL": ((0, 1), (10, -16)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -14)),
        "EXAPASCAL": ((0, 1), (10, -33)),
        "FEMTOPASCAL": (), # Same
        "GIGAPASCAL": ((0, 1), (10, -24)),
        "HECTOPASCAL": ((0, 1), (10, -17)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -18)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -21)),
        "MICROPASCAL": ((0, 1), (10, -9)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, -12)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, -6)),
        "Pascal": ((0, 1), (10, -15)),
        "PETAPASCAL": ((0, 1), (10, -30)),
        "PICOPASCAL": ((0, 1), (10, -3)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -27)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -39)),
        "YOCTOPASCAL": ((0, 1), (10, 9)),
        "ZETTAPASCAL": ((0, 1), (10, -36)),
        "ZEPTOPASCAL": ((0, 1), (10, 6)),

    },
    "GIGAPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 27)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 11)),
        "DECAPASCAL": ((0, 1), (10, 8)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 10)),
        "EXAPASCAL": ((0, 1), (10, -9)),
        "FEMTOPASCAL": ((0, 1), (10, 24)),
        "GIGAPASCAL": (), # Same
        "HECTOPASCAL": ((0, 1), (10, 7)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, 6)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, 3)),
        "MICROPASCAL": ((0, 1), (10, 15)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 12)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 18)),
        "Pascal": ((0, 1), (10, 9)),
        "PETAPASCAL": ((0, 1), (10, -6)),
        "PICOPASCAL": ((0, 1), (10, 21)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -3)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -15)),
        "YOCTOPASCAL": ((0, 1), (10, 33)),
        "ZETTAPASCAL": ((0, 1), (10, -12)),
        "ZEPTOPASCAL": ((0, 1), (10, 30)),

    },
    "HECTOPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 20)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 4)),
        "DECAPASCAL": ((0, 1), (10, 1)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 3)),
        "EXAPASCAL": ((0, 1), (10, -16)),
        "FEMTOPASCAL": ((0, 1), (10, 17)),
        "GIGAPASCAL": ((0, 1), (10, -7)),
        "HECTOPASCAL": (), # Same
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -1)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -4)),
        "MICROPASCAL": ((0, 1), (10, 8)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 5)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 11)),
        "Pascal": ((0, 1), (10, 2)),
        "PETAPASCAL": ((0, 1), (10, -13)),
        "PICOPASCAL": ((0, 1), (10, 14)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -10)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -22)),
        "YOCTOPASCAL": ((0, 1), (10, 26)),
        "ZETTAPASCAL": ((0, 1), (10, -19)),
        "ZEPTOPASCAL": ((0, 1), (10, 23)),

    },
    "KILOBAR": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (), # Same
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "KILOPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 21)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 5)),
        "DECAPASCAL": ((0, 1), (10, 2)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 4)),
        "EXAPASCAL": ((0, 1), (10, -15)),
        "FEMTOPASCAL": ((0, 1), (10, 18)),
        "GIGAPASCAL": ((0, 1), (10, -6)),
        "HECTOPASCAL": ((0, 1), (10, 1)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (), # Same
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -3)),
        "MICROPASCAL": ((0, 1), (10, 9)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 6)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 12)),
        "Pascal": ((0, 1), (10, 3)),
        "PETAPASCAL": ((0, 1), (10, -12)),
        "PICOPASCAL": ((0, 1), (10, 15)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -9)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -21)),
        "YOCTOPASCAL": ((0, 1), (10, 27)),
        "ZETTAPASCAL": ((0, 1), (10, -18)),
        "ZEPTOPASCAL": ((0, 1), (10, 24)),

    },
    "MILLIBAR": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (), # Same
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "MEGABAR": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (), # Same
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "MEGAPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 24)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 8)),
        "DECAPASCAL": ((0, 1), (10, 5)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 7)),
        "EXAPASCAL": ((0, 1), (10, -12)),
        "FEMTOPASCAL": ((0, 1), (10, 21)),
        "GIGAPASCAL": ((0, 1), (10, -3)),
        "HECTOPASCAL": ((0, 1), (10, 4)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, 3)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (), # Same
        "MICROPASCAL": ((0, 1), (10, 12)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 9)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 15)),
        "Pascal": ((0, 1), (10, 6)),
        "PETAPASCAL": ((0, 1), (10, -9)),
        "PICOPASCAL": ((0, 1), (10, 18)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -6)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -18)),
        "YOCTOPASCAL": ((0, 1), (10, 30)),
        "ZETTAPASCAL": ((0, 1), (10, -15)),
        "ZEPTOPASCAL": ((0, 1), (10, 27)),

    },
    "MICROPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 12)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, -4)),
        "DECAPASCAL": ((0, 1), (10, -7)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -5)),
        "EXAPASCAL": ((0, 1), (10, -24)),
        "FEMTOPASCAL": ((0, 1), (10, 9)),
        "GIGAPASCAL": ((0, 1), (10, -15)),
        "HECTOPASCAL": ((0, 1), (10, -8)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -9)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -12)),
        "MICROPASCAL": (), # Same
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, -3)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 3)),
        "Pascal": ((0, 1), (10, -6)),
        "PETAPASCAL": ((0, 1), (10, -21)),
        "PICOPASCAL": ((0, 1), (10, 6)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -18)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -30)),
        "YOCTOPASCAL": ((0, 1), (10, 18)),
        "ZETTAPASCAL": ((0, 1), (10, -27)),
        "ZEPTOPASCAL": ((0, 1), (10, 15)),

    },
    "MMHG": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (), # Same
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "MILLIPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 15)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, -1)),
        "DECAPASCAL": ((0, 1), (10, -4)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -2)),
        "EXAPASCAL": ((0, 1), (10, -21)),
        "FEMTOPASCAL": ((0, 1), (10, 12)),
        "GIGAPASCAL": ((0, 1), (10, -12)),
        "HECTOPASCAL": ((0, 1), (10, -5)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -6)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -9)),
        "MICROPASCAL": ((0, 1), (10, 3)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (), # Same
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 6)),
        "Pascal": ((0, 1), (10, -3)),
        "PETAPASCAL": ((0, 1), (10, -18)),
        "PICOPASCAL": ((0, 1), (10, 9)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -15)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -27)),
        "YOCTOPASCAL": ((0, 1), (10, 21)),
        "ZETTAPASCAL": ((0, 1), (10, -24)),
        "ZEPTOPASCAL": ((0, 1), (10, 18)),

    },
    "MILLITORR": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (), # Same
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "NANOPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 9)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, -7)),
        "DECAPASCAL": ((0, 1), (10, -10)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -8)),
        "EXAPASCAL": ((0, 1), (10, -27)),
        "FEMTOPASCAL": ((0, 1), (10, 6)),
        "GIGAPASCAL": ((0, 1), (10, -18)),
        "HECTOPASCAL": ((0, 1), (10, -11)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -12)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -15)),
        "MICROPASCAL": ((0, 1), (10, -3)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, -6)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (), # Same
        "Pascal": ((0, 1), (10, -9)),
        "PETAPASCAL": ((0, 1), (10, -24)),
        "PICOPASCAL": ((0, 1), (10, 3)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -21)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -33)),
        "YOCTOPASCAL": ((0, 1), (10, 15)),
        "ZETTAPASCAL": ((0, 1), (10, -30)),
        "ZEPTOPASCAL": ((0, 1), (10, 12)),

    },
    "Pascal": {
        "ATTOPASCAL": ((0, 1), (10, 18)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 2)),
        "DECAPASCAL": ((0, 1), (10, -1)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 1)),
        "EXAPASCAL": ((0, 1), (10, -18)),
        "FEMTOPASCAL": ((0, 1), (10, 15)),
        "GIGAPASCAL": ((0, 1), (10, -9)),
        "HECTOPASCAL": ((0, 1), (10, -2)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -3)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -6)),
        "MICROPASCAL": ((0, 1), (10, 6)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 3)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 9)),
        "Pascal": (), # Same
        "PETAPASCAL": ((0, 1), (10, -15)),
        "PICOPASCAL": ((0, 1), (10, 12)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -12)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -24)),
        "YOCTOPASCAL": ((0, 1), (10, 24)),
        "ZETTAPASCAL": ((0, 1), (10, -21)),
        "ZEPTOPASCAL": ((0, 1), (10, 21)),

    },
    "PETAPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 33)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 17)),
        "DECAPASCAL": ((0, 1), (10, 14)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 16)),
        "EXAPASCAL": ((0, 1), (10, -3)),
        "FEMTOPASCAL": ((0, 1), (10, 30)),
        "GIGAPASCAL": ((0, 1), (10, 6)),
        "HECTOPASCAL": ((0, 1), (10, 13)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, 12)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, 9)),
        "MICROPASCAL": ((0, 1), (10, 21)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 18)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 24)),
        "Pascal": ((0, 1), (10, 15)),
        "PETAPASCAL": (), # Same
        "PICOPASCAL": ((0, 1), (10, 27)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, 3)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -9)),
        "YOCTOPASCAL": ((0, 1), (10, 39)),
        "ZETTAPASCAL": ((0, 1), (10, -6)),
        "ZEPTOPASCAL": ((0, 1), (10, 36)),

    },
    "PICOPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 6)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, -10)),
        "DECAPASCAL": ((0, 1), (10, -13)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -11)),
        "EXAPASCAL": ((0, 1), (10, -30)),
        "FEMTOPASCAL": ((0, 1), (10, 3)),
        "GIGAPASCAL": ((0, 1), (10, -21)),
        "HECTOPASCAL": ((0, 1), (10, -14)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -15)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -18)),
        "MICROPASCAL": ((0, 1), (10, -6)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, -9)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, -3)),
        "Pascal": ((0, 1), (10, -12)),
        "PETAPASCAL": ((0, 1), (10, -27)),
        "PICOPASCAL": (), # Same
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -24)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -36)),
        "YOCTOPASCAL": ((0, 1), (10, 12)),
        "ZETTAPASCAL": ((0, 1), (10, -33)),
        "ZEPTOPASCAL": ((0, 1), (10, 9)),

    },
    "PSI": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (), # Same
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "TERAPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 30)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 14)),
        "DECAPASCAL": ((0, 1), (10, 11)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 13)),
        "EXAPASCAL": ((0, 1), (10, -6)),
        "FEMTOPASCAL": ((0, 1), (10, 27)),
        "GIGAPASCAL": ((0, 1), (10, 3)),
        "HECTOPASCAL": ((0, 1), (10, 10)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, 9)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, 6)),
        "MICROPASCAL": ((0, 1), (10, 18)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 15)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 21)),
        "Pascal": ((0, 1), (10, 12)),
        "PETAPASCAL": ((0, 1), (10, -3)),
        "PICOPASCAL": ((0, 1), (10, 24)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (), # Same
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -12)),
        "YOCTOPASCAL": ((0, 1), (10, 36)),
        "ZETTAPASCAL": ((0, 1), (10, -9)),
        "ZEPTOPASCAL": ((0, 1), (10, 33)),

    },
    "TORR": {
        "ATTOPASCAL": (None,),  # Undefined
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": (None,),  # Undefined
        "DECAPASCAL": (None,),  # Undefined
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": (None,),  # Undefined
        "EXAPASCAL": (None,),  # Undefined
        "FEMTOPASCAL": (None,),  # Undefined
        "GIGAPASCAL": (None,),  # Undefined
        "HECTOPASCAL": (None,),  # Undefined
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": (None,),  # Undefined
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": (None,),  # Undefined
        "MICROPASCAL": (None,),  # Undefined
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": (None,),  # Undefined
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": (None,),  # Undefined
        "Pascal": (None,),  # Undefined
        "PETAPASCAL": (None,),  # Undefined
        "PICOPASCAL": (None,),  # Undefined
        "PSI": (None,),  # Undefined
        "TERAPASCAL": (None,),  # Undefined
        "TORR": (), # Same
        "YOTTAPASCAL": (None,),  # Undefined
        "YOCTOPASCAL": (None,),  # Undefined
        "ZETTAPASCAL": (None,),  # Undefined
        "ZEPTOPASCAL": (None,),  # Undefined

    },
    "YOTTAPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 42)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 26)),
        "DECAPASCAL": ((0, 1), (10, 23)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 25)),
        "EXAPASCAL": ((0, 1), (10, 6)),
        "FEMTOPASCAL": ((0, 1), (10, 39)),
        "GIGAPASCAL": ((0, 1), (10, 15)),
        "HECTOPASCAL": ((0, 1), (10, 22)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, 21)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, 18)),
        "MICROPASCAL": ((0, 1), (10, 30)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 27)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 33)),
        "Pascal": ((0, 1), (10, 24)),
        "PETAPASCAL": ((0, 1), (10, 9)),
        "PICOPASCAL": ((0, 1), (10, 36)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, 12)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": (), # Same
        "YOCTOPASCAL": ((0, 1), (10, 48)),
        "ZETTAPASCAL": ((0, 1), (10, 3)),
        "ZEPTOPASCAL": ((0, 1), (10, 45)),

    },
    "YOCTOPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, -6)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, -22)),
        "DECAPASCAL": ((0, 1), (10, -25)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -23)),
        "EXAPASCAL": ((0, 1), (10, -42)),
        "FEMTOPASCAL": ((0, 1), (10, -9)),
        "GIGAPASCAL": ((0, 1), (10, -33)),
        "HECTOPASCAL": ((0, 1), (10, -26)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -27)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -30)),
        "MICROPASCAL": ((0, 1), (10, -18)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, -21)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, -15)),
        "Pascal": ((0, 1), (10, -24)),
        "PETAPASCAL": ((0, 1), (10, -39)),
        "PICOPASCAL": ((0, 1), (10, -12)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -36)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -48)),
        "YOCTOPASCAL": (), # Same
        "ZETTAPASCAL": ((0, 1), (10, -45)),
        "ZEPTOPASCAL": ((0, 1), (10, -3)),

    },
    "ZETTAPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, 39)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, 23)),
        "DECAPASCAL": ((0, 1), (10, 20)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, 22)),
        "EXAPASCAL": ((0, 1), (10, 3)),
        "FEMTOPASCAL": ((0, 1), (10, 36)),
        "GIGAPASCAL": ((0, 1), (10, 12)),
        "HECTOPASCAL": ((0, 1), (10, 19)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, 18)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, 15)),
        "MICROPASCAL": ((0, 1), (10, 27)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, 24)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, 30)),
        "Pascal": ((0, 1), (10, 21)),
        "PETAPASCAL": ((0, 1), (10, 6)),
        "PICOPASCAL": ((0, 1), (10, 33)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, 9)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -3)),
        "YOCTOPASCAL": ((0, 1), (10, 45)),
        "ZETTAPASCAL": (), # Same
        "ZEPTOPASCAL": ((0, 1), (10, 42)),

    },
    "ZEPTOPASCAL": {
        "ATTOPASCAL": ((0, 1), (10, -3)),
        "ATMOSPHERE": (None,),  # Undefined
        "BAR": (None,),  # Undefined
        "CENTIBAR": (None,),  # Undefined
        "CENTIPASCAL": ((0, 1), (10, -19)),
        "DECAPASCAL": ((0, 1), (10, -22)),
        "DECIBAR": (None,),  # Undefined
        "DECIPASCAL": ((0, 1), (10, -20)),
        "EXAPASCAL": ((0, 1), (10, -39)),
        "FEMTOPASCAL": ((0, 1), (10, -6)),
        "GIGAPASCAL": ((0, 1), (10, -30)),
        "HECTOPASCAL": ((0, 1), (10, -23)),
        "KILOBAR": (None,),  # Undefined
        "KILOPASCAL": ((0, 1), (10, -24)),
        "MILLIBAR": (None,),  # Undefined
        "MEGABAR": (None,),  # Undefined
        "MEGAPASCAL": ((0, 1), (10, -27)),
        "MICROPASCAL": ((0, 1), (10, -15)),
        "MMHG": (None,),  # Undefined
        "MILLIPASCAL": ((0, 1), (10, -18)),
        "MILLITORR": (None,),  # Undefined
        "NANOPASCAL": ((0, 1), (10, -12)),
        "Pascal": ((0, 1), (10, -21)),
        "PETAPASCAL": ((0, 1), (10, -36)),
        "PICOPASCAL": ((0, 1), (10, -9)),
        "PSI": (None,),  # Undefined
        "TERAPASCAL": ((0, 1), (10, -33)),
        "TORR": (None,),  # Undefined
        "YOTTAPASCAL": ((0, 1), (10, -45)),
        "YOCTOPASCAL": ((0, 1), (10, 3)),
        "ZETTAPASCAL": ((0, 1), (10, -42)),
        "ZEPTOPASCAL": (), # Same

    },

  },
  "Temperature": {
    "CELSIUS": {
        "CELSIUS": (), # Same
        "FAHRENHEIT": ((32, 1), (1.8, 1)),
        "RANKINE": (None,),  # Undefined
        "KELVIN": ((273.15, 1), (1, 0)),

    },
    "FAHRENHEIT": {
        "CELSIUS": ((-17.777777777, 1), (0.55555555555, 1)),
        "FAHRENHEIT": (), # Same
        "RANKINE": (None,),  # Undefined
        "KELVIN": (None,),  # Undefined

    },
    "RANKINE": {
        "CELSIUS": (None,),  # Undefined
        "FAHRENHEIT": (None,),  # Undefined
        "RANKINE": (), # Same
        "KELVIN": (None,),  # Undefined

    },
    "KELVIN": {
        "CELSIUS": ((-273.15, 1), (1, 0)),
        "FAHRENHEIT": (None,),  # Undefined
        "RANKINE": (None,),  # Undefined
        "KELVIN": (), # Same

    },

  },
  "Time": {
    "ATOOSECOND": {
        "ATOOSECOND": (), # Same
        "CENTISECOND": ((0, 1), (10, -16)),
        "DAY": ((0, 1), (10, -18, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -19)),
        "DECISECOND": ((0, 1), (10, -17)),
        "EXASECOND": ((0, 1), (10, -36)),
        "FEMTOSECOND": ((0, 1), (10, -3)),
        "GIGASECOND": ((0, 1), (10, -27)),
        "HOUR": ((0, 1), (10, -18, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -20)),
        "KILOSECOND": ((0, 1), (10, -21)),
        "MEGASECOND": ((0, 1), (10, -24)),
        "MICROSECOND": ((0, 1), (10, -12)),
        "MINUTE": ((0, 1), (10, -18, 60, -1)),
        "MILLISECOND": ((0, 1), (10, -15)),
        "NANOSECOND": ((0, 1), (10, -9)),
        "PETASECOND": ((0, 1), (10, -33)),
        "PICOSECOND": ((0, 1), (10, -6)),
        "SECOND": ((0, 1), (10, -18)),
        "TERASECOND": ((0, 1), (10, -30)),
        "YOTTASECOND": ((0, 1), (10, -42)),
        "YOCTOSECOND": ((0, 1), (10, 6)),
        "ZETTASECOND": ((0, 1), (10, -39)),
        "ZEPTOSECOND": ((0, 1), (10, 3)),

    },
    "CENTISECOND": {
        "ATOOSECOND": ((0, 1), (10, 16)),
        "CENTISECOND": (), # Same
        "DAY": ((0, 1), (10, -2, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -3)),
        "DECISECOND": ((0, 1), (10, -1)),
        "EXASECOND": ((0, 1), (10, -20)),
        "FEMTOSECOND": ((0, 1), (10, 13)),
        "GIGASECOND": ((0, 1), (10, -11)),
        "HOUR": ((0, 1), (10, -2, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -4)),
        "KILOSECOND": ((0, 1), (10, -5)),
        "MEGASECOND": ((0, 1), (10, -8)),
        "MICROSECOND": ((0, 1), (10, 4)),
        "MINUTE": ((0, 1), (10, -2, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 1)),
        "NANOSECOND": ((0, 1), (10, 7)),
        "PETASECOND": ((0, 1), (10, -17)),
        "PICOSECOND": ((0, 1), (10, 10)),
        "SECOND": ((0, 1), (10, -2)),
        "TERASECOND": ((0, 1), (10, -14)),
        "YOTTASECOND": ((0, 1), (10, -26)),
        "YOCTOSECOND": ((0, 1), (10, 22)),
        "ZETTASECOND": ((0, 1), (10, -23)),
        "ZEPTOSECOND": ((0, 1), (10, 19)),

    },
    "DAY": {
        "ATOOSECOND": ((0, 1), (10, 18, 24*60*60, 1)),
        "CENTISECOND": ((0, 1), (10, 2, 24*60*60, 1)),
        "DAY": (), # Same
        "DECASECOND": ((0, 1), (10, -1, 24*60*60, 1)),
        "DECISECOND": ((0, 1), (10, 1, 24*60*60, 1)),
        "EXASECOND": ((0, 1), (10, -18, 24*60*60, 1)),
        "FEMTOSECOND": ((0, 1), (10, 15, 24*60*60, 1)),
        "GIGASECOND": ((0, 1), (10, -9, 24*60*60, 1)),
        "HOUR": ((0, 1), (24, 1)),
        "HECTOSECOND": ((0, 1), (10, -2, 24*60*60, 1)),
        "KILOSECOND": ((0, 1), (10, -3, 24*60*60, 1)),
        "MEGASECOND": ((0, 1), (10, -6, 24*60*60, 1)),
        "MICROSECOND": ((0, 1), (10, 6, 24*60*60, 1)),
        "MINUTE": ((0, 1), (24*60, 1)),
        "MILLISECOND": ((0, 1), (10, 3, 24*60*60, 1)),
        "NANOSECOND": ((0, 1), (10, 9, 24*60*60, 1)),
        "PETASECOND": ((0, 1), (10, -15, 24*60*60, 1)),
        "PICOSECOND": ((0, 1), (10, 12, 24*60*60, 1)),
        "SECOND": ((0, 1), (24*60*60, 1)),
        "TERASECOND": ((0, 1), (10, -12, 24*60*60, 1)),
        "YOTTASECOND": ((0, 1), (10, -24, 24*60*60, 1)),
        "YOCTOSECOND": ((0, 1), (10, 24, 24*60*60, 1)),
        "ZETTASECOND": ((0, 1), (10, -21, 24*60*60, 1)),
        "ZEPTOSECOND": ((0, 1), (10, 21, 24*60*60, 1)),

    },
    "DECASECOND": {
        "ATOOSECOND": ((0, 1), (10, 19)),
        "CENTISECOND": ((0, 1), (10, 3)),
        "DAY": ((0, 1), (10, 1, 86400, -1)),
        "DECASECOND": (), # Same
        "DECISECOND": ((0, 1), (10, 2)),
        "EXASECOND": ((0, 1), (10, -17)),
        "FEMTOSECOND": ((0, 1), (10, 16)),
        "GIGASECOND": ((0, 1), (10, -8)),
        "HOUR": ((0, 1), (10, 1, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -1)),
        "KILOSECOND": ((0, 1), (10, -2)),
        "MEGASECOND": ((0, 1), (10, -5)),
        "MICROSECOND": ((0, 1), (10, 7)),
        "MINUTE": ((0, 1), (10, 1, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 4)),
        "NANOSECOND": ((0, 1), (10, 10)),
        "PETASECOND": ((0, 1), (10, -14)),
        "PICOSECOND": ((0, 1), (10, 13)),
        "SECOND": ((0, 1), (10, 1)),
        "TERASECOND": ((0, 1), (10, -11)),
        "YOTTASECOND": ((0, 1), (10, -23)),
        "YOCTOSECOND": ((0, 1), (10, 25)),
        "ZETTASECOND": ((0, 1), (10, -20)),
        "ZEPTOSECOND": ((0, 1), (10, 22)),

    },
    "DECISECOND": {
        "ATOOSECOND": ((0, 1), (10, 17)),
        "CENTISECOND": ((0, 1), (10, 1)),
        "DAY": ((0, 1), (10, -1, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -2)),
        "DECISECOND": (), # Same
        "EXASECOND": ((0, 1), (10, -19)),
        "FEMTOSECOND": ((0, 1), (10, 14)),
        "GIGASECOND": ((0, 1), (10, -10)),
        "HOUR": ((0, 1), (10, -1, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -3)),
        "KILOSECOND": ((0, 1), (10, -4)),
        "MEGASECOND": ((0, 1), (10, -7)),
        "MICROSECOND": ((0, 1), (10, 5)),
        "MINUTE": ((0, 1), (10, -1, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 2)),
        "NANOSECOND": ((0, 1), (10, 8)),
        "PETASECOND": ((0, 1), (10, -16)),
        "PICOSECOND": ((0, 1), (10, 11)),
        "SECOND": ((0, 1), (10, -1)),
        "TERASECOND": ((0, 1), (10, -13)),
        "YOTTASECOND": ((0, 1), (10, -25)),
        "YOCTOSECOND": ((0, 1), (10, 23)),
        "ZETTASECOND": ((0, 1), (10, -22)),
        "ZEPTOSECOND": ((0, 1), (10, 20)),

    },
    "EXASECOND": {
        "ATOOSECOND": ((0, 1), (10, 36)),
        "CENTISECOND": ((0, 1), (10, 20)),
        "DAY": ((0, 1), (10, 18, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 17)),
        "DECISECOND": ((0, 1), (10, 19)),
        "EXASECOND": (), # Same
        "FEMTOSECOND": ((0, 1), (10, 33)),
        "GIGASECOND": ((0, 1), (10, 9)),
        "HOUR": ((0, 1), (10, 18, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, 16)),
        "KILOSECOND": ((0, 1), (10, 15)),
        "MEGASECOND": ((0, 1), (10, 12)),
        "MICROSECOND": ((0, 1), (10, 24)),
        "MINUTE": ((0, 1), (10, 18, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 21)),
        "NANOSECOND": ((0, 1), (10, 27)),
        "PETASECOND": ((0, 1), (10, 3)),
        "PICOSECOND": ((0, 1), (10, 30)),
        "SECOND": ((0, 1), (10, 18)),
        "TERASECOND": ((0, 1), (10, 6)),
        "YOTTASECOND": ((0, 1), (10, -6)),
        "YOCTOSECOND": ((0, 1), (10, 42)),
        "ZETTASECOND": ((0, 1), (10, -3)),
        "ZEPTOSECOND": ((0, 1), (10, 39)),

    },
    "FEMTOSECOND": {
        "ATOOSECOND": ((0, 1), (10, 3)),
        "CENTISECOND": ((0, 1), (10, -13)),
        "DAY": ((0, 1), (10, -15, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -16)),
        "DECISECOND": ((0, 1), (10, -14)),
        "EXASECOND": ((0, 1), (10, -33)),
        "FEMTOSECOND": (), # Same
        "GIGASECOND": ((0, 1), (10, -24)),
        "HOUR": ((0, 1), (10, -15, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -17)),
        "KILOSECOND": ((0, 1), (10, -18)),
        "MEGASECOND": ((0, 1), (10, -21)),
        "MICROSECOND": ((0, 1), (10, -9)),
        "MINUTE": ((0, 1), (10, -15, 60, -1)),
        "MILLISECOND": ((0, 1), (10, -12)),
        "NANOSECOND": ((0, 1), (10, -6)),
        "PETASECOND": ((0, 1), (10, -30)),
        "PICOSECOND": ((0, 1), (10, -3)),
        "SECOND": ((0, 1), (10, -15)),
        "TERASECOND": ((0, 1), (10, -27)),
        "YOTTASECOND": ((0, 1), (10, -39)),
        "YOCTOSECOND": ((0, 1), (10, 9)),
        "ZETTASECOND": ((0, 1), (10, -36)),
        "ZEPTOSECOND": ((0, 1), (10, 6)),

    },
    "GIGASECOND": {
        "ATOOSECOND": ((0, 1), (10, 27)),
        "CENTISECOND": ((0, 1), (10, 11)),
        "DAY": ((0, 1), (10, 9, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 8)),
        "DECISECOND": ((0, 1), (10, 10)),
        "EXASECOND": ((0, 1), (10, -9)),
        "FEMTOSECOND": ((0, 1), (10, 24)),
        "GIGASECOND": (), # Same
        "HOUR": ((0, 1), (10, 9, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, 7)),
        "KILOSECOND": ((0, 1), (10, 6)),
        "MEGASECOND": ((0, 1), (10, 3)),
        "MICROSECOND": ((0, 1), (10, 15)),
        "MINUTE": ((0, 1), (10, 9, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 12)),
        "NANOSECOND": ((0, 1), (10, 18)),
        "PETASECOND": ((0, 1), (10, -6)),
        "PICOSECOND": ((0, 1), (10, 21)),
        "SECOND": ((0, 1), (10, 9)),
        "TERASECOND": ((0, 1), (10, -3)),
        "YOTTASECOND": ((0, 1), (10, -15)),
        "YOCTOSECOND": ((0, 1), (10, 33)),
        "ZETTASECOND": ((0, 1), (10, -12)),
        "ZEPTOSECOND": ((0, 1), (10, 30)),

    },
    "HOUR": {
        "ATOOSECOND": ((0, 1), (10, 18, 60*60, 1)),
        "CENTISECOND": ((0, 1), (10, 2, 60*60, 1)),
        "DAY": ((0, 1), (24, -1)),
        "DECASECOND": ((0, 1), (10, -1, 60*60, 1)),
        "DECISECOND": ((0, 1), (10, 1, 60*60, 1)),
        "EXASECOND": ((0, 1), (10, -18, 60*60, 1)),
        "FEMTOSECOND": ((0, 1), (10, 15, 60*60, 1)),
        "GIGASECOND": ((0, 1), (10, -9, 60*60, 1)),
        "HOUR": (), # Same
        "HECTOSECOND": ((0, 1), (10, -2, 60*60, 1)),
        "KILOSECOND": ((0, 1), (10, -3, 60*60, 1)),
        "MEGASECOND": ((0, 1), (10, -6, 60*60, 1)),
        "MICROSECOND": ((0, 1), (10, 6, 60*60, 1)),
        "MINUTE": ((0, 1), (60, 1)),
        "MILLISECOND": ((0, 1), (10, 3, 60*60, 1)),
        "NANOSECOND": ((0, 1), (10, 9, 60*60, 1)),
        "PETASECOND": ((0, 1), (10, -15, 60*60, 1)),
        "PICOSECOND": ((0, 1), (10, 12, 60*60, 1)),
        "SECOND": ((0, 1), (60*60, 1)),
        "TERASECOND": ((0, 1), (10, -12, 60*60, 1)),
        "YOTTASECOND": ((0, 1), (10, -24, 60*60, 1)),
        "YOCTOSECOND": ((0, 1), (10, 24, 60*60, 1)),
        "ZETTASECOND": ((0, 1), (10, -21, 60*60, 1)),
        "ZEPTOSECOND": ((0, 1), (10, 21, 60*60, 1)),

    },
    "HECTOSECOND": {
        "ATOOSECOND": ((0, 1), (10, 20)),
        "CENTISECOND": ((0, 1), (10, 4)),
        "DAY": ((0, 1), (10, 2, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 1)),
        "DECISECOND": ((0, 1), (10, 3)),
        "EXASECOND": ((0, 1), (10, -16)),
        "FEMTOSECOND": ((0, 1), (10, 17)),
        "GIGASECOND": ((0, 1), (10, -7)),
        "HOUR": ((0, 1), (10, 2, 3600, -1)),
        "HECTOSECOND": (), # Same
        "KILOSECOND": ((0, 1), (10, -1)),
        "MEGASECOND": ((0, 1), (10, -4)),
        "MICROSECOND": ((0, 1), (10, 8)),
        "MINUTE": ((0, 1), (10, 2, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 5)),
        "NANOSECOND": ((0, 1), (10, 11)),
        "PETASECOND": ((0, 1), (10, -13)),
        "PICOSECOND": ((0, 1), (10, 14)),
        "SECOND": ((0, 1), (10, 2)),
        "TERASECOND": ((0, 1), (10, -10)),
        "YOTTASECOND": ((0, 1), (10, -22)),
        "YOCTOSECOND": ((0, 1), (10, 26)),
        "ZETTASECOND": ((0, 1), (10, -19)),
        "ZEPTOSECOND": ((0, 1), (10, 23)),

    },
    "KILOSECOND": {
        "ATOOSECOND": ((0, 1), (10, 21)),
        "CENTISECOND": ((0, 1), (10, 5)),
        "DAY": ((0, 1), (10, 3, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 2)),
        "DECISECOND": ((0, 1), (10, 4)),
        "EXASECOND": ((0, 1), (10, -15)),
        "FEMTOSECOND": ((0, 1), (10, 18)),
        "GIGASECOND": ((0, 1), (10, -6)),
        "HOUR": ((0, 1), (10, 3, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, 1)),
        "KILOSECOND": (), # Same
        "MEGASECOND": ((0, 1), (10, -3)),
        "MICROSECOND": ((0, 1), (10, 9)),
        "MINUTE": ((0, 1), (10, 3, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 6)),
        "NANOSECOND": ((0, 1), (10, 12)),
        "PETASECOND": ((0, 1), (10, -12)),
        "PICOSECOND": ((0, 1), (10, 15)),
        "SECOND": ((0, 1), (10, 3)),
        "TERASECOND": ((0, 1), (10, -9)),
        "YOTTASECOND": ((0, 1), (10, -21)),
        "YOCTOSECOND": ((0, 1), (10, 27)),
        "ZETTASECOND": ((0, 1), (10, -18)),
        "ZEPTOSECOND": ((0, 1), (10, 24)),

    },
    "MEGASECOND": {
        "ATOOSECOND": ((0, 1), (10, 24)),
        "CENTISECOND": ((0, 1), (10, 8)),
        "DAY": ((0, 1), (10, 6, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 5)),
        "DECISECOND": ((0, 1), (10, 7)),
        "EXASECOND": ((0, 1), (10, -12)),
        "FEMTOSECOND": ((0, 1), (10, 21)),
        "GIGASECOND": ((0, 1), (10, -3)),
        "HOUR": ((0, 1), (10, 6, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, 4)),
        "KILOSECOND": ((0, 1), (10, 3)),
        "MEGASECOND": (), # Same
        "MICROSECOND": ((0, 1), (10, 12)),
        "MINUTE": ((0, 1), (10, 6, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 9)),
        "NANOSECOND": ((0, 1), (10, 15)),
        "PETASECOND": ((0, 1), (10, -9)),
        "PICOSECOND": ((0, 1), (10, 18)),
        "SECOND": ((0, 1), (10, 6)),
        "TERASECOND": ((0, 1), (10, -6)),
        "YOTTASECOND": ((0, 1), (10, -18)),
        "YOCTOSECOND": ((0, 1), (10, 30)),
        "ZETTASECOND": ((0, 1), (10, -15)),
        "ZEPTOSECOND": ((0, 1), (10, 27)),

    },
    "MICROSECOND": {
        "ATOOSECOND": ((0, 1), (10, 12)),
        "CENTISECOND": ((0, 1), (10, -4)),
        "DAY": ((0, 1), (10, -6, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -7)),
        "DECISECOND": ((0, 1), (10, -5)),
        "EXASECOND": ((0, 1), (10, -24)),
        "FEMTOSECOND": ((0, 1), (10, 9)),
        "GIGASECOND": ((0, 1), (10, -15)),
        "HOUR": ((0, 1), (10, -6, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -8)),
        "KILOSECOND": ((0, 1), (10, -9)),
        "MEGASECOND": ((0, 1), (10, -12)),
        "MICROSECOND": (), # Same
        "MINUTE": ((0, 1), (10, -6, 60, -1)),
        "MILLISECOND": ((0, 1), (10, -3)),
        "NANOSECOND": ((0, 1), (10, 3)),
        "PETASECOND": ((0, 1), (10, -21)),
        "PICOSECOND": ((0, 1), (10, 6)),
        "SECOND": ((0, 1), (10, -6)),
        "TERASECOND": ((0, 1), (10, -18)),
        "YOTTASECOND": ((0, 1), (10, -30)),
        "YOCTOSECOND": ((0, 1), (10, 18)),
        "ZETTASECOND": ((0, 1), (10, -27)),
        "ZEPTOSECOND": ((0, 1), (10, 15)),

    },
    "MINUTE": {
        "ATOOSECOND": ((0, 1), (10, 18, 60, 1)),
        "CENTISECOND": ((0, 1), (10, 2, 60, 1)),
        "DAY": ((0, 1), (24, -1)),
        "DECASECOND": ((0, 1), (10, -1, 60, 1)),
        "DECISECOND": ((0, 1), (10, 1, 60, 1)),
        "EXASECOND": ((0, 1), (10, -18, 60, 1)),
        "FEMTOSECOND": ((0, 1), (10, 15, 60, 1)),
        "GIGASECOND": ((0, 1), (10, -9, 60, 1)),
        "HOUR": ((0, 1), (60, -1)),
        "HECTOSECOND": ((0, 1), (10, -2, 60, 1)),
        "KILOSECOND": ((0, 1), (10, -3, 60, 1)),
        "MEGASECOND": ((0, 1), (10, -6, 60, 1)),
        "MICROSECOND": ((0, 1), (10, 6, 60, 1)),
        "MINUTE": (), # Same
        "MILLISECOND": ((0, 1), (10, 3, 60, 1)),
        "NANOSECOND": ((0, 1), (10, 9, 60, 1)),
        "PETASECOND": ((0, 1), (10, -15, 60, 1)),
        "PICOSECOND": ((0, 1), (10, 12, 60, 1)),
        "SECOND": (0, 1), (60, 1)),
        "TERASECOND": ((0, 1), (10, -12, 60, 1)),
        "YOTTASECOND": ((0, 1), (10, -24, 60, 1)),
        "YOCTOSECOND": ((0, 1), (10, 24, 60, 1)),
        "ZETTASECOND": ((0, 1), (10, -21, 60, 1)),
        "ZEPTOSECOND": ((0, 1), (10, 21, 60, 1)),

    },
    "MILLISECOND": {
        "ATOOSECOND": ((0, 1), (10, 15)),
        "CENTISECOND": ((0, 1), (10, -1)),
        "DAY": ((0, 1), (10, -3, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -4)),
        "DECISECOND": ((0, 1), (10, -2)),
        "EXASECOND": ((0, 1), (10, -21)),
        "FEMTOSECOND": ((0, 1), (10, 12)),
        "GIGASECOND": ((0, 1), (10, -12)),
        "HOUR": ((0, 1), (10, -3, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -5)),
        "KILOSECOND": ((0, 1), (10, -6)),
        "MEGASECOND": ((0, 1), (10, -9)),
        "MICROSECOND": ((0, 1), (10, 3)),
        "MINUTE": ((0, 1), (10, -3, 60, -1)),
        "MILLISECOND": (), # Same
        "NANOSECOND": ((0, 1), (10, 6)),
        "PETASECOND": ((0, 1), (10, -18)),
        "PICOSECOND": ((0, 1), (10, 9)),
        "SECOND": ((0, 1), (10, -3)),
        "TERASECOND": ((0, 1), (10, -15)),
        "YOTTASECOND": ((0, 1), (10, -27)),
        "YOCTOSECOND": ((0, 1), (10, 21)),
        "ZETTASECOND": ((0, 1), (10, -24)),
        "ZEPTOSECOND": ((0, 1), (10, 18)),

    },
    "NANOSECOND": {
        "ATOOSECOND": ((0, 1), (10, 9)),
        "CENTISECOND": ((0, 1), (10, -7)),
        "DAY": ((0, 1), (10, -9, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -10)),
        "DECISECOND": ((0, 1), (10, -8)),
        "EXASECOND": ((0, 1), (10, -27)),
        "FEMTOSECOND": ((0, 1), (10, 6)),
        "GIGASECOND": ((0, 1), (10, -18)),
        "HOUR": ((0, 1), (10, -9, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -11)),
        "KILOSECOND": ((0, 1), (10, -12)),
        "MEGASECOND": ((0, 1), (10, -15)),
        "MICROSECOND": ((0, 1), (10, -3)),
        "MINUTE": ((0, 1), (10, -9, 60, -1)),
        "MILLISECOND": ((0, 1), (10, -6)),
        "NANOSECOND": (), # Same
        "PETASECOND": ((0, 1), (10, -24)),
        "PICOSECOND": ((0, 1), (10, 3)),
        "SECOND": ((0, 1), (10, -9)),
        "TERASECOND": ((0, 1), (10, -21)),
        "YOTTASECOND": ((0, 1), (10, -33)),
        "YOCTOSECOND": ((0, 1), (10, 15)),
        "ZETTASECOND": ((0, 1), (10, -30)),
        "ZEPTOSECOND": ((0, 1), (10, 12)),

    },
    "PETASECOND": {
        "ATOOSECOND": ((0, 1), (10, 33)),
        "CENTISECOND": ((0, 1), (10, 17)),
        "DAY": ((0, 1), (10, 15, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 14)),
        "DECISECOND": ((0, 1), (10, 16)),
        "EXASECOND": ((0, 1), (10, -3)),
        "FEMTOSECOND": ((0, 1), (10, 30)),
        "GIGASECOND": ((0, 1), (10, 6)),
        "HOUR": ((0, 1), (10, 15, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, 13)),
        "KILOSECOND": ((0, 1), (10, 12)),
        "MEGASECOND": ((0, 1), (10, 9)),
        "MICROSECOND": ((0, 1), (10, 21)),
        "MINUTE": ((0, 1), (10, 15, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 18)),
        "NANOSECOND": ((0, 1), (10, 24)),
        "PETASECOND": (), # Same
        "PICOSECOND": ((0, 1), (10, 27)),
        "SECOND": ((0, 1), (10, 15)),
        "TERASECOND": ((0, 1), (10, 3)),
        "YOTTASECOND": ((0, 1), (10, -9)),
        "YOCTOSECOND": ((0, 1), (10, 39)),
        "ZETTASECOND": ((0, 1), (10, -6)),
        "ZEPTOSECOND": ((0, 1), (10, 36)),

    },
    "PICOSECOND": {
        "ATOOSECOND": ((0, 1), (10, 6)),
        "CENTISECOND": ((0, 1), (10, -10)),
        "DAY": ((0, 1), (10, -12, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -13)),
        "DECISECOND": ((0, 1), (10, -11)),
        "EXASECOND": ((0, 1), (10, -30)),
        "FEMTOSECOND": ((0, 1), (10, 3)),
        "GIGASECOND": ((0, 1), (10, -21)),
        "HOUR": ((0, 1), (10, -12, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -14)),
        "KILOSECOND": ((0, 1), (10, -15)),
        "MEGASECOND": ((0, 1), (10, -18)),
        "MICROSECOND": ((0, 1), (10, -6)),
        "MINUTE": ((0, 1), (10, -12, 60, -1)),
        "MILLISECOND": ((0, 1), (10, -9)),
        "NANOSECOND": ((0, 1), (10, -3)),
        "PETASECOND": ((0, 1), (10, -27)),
        "PICOSECOND": (), # Same
        "SECOND": ((0, 1), (10, -12)),
        "TERASECOND": ((0, 1), (10, -24)),
        "YOTTASECOND": ((0, 1), (10, -36)),
        "YOCTOSECOND": ((0, 1), (10, 12)),
        "ZETTASECOND": ((0, 1), (10, -33)),
        "ZEPTOSECOND": ((0, 1), (10, 9)),

    },
    "SECOND": {
        "ATOOSECOND": ((0, 1), (10, 18)),
        "CENTISECOND": ((0, 1), (10, 2)),
        "DAY": ((0, 1), (86400, -1)),
        "DECASECOND": ((0, 1), (10, -1)),
        "DECISECOND": ((0, 1), (10, 1)),
        "EXASECOND": ((0, 1), (10, -18)),
        "FEMTOSECOND": ((0, 1), (10, 15)),
        "GIGASECOND": ((0, 1), (10, -9)),
        "HOUR": ((0, 1), (3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -2)),
        "KILOSECOND": ((0, 1), (10, -3)),
        "MEGASECOND": ((0, 1), (10, -6)),
        "MICROSECOND": ((0, 1), (10, 6)),
        "MINUTE": ((0, 1), (60, -1)),
        "MILLISECOND": ((0, 1), (10, 3)),
        "NANOSECOND": ((0, 1), (10, 9)),
        "PETASECOND": ((0, 1), (10, -15)),
        "PICOSECOND": ((0, 1), (10, 12)),
        "SECOND": (), # Same
        "TERASECOND": ((0, 1), (10, -12)),
        "YOTTASECOND": ((0, 1), (10, -24)),
        "YOCTOSECOND": ((0, 1), (10, 24)),
        "ZETTASECOND": ((0, 1), (10, -21)),
        "ZEPTOSECOND": ((0, 1), (10, 21)),

    },
    "TERASECOND": {
        "ATOOSECOND": ((0, 1), (10, 30)),
        "CENTISECOND": ((0, 1), (10, 14)),
        "DAY": ((0, 1), (10, 12, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 11)),
        "DECISECOND": ((0, 1), (10, 13)),
        "EXASECOND": ((0, 1), (10, -6)),
        "FEMTOSECOND": ((0, 1), (10, 27)),
        "GIGASECOND": ((0, 1), (10, 3)),
        "HOUR": ((0, 1), (10, 12, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, 10)),
        "KILOSECOND": ((0, 1), (10, 9)),
        "MEGASECOND": ((0, 1), (10, 6)),
        "MICROSECOND": ((0, 1), (10, 18)),
        "MINUTE": ((0, 1), (10, 12, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 15)),
        "NANOSECOND": ((0, 1), (10, 21)),
        "PETASECOND": ((0, 1), (10, -3)),
        "PICOSECOND": ((0, 1), (10, 24)),
        "SECOND": ((0, 1), (10, 12)),
        "TERASECOND": (), # Same
        "YOTTASECOND": ((0, 1), (10, -12)),
        "YOCTOSECOND": ((0, 1), (10, 36)),
        "ZETTASECOND": ((0, 1), (10, -9)),
        "ZEPTOSECOND": ((0, 1), (10, 33)),

    },
    "YOTTASECOND": {
        "ATOOSECOND": ((0, 1), (10, 42)),
        "CENTISECOND": ((0, 1), (10, 26)),
        "DAY": ((0, 1), (10, 24, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 23)),
        "DECISECOND": ((0, 1), (10, 25)),
        "EXASECOND": ((0, 1), (10, 6)),
        "FEMTOSECOND": ((0, 1), (10, 39)),
        "GIGASECOND": ((0, 1), (10, 15)),
        "HOUR": ((0, 1), (10, 24, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, 22)),
        "KILOSECOND": ((0, 1), (10, 21)),
        "MEGASECOND": ((0, 1), (10, 18)),
        "MICROSECOND": ((0, 1), (10, 30)),
        "MINUTE": ((0, 1), (10, 24, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 27)),
        "NANOSECOND": ((0, 1), (10, 33)),
        "PETASECOND": ((0, 1), (10, 9)),
        "PICOSECOND": ((0, 1), (10, 36)),
        "SECOND": ((0, 1), (10, 24)),
        "TERASECOND": ((0, 1), (10, 12)),
        "YOTTASECOND": (), # Same
        "YOCTOSECOND": ((0, 1), (10, 48)),
        "ZETTASECOND": ((0, 1), (10, 3)),
        "ZEPTOSECOND": ((0, 1), (10, 45)),

    },
    "YOCTOSECOND": {
        "ATOOSECOND": ((0, 1), (10, -6)),
        "CENTISECOND": ((0, 1), (10, -22)),
        "DAY": ((0, 1), (10, -24, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -25)),
        "DECISECOND": ((0, 1), (10, -23)),
        "EXASECOND": ((0, 1), (10, -42)),
        "FEMTOSECOND": ((0, 1), (10, -9)),
        "GIGASECOND": ((0, 1), (10, -33)),
        "HOUR": ((0, 1), (10, -24, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -26)),
        "KILOSECOND": ((0, 1), (10, -27)),
        "MEGASECOND": ((0, 1), (10, -30)),
        "MICROSECOND": ((0, 1), (10, -18)),
        "MINUTE": ((0, 1), (10, -24, 60, -1)),
        "MILLISECOND": ((0, 1), (10, -21)),
        "NANOSECOND": ((0, 1), (10, -15)),
        "PETASECOND": ((0, 1), (10, -39)),
        "PICOSECOND": ((0, 1), (10, -12)),
        "SECOND": ((0, 1), (10, -24)),
        "TERASECOND": ((0, 1), (10, -36)),
        "YOTTASECOND": ((0, 1), (10, -48)),
        "YOCTOSECOND": (), # Same
        "ZETTASECOND": ((0, 1), (10, -45)),
        "ZEPTOSECOND": ((0, 1), (10, -3)),

    },
    "ZETTASECOND": {
        "ATOOSECOND": ((0, 1), (10, 39)),
        "CENTISECOND": ((0, 1), (10, 23)),
        "DAY": ((0, 1), (10, 21, 86400, -1)),
        "DECASECOND": ((0, 1), (10, 20)),
        "DECISECOND": ((0, 1), (10, 22)),
        "EXASECOND": ((0, 1), (10, 3)),
        "FEMTOSECOND": ((0, 1), (10, 36)),
        "GIGASECOND": ((0, 1), (10, 12)),
        "HOUR": ((0, 1), (10, 21, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, 19)),
        "KILOSECOND": ((0, 1), (10, 18)),
        "MEGASECOND": ((0, 1), (10, 15)),
        "MICROSECOND": ((0, 1), (10, 27)),
        "MINUTE": ((0, 1), (10, 21, 60, -1)),
        "MILLISECOND": ((0, 1), (10, 24)),
        "NANOSECOND": ((0, 1), (10, 30)),
        "PETASECOND": ((0, 1), (10, 6)),
        "PICOSECOND": ((0, 1), (10, 33)),
        "SECOND": ((0, 1), (10, 21)),
        "TERASECOND": ((0, 1), (10, 9)),
        "YOTTASECOND": ((0, 1), (10, -3)),
        "YOCTOSECOND": ((0, 1), (10, 45)),
        "ZETTASECOND": (), # Same
        "ZEPTOSECOND": ((0, 1), (10, 42)),

    },
    "ZEPTOSECOND": {
        "ATOOSECOND": ((0, 1), (10, -3)),
        "CENTISECOND": ((0, 1), (10, -19)),
        "DAY": ((0, 1), (10, -21, 86400, -1)),
        "DECASECOND": ((0, 1), (10, -22)),
        "DECISECOND": ((0, 1), (10, -20)),
        "EXASECOND": ((0, 1), (10, -39)),
        "FEMTOSECOND": ((0, 1), (10, -6)),
        "GIGASECOND": ((0, 1), (10, -30)),
        "HOUR": ((0, 1), (10, -21, 3600, -1)),
        "HECTOSECOND": ((0, 1), (10, -23)),
        "KILOSECOND": ((0, 1), (10, -24)),
        "MEGASECOND": ((0, 1), (10, -27)),
        "MICROSECOND": ((0, 1), (10, -15)),
        "MINUTE": ((0, 1), (10, -21, 60, -1)),
        "MILLISECOND": ((0, 1), (10, -18)),
        "NANOSECOND": ((0, 1), (10, -12)),
        "PETASECOND": ((0, 1), (10, -36)),
        "PICOSECOND": ((0, 1), (10, -9)),
        "SECOND": ((0, 1), (10, -21)),
        "TERASECOND": ((0, 1), (10, -33)),
        "YOTTASECOND": ((0, 1), (10, -45)),
        "YOCTOSECOND": ((0, 1), (10, 3)),
        "ZETTASECOND": ((0, 1), (10, -42)),
        "ZEPTOSECOND": (), # Same

    },

  },

}


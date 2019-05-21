from colorutils import Color
from math import ceil


def to_sint(hexval):
    # hexval in form of #FFFFFF
    value = int(hexval, 16) if hexval[0] != '#' else int(hexval[1:], 16)
    if (value & 0x80000000) == 0x80000000:
        return -((value ^ 0xffffffff) + 1)
    else:
        return value


def to_hex(value):
    return hex(value & (2**32-1)).replace('0x', '#').upper()


def lighten(base, percent):
    def lightenColor(val): return ceil(min([val + val * percent, 255.0]))
    return Color(
        (
            lightenColor(base.red),
            lightenColor(base.green),
            lightenColor(base.blue)
        )
    )

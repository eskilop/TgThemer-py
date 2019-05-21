from colorutils import Color
from math import ceil


def to_sint(hexval):
    # hexval in form of #FFFFFF
    value = int(hexval[1:], 16)
    return -((value ^ 0xffffffff) + 1)


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

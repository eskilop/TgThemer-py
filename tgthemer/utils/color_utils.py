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

    def darkenColor(val): return ceil(max([val + val * percent, 0.0]))

    return Color(
        (
            lightenColor(base.red),
            lightenColor(base.green),
            lightenColor(base.blue)
        )) if percent >= 0 else Color(
            (
                darkenColor(base.red),
                darkenColor(base.green),
                darkenColor(base.blue)
            )
    )


def edit_alpha(color, percent):
    initial_alpha = color[0:2] if color[0] != '#' else color[1:3]
    return (hex(int(round(
        int(initial_alpha, 16) +
        (int(initial_alpha, 16) * percent)
    ))) if percent > 0
        else hex(int(round(
            int(initial_alpha, 16) +
            (int(initial_alpha, 16) * percent)
        )))).replace('0x', '#').upper() + color[3:]

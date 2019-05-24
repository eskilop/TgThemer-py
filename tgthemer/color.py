#!/usr/bin/env python3
from math import ceil


class Color:

    def __init__(self, hex=None, sint=None):
        if hex is not None and sint is None:
            self.color = hex
        elif sint is not None and hex is None:
            self.color = sint
        else:
            pass  # debug purposes
            # raise ValueError("You must specify a color.")

    @property
    def sint(self):
        if type(self.color) is not str:
            return self.color

        value = int(self.color, 16) if self.color[0] != '#' else int(
            self.color[1:], 16)
        if (value & 0x80000000) == 0x80000000:
            return -((value ^ 0xffffffff) + 1)
        else:
            return value

    @property
    def hex(self):
        if type(self.color) is not int:
            return self.color
        else:
            return hex(self.color & (2**32-1)).replace('0x', '#').upper()

    def _argb_to_hex(self, colort):
        return '#%02x%02x%02x%02x'.upper() % (
            colort[0],
            colort[1],
            colort[2],
            colort[3]
        )

    @property
    def argb(self):
        return (
            int(self.hex[1:3], 16),
            int(self.hex[3:5], 16),
            int(self.hex[5:7], 16),
            int(self.hex[7:9], 16)
        )

    def lighten(self, percent):
        def lightenColor(val): return ceil(min([val + val * percent, 255.0]))

        def darkenColor(val): return ceil(max([val + val * percent, 0.0]))

        color = self.argb

        return Color(
            self._argb_to_hex(
                (
                    color[0],
                    lightenColor(color[1]),
                    lightenColor(color[2]),
                    lightenColor(color[3])
                )
            )
        ) if percent >= 0 else Color(self._argb_to_hex(
            (
                color[0],
                darkenColor(color[1]),
                darkenColor(color[2]),
                darkenColor(color[3])
            )
        ))

    def alpha(self, percent):
        initial_alpha = self.hex[1:3]
        return Color(
            hex=(
                hex(
                    int(round(
                        int(initial_alpha, 16) +
                        (int(initial_alpha, 16) * percent)
                    ))
                ) if percent > 0
                else hex(
                    int(round(
                        int(initial_alpha, 16) +
                        (int(initial_alpha, 16) * percent)
                    ))
                )
            ).replace('0x', '#').upper() + self.hex[3:])

    def __repr__(self):
        return "{}".format(self.hex)

    def __eq__(self, other):
        return self.hex == other.hex \
            and self.sint == other.sint

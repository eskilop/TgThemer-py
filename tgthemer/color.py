#!/usr/bin/env python3
from math import ceil


class Color:

    def __init__(self, color=None):
        self.is24b = False

        if color is None:
            raise ValueError("No color specified")
        elif type(color) == str:
            if len(color[1:]) == 6:
                self.is24b = True
        elif type(color) == int:
            if (color & -16777216) == 0:
                self.is24b = True
        
        self.color = color

    @property
    def sint(self):
        if type(self.color) is not str:
            return self.color

        value = int(self.color, 16) if self.color[0] != '#' else int(
            self.color[1:], 16)
        
        transformers = (0x80000000, 0xffffffff) if not self.is24b else (0x800000, 0xffffff)

        if (value & transformers[0]) == transformers[0]:
            return -((value ^ transformers[1]) + 1)
        else:
            return value

    @property
    def hex(self):
        if type(self.color) is not int:
            return self.color
        else:
            return hex(self.color & (2**32-1)).replace('0x', '#').upper() \
            if not self.is24b else \
            hex(self.color & (2**24-1)).replace('0x', '#').upper()

    def argb_to_hex(self, colort):
        formatter = '#%02x%02x%02x%02x' if not self.is24b else '#%02x%02x%02x'
        return formatter.upper() % colort

    @property
    def argb(self):
        return (
            int(self.hex[1:3], 16),
            int(self.hex[3:5], 16),
            int(self.hex[5:7], 16),
            int(self.hex[7:9], 16)
        ) if not self.is24b else \
        (
            int(self.hex[1:3], 16),
            int(self.hex[3:5], 16),
            int(self.hex[5:7], 16),
        )

    def lighten(self, percent):

        def lightenColor(val): return ceil(min([val + val * percent, 255.0]))
        def darkenColor(val): return ceil(max([val + val * percent, 0.0]))
        def lightenARGB(colort): 
            t = [lightenColor(i) for i in colort]
            if not self.is24b:
                t[0] = colort[0]
            return tuple(t)

        def darkenARGB(colort): 
            t = [darkenColor(i) for i in colort]
            if not self.is24b:
                t[0] = colort[0]
            return tuple(t)

        transform = lightenARGB if percent >= 0 else darkenARGB

        return Color(self.argb_to_hex(transform(self.argb)))

    def alpha(self, percent):
        if self.is24b:
            raise TypeError("You can't edit alpha channel on 24bit color.")

        initial_alpha = self.hex[1:3]
        new_alpha = hex(int(round(
                        int(initial_alpha, 16) +
                        (int(initial_alpha, 16) * percent)
                    )))
        return Color((new_alpha).replace('0x', '#').upper() + self.hex[3:])

    def __repr__(self):
        return "{}".format(self.hex)

    def __eq__(self, other):
        return self.hex == other.hex \
            and self.sint == other.sint

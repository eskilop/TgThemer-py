from tgthemer import Color

colorgroup = {
    "base": '#FF18181F',
    "s_int": -15198177,
    "argb": (255, 24, 24, 31)
}


class TestColor(object):

    def test_hex_prop(self):
        c = Color(hex=colorgroup["base"])
        assert c.hex == colorgroup["base"]

    def test_sint_prop(self):
        c = Color(hex=colorgroup["base"])
        assert c.sint == colorgroup["s_int"]

    def test_argb_prop(self):
        c = Color(hex=colorgroup["base"])
        assert c.argb == colorgroup["argb"]

    def test_alpha(self):
        c = Color(hex=colorgroup["base"])
        assert c.alpha(-0.5).hex == "#8018181F"

    def test_lighten(self):
        base = "#FF18181F"
        res = Color(hex="#FF30303E")
        c = Color(hex=base)
        assert c.lighten(1) == res

    def test_darken(self):
        base = "#FF30303E"
        res = Color(hex="#FF18181F")
        c = Color(hex=base)
        assert c.lighten(-0.5) == res

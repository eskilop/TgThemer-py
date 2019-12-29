from tgthemer import Color

colorgroup = {
    "base": '#FF18181F',
    "result": '#FF30303E',
    "alpha": '#8018181F',
    "s_int": -15198177,
    "argb": (255, 24, 24, 31)
}

colorgroup24 = {
    "base": '#18181F',
    "result": '#30303E',
    "s_int": 1579039,
    "argb": (24, 24, 31)
}


class TestColor(object):

    def test_hex_prop(self):
        assert Color(hex=colorgroup["base"]).hex == colorgroup["base"]

    def test_sint_prop(self):
        assert Color(hex=colorgroup["base"]).sint == colorgroup["s_int"]

    def test_argb_prop(self):
        assert Color(hex=colorgroup["base"]).argb == colorgroup["argb"]

    def test_alpha(self):
        assert Color(hex=colorgroup["base"]).alpha(-0.5).hex == "#8018181F"

    def test_lighten(self):
        assert Color(hex=colorgroup["base"]).lighten(1) == Color(hex="#FF30303E")

    def test_darken(self):
        assert Color(hex=colorgroup["result"]).lighten(-0.5) == Color(hex=colorgroup["base"])

    # tests for 24bit

    def test_hex_prop24(self):
        assert Color(hex=colorgroup24["base"]).hex == colorgroup24["base"]

    def test_sint_prop24(self):
        assert Color(hex=colorgroup24["base"]).sint == colorgroup24["s_int"]

    def test_argb_prop24(self):
        assert Color(hex=colorgroup24["base"]).argb == colorgroup24["argb"]

    def test_lighten24(self):
        assert Color(colorgroup24["base"]).lighten(1) == Color(hex=colorgroup24["result"])

    def test_darken24(self):
        assert Color(hex=colorgroup24["result"]).lighten(-0.5) == Color(hex=colorgroup24["base"])

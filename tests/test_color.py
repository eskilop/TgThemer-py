from tgthemer.color import Color


class TestColor(object):
    def test_hex_prop(self):
        base = '#FF18181F'
        s_int = -15198177
        c = Color(hex=base)
        assert c.hex == base and c.sint == s_int

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

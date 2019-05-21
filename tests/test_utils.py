import tgthemer.utils as utils
from colorutils import Color


class TestUtils(object):
    def test_to_hex(self):
        hxstr = "#7790C4FF"
        assert utils.to_hex(utils.to_sint(hxstr)) == hxstr

    def test_to_int(self):
        decval = -13347218
        assert utils.to_sint(utils.to_hex(decval)) == decval

    def test_lighten(self):
        assert utils.lighten(utils.lighten(
            Color(hex='#555555'), 0.1), -0.1).hex == '#555555'

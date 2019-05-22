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

    def test_hstr_to_tgstr(self):
        hstr = "my_str=#FF18181F"
        assert utils.hstr_to_tgstr(hstr) == "my_str=" + \
            str(utils.to_sint('FF18181F')) + "\n"

    def test_tgstr_to_hstr(self):
        tgstr = "my_str=-15198177"
        assert utils.tgstr_to_hstr(tgstr) == "my_str=" + \
            str(utils.to_hex(-15198177)) + "\n"

    def test_hdict_to_tgdict(self):
        hdict = {'myval': '#FF18181F'}
        assert utils.hdict_to_tgdict(
            hdict) == {"myval": str(utils.to_sint('FF18181F'))}

    def test_tgdict_to_hdict(self):
        tgdict = {'myval': -15198177}
        assert utils.tgdict_to_hdict(
            tgdict) == {"myval": '#FF18181F'}

    def test_edit_alpha(self):
        assert utils.edit_alpha('#FF', -0.1) == "#E6"

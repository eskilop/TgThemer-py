from tgthemer import Themer
import os


class TestThemer(object):
    def test_outfile(self):
        t = Themer()
        t.generate_android(custom={}, out="file")
        assert os.path.exists("out/file.attheme")

    def test_clear(self):
        t = Themer()
        t.clear()
        assert not os.path.exists("out")

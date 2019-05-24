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

    def test_human_dict(self):
        t = Themer()
        open('emptyfile.attheme', 'w').close()
        t._read_file("emptyfile")
        assert t.human_dict == {}
        os.remove('emptyfile.attheme')

    def test_telegram_dict(self):
        t = Themer()
        open('emptyfile.attheme', 'w').close()
        t._read_file("emptyfile")
        assert t.telegram_dict == {}
        os.remove('emptyfile.attheme')

    def test_human_string(self):
        t = Themer()
        open('emptyfile.attheme', 'w').close()
        t._read_file("emptyfile")
        assert t.human_string == ""
        os.remove('emptyfile.attheme')

    def test_telegram_string(self):
        t = Themer()
        open('emptyfile.attheme', 'w').close()
        t._read_file("emptyfile")
        assert t.telegram_string == ""
        os.remove('emptyfile.attheme')

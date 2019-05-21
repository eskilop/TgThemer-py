from colorutils import Color
import tgthemer.utils as utils


class Themer:
    def __init__(self, *args, **kwargs):
        self.colordict = {}
        if args == () and kwargs != {}:
            self.primary = kwargs['primary']
            self.secondary = kwargs['secondary']
            self.accent = kwargs['accent']
            self.mode = kwargs['mode']
        elif args != () and kwargs == {}:
            self.primary = args[0]
            self.secondary = args[1]
            self.accent = args[2]
            self.mode = args[3]
        else:
            pass
            # raise ValueError("You must specify either args or kwargs")

    def read_file(self, inputfile):
        source = open(inputfile+'.attheme', 'r')
        contents = source.read()
        source.close()
        return contents

    def to_file(self, contents, outfile):
        result = open(outfile+'.attheme', 'w')

        result.close()

    def to_string(self, contents_dict):
        result = ""
        for k, v in contents_dict.items():
            result += "{}={}\n".format(k, v)
        return result

    def to_dict(self, contents):
        result_dict = {}
        pairs = contents.split('\n')
        for pair in pairs:
            if pair != '':
                kvpair = pair.split('=')
                result_dict[kvpair[0]] = kvpair[1]

    def _transform_dict(self, contents_dict, fn):
        result = {}
        for k, v in contents_dict.items():
            result[k] = fn(v)
        return result

    def to_human_readable(self, contents_dict):
        return self._transform_dict(
            contents_dict,
            lambda x: utils.to_hex(int(x))
        )

    def to_telegram_readable(self, contents_dict):
        return self._transform_dict(
            contents_dict,
            lambda x: utils.to_sint(x)
        )

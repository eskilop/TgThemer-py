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

    def read_file(self, name):
        source = open(name+'.attheme', 'r')
        contents = source.read()
        source.close()
        pairs = contents.split('\n')
        for pair in pairs:
            if pair != '':
                kvpair = pair.split('=')
                self.colordict[kvpair[0]] = utils.to_hex(int(kvpair[1]))

    def to_string(self, name):
        result = open(name+'.attheme', 'w')
        for k, v in self.colordict.items():
            result.write("{}={}\n".format(k, v))
        result.close()

    def to_final(self, sname, dname):
        source = open(sname+'.attheme', 'r')
        contents = source.read()
        source.close()
        pairs = contents.split('\n')
        for pair in pairs:
            if pair != '':
                kvpair = pair.split('=')
                self.colordict[kvpair[0]] = utils.to_sint(kvpair[1])
        self.to_string(dname)

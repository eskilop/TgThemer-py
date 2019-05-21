from colorutils import Color
import tgthemer.utils as utils

std_none = "#00000000"


class Themer:

    def __init__(self, primary=std_none, secondary=std_none, accent=std_none,
                 mode="darken"):
        self.mode = mode
        self.primary = primary
        if secondary == std_none:
            self.secondary = utils.lighten(Color(hex=self.primary), 0.5).hex \
                if self.mode == 'lighten' \
                else utils.lighten(Color(hex=self.primary), -0.5).hex
        else:
            self.secondary = secondary
        self.accent = accent

    def generate(self):

        contents = utils.read_file("source_dark")
        human = utils.tgstr_to_hstr(contents)
        out_contents = human \
            .replace('#FF6FB3E6', self.accent) \
            .replace('#FF212426', self.primary) \
            .replace('#FF1F2122', self.primary) \
            .replace('#FF26292B', self.secondary)

        tgstr = utils.hstr_to_tgstr(out_contents)

        utils.to_file(
            tgstr, 'out_theme'
        )

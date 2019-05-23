from .color import Color
import shutil
import os

std_none = "#000000"


class Themer:

    def __init__(self, primary=std_none, secondary=std_none, accent=std_none,
                 mode="darken", ttype="dark"):
        self.mode = mode
        self.primary = Color(hex=primary)
        if secondary == std_none:
            self.secondary = self.primary.lighten(0.5) \
                if self.mode == 'lighten' \
                else self.primary.lighten(-0.5)
        else:
            self.secondary = Color(hex=secondary)
        self.accent = Color(hex=accent)
        self.ttype = ttype

        self.contents = ""
        self.theme_dict = {}

    def read_file(self, inputfile):
        source = open(inputfile+'.attheme', 'r')
        contents = source.read()
        source.close()
        self.contents = contents
        self.theme_dict = self._to_dict()

    def to_file(self, contents, outfile):
        result = open(outfile+'.attheme', 'w')
        result.write(contents)
        result.close()

    def generate_android(self, custom=None):
        shutil.rmtree('out', ignore_errors=True)

        source = "sources/android/source_dark" \
            if self.ttype == 'dark' \
            else "sources/android/source_light"

        contents = self.read_file(source)
        self.theme_dict = self.human_dict

        if custom is not None:
            for k, v in custom.items():
                setattr(self.theme_dict, k, v)
        else:
            white = Color(hex="#FFFFFFFF")
            white_2 = white.edit_alpha(-0.8)
            white_5 = white.edit_alpha(-0.5)
            white_8 = white.edit_alpha(-0.2)

            bgsect_color = self.primary.lighten(-0.2).hex
            dialogs_bg = self.primary.lighten(0.5).hex

            # accents
            self.theme_dict[
                'windowBackgroundWhiteInputFieldActivated'
            ] = self.accent.hex

            # backgrounds
            self.theme_dict['windowBackgroundWhite'] = self.primary.hex
            self.theme_dict['dialogBackground'] = dialogs_bg
            self.theme_dict['windowBackgroundGray'] = bgsect_color
            self.theme_dict['graySection'] = bgsect_color
            self.theme_dict['chats_menuBackground'] = bgsect_color
            self.theme_dict['dialogBackgroundGray'] = bgsect_color
            self.theme_dict['chat_wallpaper'] = self.primary.lighten(-0.5).hex
            self.theme_dict['dialogIcon'] = white_8
            self.theme_dict['dialogBadgeBackground'] = self.accent.hex
            self.theme_dict['dialogLineProgressBackground'] = white_5
            self.theme_dict['dialogLineProgress'] = self.accent.hex

            # actionbar default
            self.theme_dict['actionBarDefault'] = self.secondary.hex
            self.theme_dict['actionBarDefaultIcon'] = white.hex
            # menu
            self.theme_dict['actionBarDefaultSubmenuBackground'] = dialogs_bg

            # buttons
            self.theme_dict['dialogButton'] = self.accent.hex

            # checkboxs
            self.theme_dict['dialogCheckboxSquareBackground'] = white_2
            self.theme_dict['dialogCheckboxSquareCheck'] = white.hex
            self.theme_dict['dialogCheckboxSquareDisabled'] = white_2
            self.theme_dict['dialogCheckboxSquareUnchecked'] = white_2
            self.theme_dict['dialogRoundCheckBox'] = self.accent.hex

            # texts
            self.theme_dict['windowBackgroundWhiteHintText'] = white_2
            self.theme_dict['chats_menuItemText'] = white_2
            self.theme_dict['actionBarDefaultSubmenuItem'] = white_2
            self.theme_dict['dialogTextGray2'] = white_2
            self.theme_dict['actionBarDefaultTitle'] = white_5
            self.theme_dict['dialogTextBlack'] = white_5
            self.theme_dict['dialogBadgeText'] = white_5
            # optional link color?
            self.theme_dict['dialogLinkSelection'] = self.accent.hex

        os.mkdir('out', 0o755)

        self.to_file(self.telegram_string, 'out/android')

    def _to_string(self, content_dict):
        result = ""
        for k, v in content_dict.items():
            result += "{}={}\n".format(k, v)
        return result

    def _to_dict(self):
        result_dict = {}
        pairs = self.contents.split('\n')
        for pair in pairs:
            if pair != '':
                kvpair = pair.split('=')
                result_dict[kvpair[0]] = kvpair[1]
        return result_dict

    def _transform_dict(self, fn):
        result = {}
        for k, v in self.theme_dict.items():
            result[k] = fn(v)
        return result

    @property
    def human_dict(self):
        return self._transform_dict(
            lambda x: Color(sint=int(x)).hex
        )

    @property
    def telegram_dict(self):
        return self._transform_dict(
            lambda x: Color(hex=x).sint
        )

    @property
    def telegram_string(self):
        return self._to_string(self.telegram_dict)

    @property
    def human_string(self):
        return self._to_string(self.human_dict)

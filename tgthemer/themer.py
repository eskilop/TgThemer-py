from colorutils import Color
import tgthemer.utils as utils

std_none = "#000000"


class Themer:

    def __init__(self, primary=std_none, secondary=std_none, accent=std_none,
                 mode="darken", ttype="dark"):
        self.mode = mode
        self.primary = Color(hex=primary)
        if secondary == std_none:
            self.secondary = utils.lighten(self.primary, 0.5) \
                if self.mode == 'lighten' \
                else utils.lighten(self.primary, -0.5)
        else:
            self.secondary = Color(hex=secondary)
        self.accent = Color(hex=accent)
        self.type = ttype

    def generate_android(self):

        def darken(color, percent): return utils.lighten(color, -(percent))

        white = "#FFFFFFFF"
        white_2 = utils.edit_alpha(white, -0.8)
        white_5 = utils.edit_alpha(white, -0.5)
        white_8 = utils.edit_alpha(white, -0.2)

        source = "sources/android/source_dark" \
            if self.type == 'dark' \
            else "sources/android/source_light"

        contents = utils.read_file(source)
        human_dict = utils.to_dict(utils.tgstr_to_hstr(contents))

        bgsect_color = darken(self.primary, 0.2).hex.replace(
            '#', '#FF').upper()
        dialogs_bg = utils.lighten(
            self.primary, 0.5).hex.replace('#', '#FF').upper()

        # accents
        human_dict['windowBackgroundWhiteInputFieldActivated'] = self.accent.hex.replace(
            '#', '#FF').upper()

        # backgrounds
        human_dict['windowBackgroundWhite'] = self.primary.hex.replace(
            '#', '#FF').upper()
        human_dict['dialogBackground'] = dialogs_bg
        human_dict['windowBackgroundGray'] = bgsect_color
        human_dict['graySection'] = bgsect_color
        human_dict['chats_menuBackground'] = bgsect_color
        human_dict['dialogBackgroundGray'] = bgsect_color
        human_dict['chat_wallpaper'] = darken(
            self.primary, 0.5).hex.replace('#', '#FF').upper()
        human_dict['dialogIcon'] = white_8
        human_dict['dialogBadgeBackground'] = self.accent.hex.replace(
            '#', '#FF').upper()
        human_dict['dialogLineProgressBackground'] = white_5
        human_dict['dialogLineProgress'] = self.accent.hex.replace(
            '#', '#FF').upper()

        # actionbar default
        human_dict['actionBarDefault'] = self.secondary.hex.replace(
            '#', '#FF').upper()
        human_dict['actionBarDefaultIcon'] = white

        # menu
        human_dict['actionBarDefaultSubmenuBackground'] = dialogs_bg

        # buttons
        human_dict['dialogButton'] = self.accent.hex.replace(
            '#', '#FF').upper()

        # checkboxs
        human_dict['dialogCheckboxSquareBackground'] = white_2
        human_dict['dialogCheckboxSquareCheck'] = white
        human_dict['dialogCheckboxSquareDisabled'] = white_2
        human_dict['dialogCheckboxSquareUnchecked'] = white_2
        human_dict['dialogRoundCheckBox'] = self.accent.hex.replace(
            '#', '#FF').upper()

        # texts
        human_dict['windowBackgroundWhiteHintText'] = white_2
        human_dict['chats_menuItemText'] = white_2
        human_dict['actionBarDefaultSubmenuItem'] = white_2
        human_dict['dialogTextGray2'] = white_2
        human_dict['actionBarDefaultTitle'] = white_5
        human_dict['dialogTextBlack'] = white_5
        human_dict['dialogBadgeText'] = white_5
        # optional link color?
        human_dict['dialogLinkSelection'] = self.accent.hex.replace(
            '#', '#FF').upper()

        utils.to_file(utils.to_string(human_dict), "out/human_readable")

        out_contents = utils.to_string(utils.hdict_to_tgdict(human_dict))

        utils.to_file(
            out_contents, 'out/android'
        )

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
            black = Color(hex="#FF000000")
            white_2 = white.edit_alpha(-0.8).hex
            white_5 = white.edit_alpha(-0.5).hex
            white_8 = white.edit_alpha(-0.2).hex
            white_9 = white.edit_alpha(-0.1).hex
            black_9 = black.edit_alpha(-0.1).hex
            black_8 = black.edit_alpha(-0.2).hex
            black_5 = black.edit_alpha(-0.5).hex
            black_2 = black.edit_alpha(-0.8).hex

            bgsect_color = self.primary.lighten(-0.2).hex
            dialogs_bg = self.primary.lighten(-0.25).hex

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

            # actionbar
            self.theme_dict['actionBarDefault'] = self.secondary.hex
            self.theme_dict['actionBarDefaultIcon'] = white.hex
            self.theme_dict['avatar_backgroundActionBarBlue'] = self.secondary.hex
            self.theme_dict['actionBarDefaultTitle'] = white_9
            self.theme_dict['actionBarDefaultArchived'] = self.secondary.hex

            # menu
            self.theme_dict['chats_menuItemIcon'] = self.secondary.lighten(
                1).hex
            self.theme_dict['chats_menuItemText'] = white_8

            # submenu
            self.theme_dict['actionBarDefaultSubmenuBackground'] = dialogs_bg
            self.theme_dict['actionBarDefaultSubmenuItemIcon'] = self.secondary.lighten(
                1).hex
            self.theme_dict['actionBarDefaultSubmenuItem'] = white_8

            # dialogs
            self.theme_dict['dialogTextGray2'] = white_8
            self.theme_dict['dialogTextBlack'] = white_8
            self.theme_dict['dialogBadgeText'] = white_8

            # buttons
            self.theme_dict['dialogButton'] = self.accent.hex
            self.theme_dict['chats_actionIcon'] = self._accent_text(
                self.accent).edit_alpha(-0.5)
            self.theme_dict['profile_actionIcon'] = self._accent_text(
                self.accent).edit_alpha(-0.5)
            self.theme_dict['chats_actionBackground'] = self.accent.hex
            self.theme_dict['chats_actionPressedBackground'] = self.accent.lighten(
                0.2).hex
            self.theme_dict['profile_actionBackground'] = self.accent.hex
            self.theme_dict['profile_actionPressedBackground'] = self.accent.lighten(
                0.2).hex

            # switchs
            self.theme_dict['switchTrackChecked'] = self.accent.hex

            # checkboxs
            self.theme_dict['dialogCheckboxSquareBackground'] = white_2
            self.theme_dict['dialogCheckboxSquareCheck'] = white.hex
            self.theme_dict['dialogCheckboxSquareDisabled'] = white_2
            self.theme_dict['dialogCheckboxSquareUnchecked'] = white_2
            self.theme_dict['dialogRoundCheckBox'] = self.accent.hex

            # avatar
            self.theme_dict['avatar_nameInMessageBlue'] = self.accent.hex

            # chat
            self.theme_dict['chat_inBubble'] = self.primary.lighten(0.1).hex
            self.theme_dict['chat_inBubbleSelected'] = self.primary.lighten(
                0.1).lighten(0.1).hex
            self.theme_dict['chat_outBubble'] = self.secondary.lighten(0.1)
            self.theme_dict['chat_outBubbleSelected'] = self.secondary.lighten(
                0.1).lighten(0.1).hex
            self.theme_dict['chat_messageLinkIn'] = self.accent.hex
            self.theme_dict['chat_messageLinkOut'] = self.accent.lighten(0.2)
            self.theme_dict['chat_outSentCheck'] = self.accent.hex
            self.theme_dict['chat_outSentCheckSelected'] = self.accent.lighten(
                0.1).hex
            self.theme_dict['chat_outSentClock'] = self.accent.lighten(
                -0.2).hex
            self.theme_dict['chat_outSentClockSelected'] = self.accent.lighten(
                0.1).hex
            self.theme_dict['chat_inSentClock'] = self.secondary.lighten(
                -0.1).hex
            self.theme_dict['chat_inSentClockSelected'] = self.secondary.lighten(
                -0.1).lighten(0.2)

            self.theme_dict['chat_messagePanelSend'] = self.accent.hex
            self.theme_dict['chat_messagePanelHint'] = white_5
            self.theme_dict['chat_messagePanelIcons'] = self.secondary.lighten(
                1).hex
            self.theme_dict['chat_messagePanelBackground'] = self.primary.lighten(
                -0.1).hex
            self.theme_dict['chats_nameMessage_threeLines'] = self.accent.lighten(
                0.1).hex
            self.theme_dict['chats_nameMessage'] = self.accent.lighten(
                0.1).hex
            self.theme_dict['chat_emojiPanelBackground'] = self.primary.lighten(
                0.2).hex
            self.theme_dict['chat_emojiPanelNewTrending'] = self.accent.hex
            self.theme_dict['chat_emojiPanelIconSelected'] = self.accent.hex
            self.theme_dict['chat_emojiPanelBadgeBackground'] = self.accent.hex
            self.theme_dict['chat_topPanelBackground'] = self.primary.lighten(
                -0.1).hex
            self.theme_dict['chat_topPanelTitle'] = self.accent.hex
            self.theme_dict['chat_topPanelLine'] = self.accent.hex
            self.theme_dict['chat_replyPanelName'] = self.accent.lighten(
                0.1).hex
            self.theme_dict['chat_replyPanelIcons'] = self.accent.hex
            self.theme_dict['chat_goDownButtonCounterBackground'] = self.accent.hex
            self.theme_dict['chat_goDownButtonCounter'] = self._accent_text(self.accent).edit_alpha(
                -0.5)
            self.theme_dict['chat_fieldOverlayText'] = self.accent.edit_alpha(
                -0.25)

            # texts
            self.theme_dict['windowBackgroundWhiteHintText'] = white_2
            self.theme_dict['windowBackgroundWhiteLinkText'] = self.accent.hex
            self.theme_dict['windowBackgroundWhiteValueText'] = self.accent.hex
            self.theme_dict['windowBackgroundWhiteGrayIcon'] = self.secondary.lighten(
                1).hex
            # optional link color?
            self.theme_dict['dialogLinkSelection'] = self.accent.hex
            self.theme_dict['windowBackgroundWhiteBlueHeader'] = self.accent.hex

        os.mkdir('out', 0o755)

        self.to_file(self.telegram_string, 'out/android')

    def _accent_text(self, color):
        mid = Color(hex="#FF808080")
        if color.argb > mid.argb:
            return Color(hex='#FF000000')
        elif color.argb < mid.argb:
            return Color(hex='#FFFFFFFF')

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

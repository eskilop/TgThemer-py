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

            def set(key, color):
                self.theme_dict[key] = color.hex

            pri_text = self._accent_text(self.primary)
            sec_text = self._accent_text(self.secondary)
            acc_text = self._accent_text(self.accent)
            title_text = pri_text.alpha(-0.1)
            msg_text = pri_text.alpha(-0.2)
            info_text = pri_text.alpha(-0.75)

            set('windowBackgroundWhite', self.primary)
            set('actionBarDefault', self.secondary)
            set('actionBarDefaultIcon', sec_text.alpha(-0.1))
            set('actionBarDefaultTitle', sec_text.alpha(-0.1))
            set('actionBarDefaultSelector', acc_text.alpha(-0.8))
            set('actionBarDefaultSearch', sec_text.alpha(-0.2))
            set('actionBarDefaultSearchPlaceholder', sec_text.alpha(-0.8))
            set('actionBarActionModeDefaultIcon', sec_text.alpha(-0.1))
            set('actionBarActionModeDefault', self.secondary)
            set('actionBarActionModeDefaultTop', self.secondary.lighten(0.25))
            set('actionBarActionModeDefaultSelector', acc_text.alpha(-0.8))
            set('divider', pri_text.alpha(-0.9))
            set('emptyListPlaceholder', pri_text.alpha(-0.8))
            set('progressCircle', self.accent)
            set('chats_nameMessage_threeLines', self.accent.alpha(-0.2))
            set('chats_message', msg_text)
            set('chats_actionIcon', acc_text.alpha(-0.5))
            set('chats_actionBackground', self.accent)
            set('chats_actionPressedBackground', self.accent.lighten(0.25))
            set('avatar_text', acc_text.alpha(-0.5))
            set('avatar_backgroundSaved', self.accent)
            set('avatar_backgroundArchived', self.secondary.lighten(0.5))
            set('avatar_backgroundArchivedHidden', self.secondary.lighten(0.25))
            set('chats_unreadCounter',  self.accent)
            set('chats_unreadCounterMuted', self.secondary.lighten(0.5))
            set('chats_unreadCounterText', acc_text.alpha(-0.5))
            set('chats_name', title_text)
            set('chats_secretName', self.accent.alpha(-0.15))
            set('chats_secretIcon', self.accent.alpha(-0.15))
            # set('chats_draft', )
            set('chats_pinnedIcon', pri_text.alpha(-0.5))
            set('chats_message_threeLines', msg_text)
            set('chats_nameMessage', self.accent.alpha(-0.25))
            set('chats_attachMessage', msg_text)
            set('chats_nameArchived', self.accent.alpha(-0.25))
            set('chats_messageArchived', msg_text)
            set('chats_actionMessage', msg_text)
            set('chats_date', msg_text)
            set('chats_pinnedOverlay', acc_text.alpha(-0.75))
            # set('chats_tabletSelectedOverlay')
            set('chats_sentCheck', self.accent.alpha(-0.2))
            set('chats_sentClock', msg_text)
            # set('chats_sentError') chats_sentErrorIcon
            set('chats_verifiedCheck', acc_text.alpha(-0.5))
            set('chats_verifiedBackground', self.accent.alpha(-0.2))
            set('chats_muteIcon', msg_text)
            set('chats_mentionIcon', acc_text)
            set('chats_archivePinBackground', self.primary.lighten(0.5))
            set('chats_archiveBackground', self.accent)
            set('chats_archiveIcon', acc_text)
            set('chats_menuBackground', self.primary.lighten(-0.25))
            set('chats_menuName', self.accent.alpha(-0.2))
            set('chats_menuPhone', info_text)
            # set('chats_menuPhoneCats', ) 'chats_menuCloudBackgroundCats',
            # chat_serviceBackground, chats_menuTopShadow
            set('avatar_backgroundActionBarBlue', self.secondary)
            set('chats_menuItemIcon', self.secondary.lighten(1))
            set('chats_menuItemText', msg_text)
            set('windowBackgroundWhiteGrayText3', info_text)
            set('windowBackgroundWhiteBlueText3', self.accent.alpha(-0.2))
            set('key_graySectionText', info_text)
            set('graySection', self.primary.lighten(-0.25))
            set('windowBackgroundWhiteBlackText', msg_text)
            set('actionBarDefaultArchived', self.secondary)
            set('windowBackgroundGrayShadow', Color(hex='#FF000000'))
            set('windowBackgroundGray', self.primary.lighten(-0.25))
            set('chats_archiveText', acc_text.alpha(-0.25))
            set('chats_onlineCircle', self.accent)
            set('inappPlayerBackground', self.primary.lighten(0.15))
            set('inappPlayerPlayPause', self.secondary.lighten(0.25))
            set('inAppPlayerTitle', msg_text)
            set('inappPlayerPerformer', msg_text)
            set('inappPlayerClose', pri_text)
            set('returnToCallBackground', self.accent)
            set('returnToCallText', acc_text)
            set('undo_background', self.secondary)
            set('undo_cancelColor', self.accent)
            set('undo_infoColor', sec_text)
            set('dialogBackground', self.secondary)
            # set('dialogBackgroundGray')
            set('dialogTextBlack', sec_text.lighten(-0.1))
            set('dialogTextLink', self.accent)
            set('dialogLinkSection', self.accent.alpha(-0.25))
            set('dialogTextBlue', self.accent)
            set('dialogTextBlue2', self.accent)
            set('dialogTextBlue3', self.accent)
            set('dialogTextBlue4', self.accent)
            # dialogTextRed dialogTextRed2
            set('dialogTextGray', sec_text)
            set('dialogTextGray2', sec_text)
            set('dialogTextGray3', sec_text)
            set('dialogTextGray4', sec_text)
            set('dialogIcon', title_text)
            # set('dialogRedIcon')
            set('dialogTextHint', sec_text.alpha(-0.1))
            set('dialogInputField', self.secondary)
            set('dialogInputFieldActivated', self.accent)
            set('dialogCheckboxSquareBackground', self.accent)
            set('dialogCheckboxSquareCheck', acc_text)
            set('dialogCheckboxSquareUnchecked', self.primary)
            set('dialogCheckboxSquareDisabled', self.primary.lighten(-0.1))
            set('dialogRadioBackground', self.primary)
            set('dialogRadioBackgroundChecked', self.accent)
            set('dialogProgressCircle', self.accent)
            set('dialogButton', self.accent)
            set('dialogButtonSelector', acc_text.alpha(-0.8))
            set('dialogScrollGlow', sec_text.lighten(0.25))
            set('dialogRoundCheckBox', self.accent)
            set('dialogRoundCheckBoxCheck', acc_text)
            set('dialogBadgeBackground', self.accent)
            set('dialogBadgeText', acc_text)
            set('dialogLineProgress', self.accent)
            set('dialogLineProgressBackground', self.primary)
            # set('dialogGrayLine',
            set('dialogSearchBackground', self.secondary)
            set('dialogSearchHint', info_text)
            set('dialogSearchIcon', msg_text)
            set('dialogSearchText', msg_text)
            set('dialogFloatingIcon', acc_text)
            # dialogShadowLine key_sheet_scrollUp key_sheet_other
            set('player_actionBar', self.secondary)
            set('player_actionBarSelecto', self.secondary.alpha(-0.7))
            set('player_actionBarTitle', sec_text)
            set('player_actionBarTop', self.secondary.lighten(0.5))
            set('player_actionBarSubtitle', sec_text)
            set('player_actionBarItems', sec_text.alpha(-0.1))
            set('player_background', self.primary)
            set('player_time', msg_text)
            set('player_progressBackground', self.secondary)
            # set('key_player_progressCachedBackground')
            set('player_progress', self.accent)
            set('player_placeholder', sec_text)
            set('player_placeholderBackground', self.secondary)
            set('player_button', pri_text.alpha(-0.1))
            set('player_buttonActive', self.accent)

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

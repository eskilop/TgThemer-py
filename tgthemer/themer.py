#!/usr/bin/env python3
from .color import Color
import shutil
import os

std_none = "#FF000000"


class Themer:

    def __init__(self, primary=std_none, secondary=std_none, accent=std_none,
                 mode=None, ttype="dark"):
        self.primary = Color(primary)
        self.ttype = ttype
        if mode is None:
            self.mode = 'lighten' if self.ttype == 'dark' else 'darken'
        else:
            self.mode = mode
        if secondary == std_none:
            self.secondary = self.primary.lighten(0.5) \
                if self.mode == 'lighten' \
                else self.primary.lighten(-0.5)
        else:
            self.secondary = Color(secondary)
        self.tertiary = self.secondary.lighten(0.75) \
            if self.mode == 'lighten' \
            else self.secondary.lighten(-0.75)
        self.accent = Color(accent)

        self.contents = ""
        self.theme_dict = {}

        if not os.path.exists("out"):
            os.mkdir('out', 0o755)

    def _read_file(self, inputfile):
        source = open(inputfile+'.attheme', 'r')
        contents = source.read()
        source.close()
        self.contents = contents
        self.theme_dict = self._to_dict()

    def _to_file(self, contents, outfile):
        result = open(outfile+'.attheme', 'w')
        result.write(contents)
        result.close()

    def _accent_text(self, color):
        mid = Color("#FF808080")
        if color.argb > mid.argb:
            return Color('#FF000000')
        elif color.argb < mid.argb:
            return Color('#FFFFFFFF')
        else:  # either one will go
            return Color('#FF000000')

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

    def clear(self):
        shutil.rmtree('out', ignore_errors=True)

    @property
    def human_dict(self):
        return self._transform_dict(
            lambda x: Color(int(x)).hex
        )

    @property
    def telegram_dict(self):
        return self._transform_dict(
            lambda x: Color(x).sint
        )

    @property
    def telegram_string(self):
        return self._to_string(self.telegram_dict)

    @property
    def human_string(self):
        return self._to_string(self.human_dict)

    def generate_android(self, custom=None, out=None):

        source = "sources/android/source_dark" \
            if self.ttype == 'dark' \
            else "sources/android/source_light"

        self._read_file(source)
        self.theme_dict = self.human_dict

        if custom is not None:
            for k, v in custom.items():
                self.theme_dict[k] = v
        else:

            def set(key, color):
                self.theme_dict[key] = color.hex

            pri_text = self._accent_text(self.primary)
            sec_text = self._accent_text(self.secondary)
            ter_text = self._accent_text(self.tertiary)
            acc_text = self._accent_text(self.accent)
            acc_icon = acc_text.alpha(-0.5)

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
            set('actionBarActionModeDefaultSelector', acc_text.alpha(-0.8))
            set('divider', pri_text.alpha(-0.9))
            set('emptyListPlaceholder', pri_text.alpha(-0.8))
            set('progressCircle', self.accent)
            set('chats_nameMessage_threeLines', self.accent.alpha(-0.2))
            set('chats_message', msg_text)
            set('chats_actionIcon', acc_icon)
            set('chats_actionBackground', self.accent)
            set('avatar_text', acc_icon)
            set('avatar_backgroundSaved', self.accent)
            set('chats_unreadCounter',  self.accent)
            set('chats_unreadCounterText', acc_icon)
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
            set('chats_pinnedOverlay', Color("#FF000000").alpha(-0.75))
            # set('chats_tabletSelectedOverlay')
            set('chats_sentCheck', self.accent.alpha(-0.2))
            set('chats_sentClock', msg_text)
            # set('chats_sentError') chats_sentErrorIcon
            set('chats_verifiedCheck', acc_icon)
            set('chats_verifiedBackground', self.accent.alpha(-0.2))
            set('chats_muteIcon', msg_text)
            set('chats_mentionIcon', acc_text)
            set('chats_archiveBackground', self.accent)
            set('chats_archiveIcon', acc_text)
            set('chats_menuName', self.accent.alpha(-0.2))
            set('chats_menuPhone', info_text)
            # set('chats_menuPhoneCats', ) 'chats_menuCloudBackgroundCats',
            # chat_serviceBackground, chats_menuTopShadow
            set('avatar_backgroundActionBarBlue', self.secondary)
            set('chats_menuItemText', msg_text)
            set('windowBackgroundWhiteGrayText3', info_text)
            set('windowBackgroundWhiteBlueText3', self.accent.alpha(-0.2))
            set('key_graySectionText', info_text)
            set('windowBackgroundWhiteBlackText', msg_text)
            set('actionBarDefaultArchived', self.secondary)
            set('windowBackgroundGrayShadow', Color('#FF000000'))
            set('chats_archiveText', acc_text.alpha(-0.25))
            set('chats_onlineCircle', self.accent)
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
            set('dialogRadioBackground', self.primary)
            set('dialogRadioBackgroundChecked', self.accent)
            set('dialogProgressCircle', self.accent)
            set('dialogButton', self.accent)
            set('dialogButtonSelector', acc_text.alpha(-0.8))
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

            set('actionBarDefaultSubmenuItem', sec_text)
            set('actionBarDefaultSubtitle', sec_text)
            set('chat_muteIcon', sec_text)
            set('chat_lockIcon', self.accent)
            set('chat_inBubble', self.secondary)
            set('chat_outBubble', self.tertiary)
            set('chat_outBubbleSelected', self.tertiary)
            set('chat_serviceText', pri_text)
            set('chat_serviceLink', self.accent.alpha(-0.25))
            set('chat_serviceIcon', self.tertiary)
            set('chat_serviceBackground', self.primary)
            set('chat_messageTextIn', sec_text.alpha(-0.15))
            set('chat_messageTextOut', ter_text)
            set('chat_messageLinkIn', self.accent)
            set('chat_mediaTimeText', info_text)
            set('chat_outSentCheck', self.accent)
            set('chat_outSentCheckSelected', self.accent)
            set('chat_mediaSentCheck', msg_text)
            set('chat_mediaSentClock', msg_text)
            set('chat_outViews', self.accent.alpha(-0.6))
            set('chat_outViewsSelected', self.accent.alpha(-0.4))
            set('chat_inViews', self.accent.alpha(-0.8))
            set('chat_inViewsSelected', self.accent.alpha(-0.6))
            # chat_mediaViews
            set('chat_outMenu', ter_text.alpha(-0.2))
            set('chat_outMenuSelected', ter_text.alpha(-0.3))
            set('chat_inMenu', sec_text.alpha(-0.2))
            set('chat_inMenuSelected', sec_text.alpha(-0.3))
            # set('chat_mediaMenu',)
            set('chat_outInstant', self.accent)
            set('chat_inInstant', self.accent)
            set('chat_inInstantSelected', self.accent.alpha(-0.2))
            # calls_callReceivedRedIcon calls_callReceivedGreenIcon chat_SentError
            # chat_sentErrorIcon
            set('chat_selectedBackground', self.secondary.alpha(-0.6))
            set('chat_previewDurationText', info_text)
            set('chat_previewGameText', info_text)
            set('chat_outPreviewInstantText', self.accent)
            set('chat_outPreviewInstantSelectedText', self.accent)
            # chat_secretTimeText chat_stickerNameText chat_botProgress chat_mediaTimeBackground
            set('chat_botButtonText', self.accent.alpha(-0.25))
            set('chat_inForwardedNameText', self.accent.alpha(-0.25))
            set('chat_outForwardedNameText', self.accent.alpha(-0.15))
            set('chat_inViaBotNameText', self.accent.alpha(-0.25))
            set('chat_outViaBotNameText', self.accent.alpha(-0.15))
            set('chat_inReplyLine', self.accent.alpha(-0.25))
            set('chat_outReplyLine', self.accent.alpha(-0.15))
            set('chat_inReplyNameText', self.accent.alpha(-0.25))
            set('chat_outReplyNameText', self.accent.alpha(-0.15))
            set('chat_inReplyMessageText', self.accent.alpha(-0.25))
            set('chat_outReplyMessageText', self.accent.alpha(-0.15))
            set('chat_inReplyMediaMessageText', self.accent.alpha(-0.25))
            set('chat_outReplyMediaMessageText', self.accent.alpha(-0.15))
            set('chat_inReplyMediaMessageSelectedText', self.accent.alpha(-0.25))
            set('chat_outReplyMediaMessageSelectedText', self.accent.alpha(-0.15))
            set('chat_inPreviewLine', self.accent.alpha(-0.25))
            set('chat_outPreviewLine', self.accent.alpha(-0.15))
            set('chat_inContactNameText', self.accent.alpha(-0.25))
            set('chat_outContactNameText', self.accent.alpha(-0.5))
            set('chat_inSiteNameText', self.accent.alpha(-0.25))
            set('chat_outSiteNameText', self.accent.alpha(-0.15))
            set('chat_inContactPhoneText', self.accent.alpha(-0.25))
            set('chat_outContactPhoneText', self.accent.alpha(-0.15))
            set('chat_inContactPhoneSelectedText', self.accent.alpha(-0.25))
            set('chat_outContactPhoneSelectedText', self.accent.alpha(-0.15))
            set('chat_mediaProgress ', msg_text)
            set('chat_inAudioProgress', sec_text)
            set('chat_outAudioProgress', ter_text)
            set('chat_inAudioSelectedProgress', sec_text)
            set('chat_outAudioSelectedProgress', ter_text)
            set('chat_inTimeText', sec_text)
            set('chat_outTimeText', ter_text)
            set('chat_inTimeSelectedText', sec_text.alpha(-0.1))
            set('chat_adminText', msg_text)
            set('chat_adminSelectedText', msg_text)
            set('chat_outTimeSelectedText', ter_text.alpha(-0.1))
            set('chat_outTimeSelectedText', sec_text.alpha(-0.1))
            set('chat_inAudioPerfomerText', self.accent.alpha(-0.25))
            set('chat_outAudioPerfomerText', self.accent.alpha(-0.25))
            set('chat_inAudioPerfomerSelectedText', self.accent.alpha(-0.25))
            set('chat_outAudioPerfomerSelectedText', self.accent.alpha(-0.25))
            set('chat_inAudioTitleText', sec_text)
            set('chat_outAudioTitleText', ter_text)
            set('chat_inAudioDurationText', ter_text.alpha(-0.25))
            set('chat_outAudioDurationText', sec_text.alpha(-0.25))
            set('chat_inAudioDurationSelectedText', ter_text.alpha(-0.25))
            set('chat_outAudioDurationSelectedText', sec_text.alpha(-0.25))
            set('chat_inAudioSeekbar', self.primary)
            set('chat_outAudioSeekbar', self.secondary)
            set('chat_inAudioSeekbarSelected', self.primary)
            set('chat_outAudioSeekbarSelected', self.secondary)
            set('chat_inAudioSeekbarFill', self.accent)
            set('chat_outAudioSeekbarFill', self.accent)
            set('chat_inAudioCacheSeekbar', self.primary)
            set('chat_outAudioCacheSeekbar', self.secondary)
            set('chat_inVoiceSeekbar', self.primary)
            set('chat_outVoiceSeekbar', self.secondary)
            set('chat_inVoiceSeekbarSelected', self.primary)
            set('chat_outVoiceSeekbarSelected', self.secondary)
            set('chat_inVoiceSeekbarFill', self.accent.alpha(-0.25))
            set('chat_outVoiceSeekbarFill', self.accent.alpha(-0.25))
            set('chat_inFileNameText', sec_text)
            set('chat_outFileNameText', ter_text)
            set('chat_inFileInfoText', sec_text)
            set('chat_outFileInfoText', ter_text)
            set('chat_inFileInfoSelectedText', sec_text)
            set('chat_outFileInfoSelectedText', ter_text)
            set('chat_inVenueInfoText', self.accent.alpha(-0.25))
            set('chat_outVenueInfoText', self.accent.alpha(-0.15))
            set('chat_inVenueInfoSelectedText', self.accent.alpha(-0.25))
            set('chat_outVenueInfoSelectedText', self.accent.alpha(-0.15))
            set('chat_linkSelectBackground', self.accent.alpha(-0.75))
            set('chat_textSelectBackground', self.accent.alpha(-0.25))
            set('chat_messagePanelBackground', self.secondary)
            set('chat_inLoader', self.primary)
            set('chat_outLoader', self.secondary)
            set('chat_inLoaderSelected', self.primary)
            set('chat_outLoaderSelected', self.secondary)
            set('chat_inMediaIcon', self.accent)
            set('chat_outMediaIcon', self.accent)
            set('chat_inMediaIconSelected', self.accent)
            set('chat_outMediaIconSelected', self.accent)
            set('chat_mediaLoaderPhoto', self.primary)
            set('chat_mediaLoaderPhotoIcon', self.accent)
            set('chat_mediaLoaderPhotoSelected', self.primary)
            set('chat_mediaLoaderPhotoIconSelected', self.accent)
            set('chat_outLoaderPhoto', self.secondary)
            set('chat_outLoaderPhotoSelected', self.secondary)
            set('chat_outLoaderPhotoIcon', self.accent)
            set('chat_outLoaderPhotoIconSelected', self.accent)
            set('chat_inLoaderPhoto', self.primary)
            set('chat_inLoaderPhotoSelected', self.primary)
            set('chat_inLoaderPhotoIcon', self.accent)
            set('chat_inLoaderPhotoIconSelected', self.accent)
            set('chat_outFileIcon', self.accent)
            set('chat_outFileSelectedIcon', self.accent)
            set('chat_inFileIcon', self.accent)
            set('chat_inFileSelectedIcon', self.accent)
            set('chat_inContactBackground', self.primary)
            set('chat_outContactBackground', self.secondary)
            set('chat_inContactIcon', self.accent)
            set('chat_outContactIcon', self.accent)
            set('chat_inLocationBackground', self.primary)
            set('chat_outLocationBackground', self.secondary)
            set('chat_inLocationIcon', self.accent)
            set('chat_outLocationIcon', self.accent)
            # chat_messagePanelShadow' default ok
            set('chat_fieldOverlayText', self.accent)
            set('chat_messagePanelText', pri_text)
            set('chat_messagePanelHint', pri_text.alpha(-0.8))
            set('chat_messagePanelSend', self.accent)
            set('chat_messagePanelIcons', pri_text.alpha(-0.5))
            set('chat_messagePanelVoicePressed', acc_icon)
            set('key_chat_messagePanelVoiceLock', pri_text.alpha(-0.5))
            set('key_chat_messagePanelVoiceLockBackground', self.secondary)
            set('chat_messagePanelVoiceBackground', self.accent)
            # 'key_chat_messagePanelVoiceLockShadow' ok
            set('chat_messagePanelVoiceDelete', msg_text)
            set('chat_recordedVoiceBackground', self.accent)
            set('chat_recordTime', msg_text)
            set('chat_recordVoiceCancel', msg_text)
            set('chat_messagePanelVoiceDuration', title_text)
            set('contextProgressInner1', self.accent.alpha(-0.5))
            set('contextProgressOuter1', self.accent)
            set('chat_messagePanelCancelInlineBot', pri_text.alpha(-0.5))
            # chat_recordedVoiceDot ok
            # chat_messagePanelVoiceShadow ok
            set('chat_recordedVoiceProgress', self.accent.alpha(-0.5))
            set('chat_recordedVoiceProgressInner', msg_text)
            set('chat_recordedVoicePlayPause', msg_text)
            set('chat_recordedVoicePlayPausePressed', self.accent.alpha(-0.8))
            set('chat_emojiPanelNewTrending', self.accent)
            set('chat_emojiPanelBackground', self.secondary)
            set('chat_emojiPanelShadowLine', pri_text.alpha(-0.9))
            set('chat_emojiPanelEmptyText', self.tertiary)
            set('chat_emojiPanelIcon', self.tertiary)
            set('chat_emojiPanelIconSelected', self.accent)
            set('chat_emojiPanelStickerPackSelector', self.tertiary)
            set('chat_emojiPanelBackspace', self.tertiary)
            set('chat_emojiPanelTrendingTitle', title_text)
            set('chat_emojiPanelTrendingDescription', msg_text)
            set('chat_emojiPanelBadgeText', acc_text.alpha(-0.2))
            set('chat_emojiPanelBadgeBackground', self.accent)
            set('chat_emojiBottomPanelIcon', self.tertiary)
            set('chat_emojiSearchIcon', self.tertiary)
            set('chat_emojiPanelStickerSetNameHighlight', self.accent)
            set('chat_emojiPanelStickerPackSelectorLine', self.accent)
            set('chatbotKeyboardButtonText', self.secondary.alpha(-0.25))
            set('chatbotKeyboardButtonBackground', self.secondary)
            set('chat_topPanelLine', self.accent)
            set('chat_topPanelTitle', self.accent)
            set('chat_topPanelMessage', sec_text)
            set('chat_addContact', self.accent)
            set('chat_replyPanelMessage', sec_text)
            set('chat_replyPanelIcons', self.accent)
            set('chat_replyPanelName', self.accent)
            set('chat_searchPanelText', self.accent)
            set('chat_searchPanelIcons', self.accent)
            set('chat_secretChatStatusText', msg_text)
            # chat_stickersHintPanel
            set('chat_unreadMessagesStartBackground', self.primary)
            set('chat_unreadMessagesStartText', msg_text)
            set('chat_botSwitchToInlineText', self.accent.alpha(-0.25))
            set('chat_inlineResultIcon', self.accent)
            set('windowBackgroundWhiteGrayText2', info_text)
            set('windowBackgroundWhiteLinkText', self.accent.alpha(-0.25))
            set('chat_gifSaveHintBackground', self.primary)
            set('chat_gifSaveHintText', msg_text)
            set('chat_attachMediaBanBackground', self.primary)
            set('chat_attachMediaBanText', msg_text)
            set('chat_goDownButtonCounterBackground', self.accent)
            set('chat_goDownButtonCounter', acc_icon)
            set('chat_goDownButton', self.secondary)
            # chat_goDownButtonShadow ok
            set('chat_goDownButtonIcon', sec_text.alpha(-0.2))
            set('chat_secretTimerBackground', self.primary)
            set('chat_secretTimerText', msg_text)
            # chat_attachCameraIcon* ok
            # chat_attach*Background ok
            # chat_attach*Icon ok
            set('chat_attachHideBackground', self.primary)
            set('chat_attachHideIcon', pri_text.alpha(-0.25))
            set('chat_attachSendBackground', self.accent)
            set('chat_attachSendIcon', acc_icon)
            # dialogCameraIcon ok
            set('avatar_actionBarIconBlue', sec_text)
            set('avatar_actionBarSelectorBlue', self.secondary.alpha(-0.8))
            set('profile_title', sec_text.alpha(-0.1))
            set('avatar_subtitleInProfileBlue', sec_text.alpha(-0.25))
            set('actionBarDefaultSubmenuItem', sec_text.alpha(-0.25))
            set('listSelectorSDK21', self.secondary.alpha(-0.8))
            set('windowBackgroundWhiteValueText', self.accent)
            set('windowBackgroundWhiteBlueHeader', self.accent)
            set('avatar_backgroundInProfileBlue', self.accent)
            set('profile_actionIcon', acc_icon)
            set('profile_actionBackground', self.accent)
            set('profile_actionPressedBackground', self.accent.alpha(-0.25))

            set('switchTrack', self.tertiary)
            set('switchTrackChecked', self.accent)
            set('radioBackground', self.primary)
            set('radioBackgroundChecked', self.accent)
            set('windowBackgroundWhiteInputField', self.secondary)
            set('windowBackgroundWhiteInputFieldActivated', self.accent)
            set('windowBackgroundWhiteBlueText4', self.accent)
            set('featuredStickers_addedIcon', self.accent)
            set('stickers_menu', pri_text.alpha(-0.5))
            set('stickers_menuSelector', pri_text.alpha(-0.7))
            set('key_changephoneinfo_changeText', self.accent)
            set('changephoneinfo_image', self.tertiary)
            set('profile_creatorIcon', self.accent)
            set('profile_verifiedBackground', self.accent)
            set('windowBackgroundWhiteLinkSelection', self.accent.alpha(-0.75))
            set('windowBackgroundWhiteBlueText', self.accent)
            set('windowBackgroundWhiteBlueText2', self.accent)
            set('windowBackgroundWhiteBlueButton', self.accent)
            set('windowBackgroundWhiteBlueIcon', self.accent)

            if self.ttype == 'dark':
                set('actionBarActionModeDefaultTop',
                    self.secondary.lighten(0.25))
                set('chats_actionPressedBackground', self.accent.lighten(0.25))
                set('avatar_backgroundArchived', self.secondary.lighten(0.5))
                set('avatar_backgroundArchivedHidden',
                    self.secondary.lighten(0.25))
                set('chats_unreadCounterMuted', self.secondary.lighten(0.5))
                set('chats_archivePinBackground', self.primary.lighten(0.5))
                set('chats_menuBackground', self.primary.lighten(-0.25))
                set('chats_menuItemIcon', self.tertiary.lighten(1))
                set('graySection', self.primary.lighten(-0.25))
                set('windowBackgroundGray', self.primary.lighten(-0.25))
                set('inappPlayerBackground', self.primary.lighten(0.15))
                set('inappPlayerPlayPause', self.secondary.lighten(0.25))
                set('dialogTextBlack', sec_text.lighten(-0.1))
                set('dialogCheckboxSquareDisabled', self.primary.lighten(-0.1))
                set('dialogScrollGlow', sec_text.lighten(0.25))
                set('player_actionBarTop', self.secondary.lighten(0.5))
                set('chat_wallpaper', self.primary.lighten(-0.25))
                set('actionBarDefaultSubmenuBackground',
                    self.secondary.lighten(-0.25))
                set('actionBarDefaultSubmenuItemIcon', self.tertiary.lighten(1))
                set('chat_inBubbleSelected', self.secondary.lighten(0.25))
                set('chat_inBubbleShadow', self.secondary.lighten(-0.25))
                set('chat_outBubbleShadow', self.tertiary.lighten(-0.25))
                set('chat_serviceBackgroundSelected', self.primary.lighten(0.25))
                set('chat_messageLinkOut', self.accent.lighten(0.25))
                set('chat_outSentClock', self.accent.lighten(0.2))
                set('chat_inSentCheck', self.accent.lighten(-0.3))
                set('chat_inSentClock', self.accent.lighten(-0.2))
                set('chat_inSentClockSelected', self.accent.lighten(-0.2))
                set('chat_outSentClockSelected', self.accent.lighten(0.1))
                set('chat_outInstantSelected', self.accent.lighten(0.2))
                set('chat_inPreviewInstantText', self.accent.lighten(0.2))
                set('chat_inPreviewInstantSelectedText', self.accent.lighten(0.2))
                set('chat_inFileProgress', self.accent.lighten(-0.25))
                set('chat_outFileProgress', self.accent.lighten(-0.15))
                set('chat_inFileProgressSelected', self.accent.lighten(-0.15))
                set('chat_outFileProgressSelected', self.accent.lighten(-0.05))
                set('chat_inFileBackground', self.accent.lighten(-0.5))
                set('chat_outFileBackground', self.accent.lighten(0.5))
                set('chat_inFileBackgroundSelected', self.accent.lighten(-0.5))
                set('chat_outFileBackgroundSelected', self.accent.lighten(0.5))
                set('chatbotKeyboardButtonBackgroundPressed',
                    self.secondary.lighten(0.1).alpha(-0.7))
                set('chat_topPanelBackground', self.secondary.lighten(-0.2))
                set('chat_unreadMessagesStartArrowIcon',
                    self.primary.lighten(0.75).alpha(-0.2))
                set('windowBackgroundWhiteGrayIcon', self.tertiary.lighten(1))

            elif self.ttype == 'light':
                set('actionBarActionModeDefaultTop',
                    self.secondary.lighten(-0.25))
                set('chats_actionPressedBackground', self.accent.lighten(-0.25))
                set('avatar_backgroundArchived', self.secondary.lighten(-0.5))
                set('avatar_backgroundArchivedHidden',
                    self.secondary.lighten(-0.25))
                set('chats_unreadCounterMuted', self.secondary.lighten(-0.5))
                set('chats_archivePinBackground', self.primary.lighten(-5))
                set('chats_menuBackground', self.primary.lighten(-0.25))
                set('chats_menuItemIcon', self.tertiary.lighten(-1))
                set('graySection', self.primary.lighten(0.25))
                set('windowBackgroundGray', self.primary.lighten(-0.25))
                set('inappPlayerBackground', self.primary.lighten(-0.15))
                set('inappPlayerPlayPause', self.secondary.lighten(-0.25))
                set('dialogTextBlack', sec_text.lighten(0.1))
                set('dialogCheckboxSquareDisabled', self.primary.lighten(0.1))
                set('dialogScrollGlow', sec_text.lighten(-0.25))
                set('player_actionBarTop', self.secondary.lighten(-0.5))
                set('chat_wallpaper', self.primary.lighten(-0.25))
                set('actionBarDefaultSubmenuBackground',
                    self.secondary.lighten(0.25))
                set('actionBarDefaultSubmenuItemIcon', self.tertiary.lighten(-1))
                set('chat_inBubbleSelected', self.secondary.lighten(-0.25))
                set('chat_inBubbleShadow', self.secondary.lighten(0.25))
                set('chat_outBubbleShadow', self.tertiary.lighten(0.25))
                set('chat_serviceBackgroundSelected',
                    self.primary.lighten(-0.25))
                set('chat_messageLinkOut', self.accent.lighten(-0.25))
                set('chat_outSentClock', self.accent.lighten(-0.2))
                set('chat_inSentCheck', self.accent.lighten(0.3))
                set('chat_inSentClock', self.accent.lighten(0.2))
                set('chat_inSentClockSelected', self.accent.lighten(0.2))
                set('chat_outSentClockSelected', self.accent.lighten(-0.1))
                set('chat_outInstantSelected', self.accent.lighten(-0.2))
                set('chat_inPreviewInstantText', self.accent.lighten(-0.2))
                set('chat_inPreviewInstantSelectedText',
                    self.accent.lighten(-0.2))
                set('chat_inFileProgress', self.accent.lighten(0.25))
                set('chat_outFileProgress', self.accent.lighten(0.15))
                set('chat_inFileProgressSelected', self.accent.lighten(0.15))
                set('chat_outFileProgressSelected', self.accent.lighten(0.05))
                set('chat_inFileBackground', self.accent.lighten(0.5))
                set('chat_outFileBackground', self.accent.lighten(-0.5))
                set('chat_inFileBackgroundSelected', self.accent.lighten(0.5))
                set('chat_outFileBackgroundSelected', self.accent.lighten(-0.5))
                set('chatbotKeyboardButtonBackgroundPressed',
                    self.secondary.lighten(-0.1).alpha(-0.7))
                set('chat_topPanelBackground', self.secondary.lighten(0.2))
                set('chat_unreadMessagesStartArrowIcon',
                    self.primary.lighten(-0.75).alpha(-0.2))
                set('windowBackgroundWhiteGrayIcon', self.tertiary.lighten(-1))

        if out is None:
            self._to_file(self.telegram_string, 'out/android')
        else:
            self._to_file(self.telegram_string, 'out/'+out)

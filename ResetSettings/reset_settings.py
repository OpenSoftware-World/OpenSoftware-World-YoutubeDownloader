#!/usr/bin/python3
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

import configparser

keyboard_settings = configparser.ConfigParser()
keyboard_settings.read('KeyboardShortcut/keyboard.ini')

lang_config = configparser.ConfigParser()
lang_config.read('Lang/lang.ini')

theme_file_config = configparser.ConfigParser()
theme_file_config.read('Theme/theme_file.ini')

theme_config = configparser.ConfigParser()
theme_config.read('Theme/theme.ini')

tray_config = configparser.ConfigParser()
tray_config.read('TrayMenu/tray.ini')

reset_settings_config = configparser.ConfigParser()
reset_settings_config.read('ResetSettings/reset_settings.ini')

ResetSettingsEnabled = reset_settings_config['ResetSettings']['resetsettingsenabled']

keyboard_settings['KeyboardShortcutSettings'] = {'keyboard_shortcut': 'True'}
keyboard_settings['KeyboardShortcut'] = {
        'window_close_shortcut': '<Control-w>',
        'video_downloader_shortcut': '<Control-v>',
        'music_downloader_shortcut': '<Control-m>',
        'playlist_downloader_shortcut': '<Control-p>',
        'video_search_shortcut': '<Control-s>',
        'downloader_shortcut': '<Control-d>'
    }

lang_config['AppLang'] = {'lang': 'en'}

theme_file_config['ThemeDataFile'] = {'name': 'theme.ini'}

theme_config['ThemeSettings'] = {
    'userTheme': 'dark',
    'pywinstyles_theme': 'dark'
}
theme_config['FontSettings'] = {
    'userFont': 'Arial',
    'userFontSize': '15',
    'userTitleFontSize': '30',
    'userFontBold': 'True'
}
theme_config['CornerRadiusSettings'] = {'userCornerRadiusValue': '9'}
theme_config['ButtonAppearanceSettings'] = {
    'userButtonColor': 'default',
    'userButtonHoverColor': 'default',
    'userButtonTextColor': 'default',
    'userButtonBorderColor': 'default',
    'userButtonBorderWidth': 'default'
}
theme_config['WindowSettings'] = {'userWindowTitleColor': 'default'}

tray_config['TraySettings'] = {'tray_visible': 'True'}

reset_settings_config['ResetSettings']['resetsettingsenabled'] = 'false'

if ResetSettingsEnabled.lower() == "all":
    with open('ResetSettings/reset_settings.ini', 'w') as configfile:
        reset_settings_config.write(configfile)
    with open('KeyboardShortcut/keyboard.ini', 'w') as configfile:
        keyboard_settings.write(configfile)
    with open('Lang/lang.ini', 'w') as configfile:
        lang_config.write(configfile)
    with open('Theme/theme_file.ini', 'w') as configfile:
        theme_file_config.write(configfile)
    with open('Theme/theme.ini', 'w') as configfile:
        theme_config.write(configfile)
    with open('TrayMenu/tray.ini', 'w') as configfile:
        tray_config.write(configfile)
elif ResetSettingsEnabled == "keyboardshortcut":
    with open('ResetSettings/reset_settings.ini', 'w') as configfile:
        reset_settings_config.write(configfile)
    with open('KeyboardShortcut/keyboard.ini', 'w') as configfile:
        keyboard_settings.write(configfile)
elif ResetSettingsEnabled == "lang":
    with open('ResetSettings/reset_settings.ini', 'w') as configfile:
        reset_settings_config.write(configfile)
    with open('Lang/lang.ini', 'w') as configfile:
        lang_config.write(configfile)
elif ResetSettingsEnabled == "theme":
    with open('ResetSettings/reset_settings.ini', 'w') as configfile:
        reset_settings_config.write(configfile)
    with open('Theme/theme_file.ini', 'w') as configfile:
        theme_file_config.write(configfile)
    with open('Theme/theme.ini', 'w') as configfile:
        theme_config.write(configfile)
elif ResetSettingsEnabled == "traymenu":
    with open('ResetSettings/reset_settings.ini', 'w') as configfile:
        reset_settings_config.write(configfile)
    with open('TrayMenu/tray.ini', 'w') as configfile:
        tray_config.write(configfile)
elif ResetSettingsEnabled == "false":
    pass
else:
    print("Invalid input!")
#!/usr/bin/python3
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

import configparser

theme_config = configparser.ConfigParser()
theme_config.read('Theme/theme.ini')

userTheme = theme_config['ThemeSettings']['userTheme']
pywinstyles_theme = theme_config['ThemeSettings']['pywinstyles_theme']
userFont = theme_config['FontSettings']['userFont']
userFontSize = int(theme_config['FontSettings']['userFontSize'])
userTitleFontSize = int(theme_config['FontSettings']['userTitleFontSize'])
userFontBold = theme_config['FontSettings']['userFontBold']
userCornerRadiusValue = int(theme_config['CornerRadiusSettings']['userCornerRadiusValue'])

userButtonColor = theme_config['ButtonAppearanceSettings']['userButtonColor']
userButtonHoverColor = theme_config['ButtonAppearanceSettings']['userButtonHoverColor']
userButtonTextColor = theme_config['ButtonAppearanceSettings']['userButtonTextColor']
userButtonBorderColor = theme_config['ButtonAppearanceSettings']['userButtonBorderColor']
userButtonBorderWidth = theme_config['ButtonAppearanceSettings']['userButtonBorderWidth']
userWindowTitleColor = theme_config['WindowSettings']['userWindowTitleColor']

if userFontBold == "False":
    userFontBold = "normal"
else:
    userFontBold = "bold"

if userButtonColor == "default":
    userButtonColor = None

if userButtonHoverColor == "default":
    userButtonHoverColor = None

if userButtonTextColor == "default":
    userButtonTextColor = None

if userButtonBorderColor == "default":
    userButtonBorderColor = None

if userButtonBorderWidth == "default":
    userButtonBorderWidth = None
else:
    userButtonBorderWidth = int(userButtonBorderWidth)

if userWindowTitleColor == "default":
    userWindowTitleColor = None
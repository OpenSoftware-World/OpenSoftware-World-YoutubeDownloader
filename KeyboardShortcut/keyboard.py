#!/usr/bin/python3
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

import configparser

keyboard_settings = configparser.ConfigParser()
keyboard_settings.read('KeyboardShortcut/keyboard.ini')

keyboard_shortcut = keyboard_settings['KeyboardShortcutSettings']['keyboard_shortcut']

if keyboard_shortcut == "True":
    keyboard_shortcut = True
else:
    keyboard_shortcut = False

if keyboard_shortcut == True:
    window_close_shortcut = keyboard_settings['KeyboardShortcut']['window_close_shortcut']
    video_downloader_shortcut = keyboard_settings['KeyboardShortcut']['video_downloader_shortcut']
    music_downloader_shortcut = keyboard_settings['KeyboardShortcut']['music_downloader_shortcut']
    playlist_downloader_shortcut = keyboard_settings['KeyboardShortcut']['playlist_downloader_shortcut']
    video_search_shortcut = keyboard_settings['KeyboardShortcut']['video_search_shortcut']
    downloader_shortcut = keyboard_settings['KeyboardShortcut']['downloader_shortcut']
else:
    window_close_shortcut = None
    video_downloader_shortcut = None
    music_downloader_shortcut = None
    playlist_downloader_shortcut = None
    video_search_shortcut = None
    downloader_shortcut = None
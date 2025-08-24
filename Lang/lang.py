#!/usr/bin/python3
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

import configparser

lang_config = configparser.ConfigParser()
lang_config.read('Lang/lang.ini')

lang = lang_config['AppLang']['lang']

langconfig = configparser.ConfigParser()
langconfig.read(f'Lang/{lang}.ini')

music_file_name = langconfig['LangContent']['music_file_name']
playlist_file_name = langconfig['LangContent']['playlist_file_name']
option_one = langconfig['LangContent']['option_one']
option_two = langconfig['LangContent']['option_two']
option_three = langconfig['LangContent']['option_three']
option_four = langconfig['LangContent']['option_four']
download_txt = langconfig['LangContent']['download_txt']
search_txt = langconfig['LangContent']['search_txt']
video_url_txt = langconfig['LangContent']['video_url_txt']
music_url_txt = langconfig['LangContent']['music_url_txt']
playlist_url_txt = langconfig['LangContent']['playlist_url_txt']
video_search_txt = langconfig['LangContent']['video_search_txt']
github_repo_txt = langconfig['LangContent']['github_repo_txt']
my_github_acc_txt = langconfig['LangContent']['my_github_acc_txt']
documents_txt = langconfig['LangContent']['documents_txt']
about_txt = langconfig['LangContent']['about_txt']
windows_not_os_txt = langconfig['LangContent']['windows_not_os_txt']
open_txt = langconfig['LangContent']['open_txt']
close_txt = langconfig['LangContent']['close_txt']
downloaded_successfully = langconfig['LangContent']['downloaded_successfully']
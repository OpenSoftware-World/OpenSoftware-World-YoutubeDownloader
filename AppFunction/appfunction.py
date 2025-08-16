from AppFunction.Lib.lib import *
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

file_name = ["Video",music_file_name,playlist_file_name]

for i in file_name:
    if not os.path.exists(i):
        os.mkdir(i)

def messagebox(message):
    CTkMessagebox(title=message, message=message)

def video_download(video_url):
    options = {
        'format': 'best',
        'outtmpl': 'Video/%(title)s.%(ext)s',
    }
    with YoutubeDL(options) as yt_dlp:
        yt_dlp.download([video_url])
        messagebox("Video "+downloaded_successfully)

def playlist_download(playlist_url):
    options = {
        'format': 'best',
        'outtmpl': '{0}/%(title)s.%(ext)s'. format(playlist_file_name),
        'ignoreerrors': True,
    }
    with YoutubeDL(options) as yt_dlp:
        yt_dlp.download([playlist_url])
        messagebox(playlist_file_name + " "+ downloaded_successfully)

def audio_download(audio_url):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': '{0}/%(title)s.%(ext)s'. format(music_file_name),
    }
    with YoutubeDL(options) as yt_dlp:
        yt_dlp.download([audio_url])
        messagebox(music_file_name + " "+ downloaded_successfully)

def video_search(search_video):
    options = {
        'format': 'best',
        'nonplaylists': True,
        'quiet': False,
    }
    with YoutubeDL(options) as yt_dlp:
        search = f"ytsearch10:{search_video}"
        for i, video in enumerate(yt_dlp.extract_info(search, download=False), start=1):
            print(f"{i}. {video['title']} ({video['webpage_url']})")
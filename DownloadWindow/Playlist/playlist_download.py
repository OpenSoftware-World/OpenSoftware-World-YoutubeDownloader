#!/usr/bin/python3
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

from AppFunction.appfunction import *

def close(event=None):
    window.destroy()

def GetPlaylistUrl(event=None):
     playlist_download(str(playlist_url_entry.get()))

def Playlist_downloader(event=None):
    global window, playlist_url_entry
    window = customtkinter.CTk()
    pywinstyles.apply_style(window, pywinstyles_theme)
    window.geometry("500x100")
    window.title(option_three)
    window.iconbitmap("Icon/lxlm_yt_downloader.ico")
    video_download_title = customtkinter.CTkLabel(master=window, text=option_three, font=(userFont, userTitleFontSize, userFontBold))
    video_download_title.place(x=10, y=10)
    playlist_url_entry = customtkinter.CTkEntry(master=window, placeholder_text=playlist_url_txt, width=300)
    playlist_url_entry.place(x=10, y=50)
    video_download_btn = customtkinter.CTkButton(master=window, text=download_txt, font=(userFont, userFontSize, userFontBold), command=GetPlaylistUrl, corner_radius=userCornerRadiusValue, fg_color=userButtonColor, hover_color=userButtonHoverColor, text_color=userButtonTextColor, border_color=userButtonBorderColor, border_width=userButtonBorderWidth)
    video_download_btn.place(x=320, y=50)

    window.bind(window_close_shortcut, close)
    window.bind(downloader_shortcut, GetPlaylistUrl)
    
    window.mainloop()
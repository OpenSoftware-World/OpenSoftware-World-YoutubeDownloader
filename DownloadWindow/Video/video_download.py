#!/usr/bin/python3
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

from AppFunction.appfunction import *

def close(event=None):
    window.destroy()

def GetVideoUrl(event=None):
    get_url = str(video_url_entry.get())
    video_download(get_url)

def Video_downloader(event=None):
    global window, video_url_entry
    window = customtkinter.CTk()
    pywinstyles.apply_style(window, pywinstyles_theme)
    window.geometry("500x100")
    window.title(option_one)
    window.iconbitmap("Icon/lxlm_yt_downloader.ico")
    video_download_title = customtkinter.CTkLabel(master=window, text=option_one, font=(userFont, userTitleFontSize, userFontBold))
    video_download_title.place(x=10, y=10)
    video_url_entry = customtkinter.CTkEntry(master=window, placeholder_text=video_url_txt, width=300)
    video_url_entry.place(x=10, y=50)
    video_download_btn = customtkinter.CTkButton(master=window, text=download_txt, font=(userFont, userFontSize, userFontBold), command=GetVideoUrl, corner_radius=userCornerRadiusValue, fg_color=userButtonColor, hover_color=userButtonHoverColor, text_color=userButtonTextColor, border_color=userButtonBorderColor, border_width=userButtonBorderWidth)
    video_download_btn.place(x=320, y=50)
    
    window.bind(window_close_shortcut, close)
    window.bind(downloader_shortcut, GetVideoUrl)

    window.mainloop()
#!/usr/bin/python3
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

from AppFunction.appfunction import *

def close(event=None):
    window.destroy()

def GetSearchKeyword(event=None):
    get_search = video_search_keyword_entry.get()
    video_search(get_search)

def Video_Search(event=None):
    global window, video_search_keyword_entry
    window = customtkinter.CTk()
    pywinstyles.apply_style(window, pywinstyles_theme)
    window.geometry("500x100")
    window.title(option_four)
    window.iconbitmap("Icon/lxlm_yt_downloader.ico")
    video_search_title = customtkinter.CTkLabel(master=window, text=option_four, font=(userFont, userTitleFontSize, userFontBold))
    video_search_title.place(x=10, y=10)
    video_search_keyword_entry = customtkinter.CTkEntry(master=window, placeholder_text=video_search_txt, width=320)
    video_search_keyword_entry.place(x=10, y=50)
    video_search_btn = customtkinter.CTkButton(master=window, text=search_txt, font=(userFont, userFontSize, userFontBold), command=GetSearchKeyword, corner_radius=userCornerRadiusValue, fg_color=userButtonColor, hover_color=userButtonHoverColor, text_color=userButtonTextColor, border_color=userButtonBorderColor, border_width=userButtonBorderWidth)
    video_search_btn.place(x=340, y=50)

    window.bind(window_close_shortcut, close)
    window.bind(video_search_shortcut, GetSearchKeyword)
    
    window.mainloop()
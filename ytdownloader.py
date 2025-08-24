#!/usr/bin/python3
""" Copyright© 2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader"""

from DownloadWindow.Video.video_download import *
from DownloadWindow.Music.music_download import *
from DownloadWindow.Playlist.playlist_download import *
from VideoSearch.video_search import *
import pystray, threading
from PIL import Image, ImageTk, ImageDraw
import webbrowser

def hide_window():
    window.withdraw()

def tray():
    image = Image.open("Icon/lxlm_yt_downloader.png")
    tray_img = ImageDraw.Draw(image)
    tray_img.text((10, 25), "A", fill=(255,255,255))

    def on_exit(icon, item):
        icon.stop()
        window.quit()

    def on_show(icon, item):
        window.deiconify()
    
    windows = pystray.Menu(
        pystray.MenuItem(option_one, Video_downloader),
        pystray.MenuItem(option_two, Music_downloader),
        pystray.MenuItem(option_three, Playlist_downloader),
        pystray.MenuItem(option_four, Video_Search)
    )

    about = pystray.Menu(
        pystray.MenuItem(github_repo_txt, lambda: webbrowser.open("https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-YoutubeDownloader")),
        pystray.MenuItem(my_github_acc_txt, lambda: webbrowser.open("https://github.com/LinuxUsersLinuxMint")),
        pystray.MenuItem("Web Site", lambda: webbrowser.open("https://linuxuserslinuxmint.github.io/")),
        pystray.MenuItem(documents_txt, lambda: webbrowser.open("https://linuxuserslinuxmint.github.io/Documents/documents"))
    )

    menu = pystray.Menu(
        pystray.MenuItem(about_txt, about),
        pystray.MenuItem(windows_not_os_txt, windows),
        pystray.MenuItem(open_txt, on_show),
        pystray.MenuItem(close_txt, on_exit)
    )

    icon = pystray.Icon("LinuxUsersLinuxMint-YTDownloader", image, "LinuxUsersLinuxMint-YTDownloader", menu)
    icon.run()

def close(event=None):
    window.destroy()

window = customtkinter.CTk()
window.geometry("730x160")
window.title("LinuxUsersLinuxMint YTDownloader")
window.iconbitmap("Icon/lxlm_yt_downloader.ico")
lxlm_yt_downloader_title = customtkinter.CTkLabel(master=window, text="LinuxUsersLinuxMint YTDownloader", font=(userFont, userTitleFontSize, userFontBold), text_color=userWindowTitleColor)
lxlm_yt_downloader_title.place(x=10, y=50)
img = Image.open("Icon/lxlm_yt_downloader.png")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)
lxlm_yt_downloader_icon = customtkinter.CTkLabel(master=window, text="", image=img)
lxlm_yt_downloader_icon.place(x=560, y=15)
video_download_btn = customtkinter.CTkButton(master=window, text=option_one, font=(userFont, userFontSize, userFontBold), command=Video_downloader, corner_radius=userCornerRadiusValue, fg_color=userButtonColor, hover_color=userButtonHoverColor, text_color=userButtonTextColor, border_color=userButtonBorderColor, border_width=userButtonBorderWidth)
video_download_btn.place(x=10, y=100)
music_download_btn = customtkinter.CTkButton(master=window, text=option_two, font=(userFont, userFontSize, userFontBold), command=Music_downloader, corner_radius=userCornerRadiusValue, fg_color=userButtonColor, hover_color=userButtonHoverColor, text_color=userButtonTextColor, border_color=userButtonBorderColor, border_width=userButtonBorderWidth)
music_download_btn.place(x=160, y=100)
playlist_download_btn = customtkinter.CTkButton(master=window, text=option_three, font=(userFont, userFontSize, userFontBold), command=Playlist_downloader, corner_radius=userCornerRadiusValue, fg_color=userButtonColor, hover_color=userButtonHoverColor, text_color=userButtonTextColor, border_color=userButtonBorderColor, border_width=userButtonBorderWidth)
playlist_download_btn.place(x=310, y=100)
video_search_btn = customtkinter.CTkButton(master=window, text=option_four, font=(userFont, userFontSize, userFontBold), command=Video_Search, corner_radius=userCornerRadiusValue, fg_color=userButtonColor, hover_color=userButtonHoverColor, text_color=userButtonTextColor, border_color=userButtonBorderColor, border_width=userButtonBorderWidth)
video_search_btn.place(x=480, y=100)
if lang == "en":
    video_search_btn.place(x=465, y=100)

window.bind(window_close_shortcut, close)
window.bind(video_downloader_shortcut, Video_downloader)
window.bind(music_downloader_shortcut, Music_downloader)
window.bind(playlist_downloader_shortcut, Playlist_downloader)
window.bind(video_search_shortcut, Video_Search)

pywinstyles.apply_style(window, pywinstyles_theme)
customtkinter.set_appearance_mode(userTheme)

if tray_visible == True:
    window.protocol("WM_DELETE_WINDOW", hide_window)
    threading.Thread(target=tray, daemon=True).start()

window.mainloop()
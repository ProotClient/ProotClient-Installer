# Developing this installer is more pain than actually making stuff for the client

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

import os, json, sys, shutil
from tkinter import *
import os

path = ""

window = Tk(); window.geometry("420x210"); window.title("ProotClient Installer")
window_icon = PhotoImage(file="ui_icon.png"); window.iconphoto(True, window_icon); window.resizable(False, False)
icon = PhotoImage(file="icon.png"); title_icon = Label(window, image=icon); title_icon.place(x=16, y=16)
title = Label(window, text="ProotClient Installer", font=("Calibry", 18, "bold")); title.place(x=64, y=16)
text1 = Label(window, text="Enter the path of your Minecraft directory:"); text1.place(x=64, y=48)
text2 = Entry(window, width=56); text2.pack(padx=10); text2.place(x=64, y=72); text2.insert(10, "C:\\Users\\" + os.environ.get('USERNAME') + "\\AppData\\Roaming\\.minecraft\\")
def button_continue():
    global path
    path = text2.get().replace("/", "\\")
    if not (path.endswith("\\")): path+="\\"
    window.destroy()
text3 = Label(window, text="Select what version you want to install:"); text3.place(x=64, y=104)
version = StringVar(window)
version.set("1.19.3") # default value
text4 = OptionMenu(window, version, "1.19.3", "1.19.4", "1.20"); text4.place(x=64, y=128)
continue_button = Button(window, text="Continue", command=button_continue); continue_button.place(x=13, y=176)
window.mainloop()

origin = os.getcwd() + "\\origin\\"
target = path

versions_path = "versions\\"
name = "ProotClient\\"

files = os.listdir(origin)

os.mkdir(
    target + versions_path + name,
    0o666
)
for file_name in files:
    shutil.copy(
        origin + file_name,
        target + versions_path + name + file_name
    )

window = Tk(); window.geometry("420x210"); window.title("ProotClient Installer")
window_icon = PhotoImage(file="ui_icon.png"); window.iconphoto(True, window_icon); window.resizable(False, False)
icon = PhotoImage(file="icon.png"); title_icon = Label(window, image=icon); title_icon.place(x=16, y=16)
title = Label(window, text="ProotClient Installer", font=("Calibry", 18, "bold")); title.place(x=64, y=16)
text1 = Label(window, text="ProotClient has been successfully installed. You can close"); text1.place(x=64, y=48)
text2 = Label(window, text="this window now."); text2.place(x=64, y=64)
def button_continue():
    window.destroy()
continue_button = Button(window, text="Close", command=button_continue); continue_button.place(x=13, y=176)
window.mainloop()

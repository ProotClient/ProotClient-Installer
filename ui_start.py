from tkinter import *
import os

start = Tk(); start.geometry("420x210"); start.title("ProotClient Installer")
start_icon = PhotoImage(file="ui_icon.png"); start.iconphoto(True, start_icon); start.resizable(False, False)
icon = PhotoImage(file="icon.png"); title_icon = Label(start, image=icon); title_icon.place(x=16, y=16)
title = Label(start, text="ProotClient Installer", font=("Calibry", 18, "bold")); title.place(x=64, y=16)
text1 = Label(start, text="Enter the path of your Minecraft directory:"); text1.place(x=64, y=48)
text2 = Entry(start, width=56); text2.pack(padx=10); text2.place(x=64, y=72); text2.insert(10, "C:\\Users\\" + os.environ.get('USERNAME') + "\\AppData\\Roaming\\.minecraft\\")
def button_continue():
    path = text2.get().replace("/", "\\")
    if not (path.endswith("\\")): path+="\\"
    print(path)
continue_button = Button(start, text="Continue", command=button_continue); continue_button.place(x=13, y=176)
start.mainloop()
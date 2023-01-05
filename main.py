import os, json, sys, shutil
from tkinter import *
import ui_start

origin = os.getcwd() + "\\origin\\"
target = "C:\\Users\\Patrick\\Programs\\! AmongUs\\.minecraft\\"

versions_path = "versions\\"
name = "ProotClient\\"

"""
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
"""
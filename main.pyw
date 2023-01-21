# TODO: Replace the origin folder with a system that gets a .zip file from Internet, unzip it and copy the files into the folder where it should be installed to. 
#       Add a Launcher Profile when it is done installing.


# Import needed Librarys
import os, shutil, base64, random, json, requests, subprocess
from tkinter import *
from zipfile import ZipFile



# Predefine Variables
pressed_continue = False
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
random_number = ""
path = ""

# Base64 Images for Temporary Directory
image_icon = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALcSURBVFhH7dZJqI1hHMfxYx7jimQeuzKmEIqFUFIkhYW6C4oICxTC1oKFSJGNDYpCpqUyLShDEWVcmEJS5nn6fl/nqdfpvOc857rnbvjVJ95zz3me532G//vm/vk0y//7t2mOXrC9j37QmBmCA/iJW+iORkkbrMUbeNcHcQPzUfUMxWl413Y6HsbZWPT7v9XLNDyBnTuIHghpgmFwdqqS2XDK7fwoOqEwbkQHEpXoL5IpsNP22IcleI9iaY0+6Ac3ZTc4Ux3gAN9iLy4iOq7vVmxDWz8okq5Yj6v4BGdKn+Fgv+SvH2EiojIKdRiBrBlriQW4j9Cpd3kCC9EXzspG3IObOCp2/gw26OgvYQXSaz8ZZxE6thaswQA0Rcgg3MGM5CoiPXEd3+HGC9On25gDMwuP8Q2b0BGFcd1P4TysmmXjyI/A6RoJN5BnfTMewkHY4U64HyzDHs+sTIW/cZmishKvMDa5+jNdsBs/YKNOv2tcKqvhd+clV2UyHC9gmc2KM7QYDjIsyQRkZQv83rrkqkyOwWMUU82coWuwcR9ILVAs++F3nImSmY6vcGPFpje8e4+oR60d0o/5ubBzZ3WwH2TFH53JSzcQE6vednhq7uI4wnFzKR3AquSqRNzFld69GYMHsJPXsG64QT0lVkWLlCepFUrmEFx7fxAbp/wC7HwHrPsey1AbrCEWqrLpD0e/PLmKzyTY+TkU3qFn3r/tSq4yEkqlG8VK5yxUEjegceZ84KRzBQ7Aipr51A0D8PjUwBpQSXyqGZ8ZhTMwGnYcXl5KpjM8zx6VqDUj7pUG2wPGnWqd9zm+DMWOonfkS4YV7TJs3N+lT8FThFPg47ei2Jhn2cb2oBbj4B7ZgJOwE/8uz7vLOBDOQLoOzES94nP8OezgA6wNoUO9w2FYaArfjIpVwnrFd3w7c2f7LnAT1vOl8G4zd3WlyWrIdba8+lrlxnyJ8I73Pw2YXO4Xi4q1LgolSTUAAAAASUVORK5CYII="
image_ui_icon = b"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAHbSURBVDjLpZM/a1RBFEfPnfciq4uChLgrWChaihBYbAxqBD+AgrGwVBDRxipgH1AMEQJpbawU9SvYCRaiEmOaBUkRDRYBwf3zZt691+K9DWuXxYELwzCce37MXHF3/mfJtYcv789d7jzZ7XvTHTDDzVBT3Bxzw1Uxd1wVNePIgdTb3NxefLuysJZ3LnRWpxrN0GpM1LjZ6+sqsJb3k4f+7p+J1QfJA0Du6izdOjMx4M7jLSqAGwCxVBxwc9TAcMwcNUNLr8qNqM6p9mHUtAJQv4IEQdzxILg4YkIIgkhARJHMySyQl9V9K2vAiBQAFwGBzMEEzJzMIUhGLqDiaKiMTa2OYPU/EAH3f0Ai4OqYgAsQhMyyCjCKMNpUDKk2YyDLhcV3t0mxJMZEGiZe3HyDWWUQypT2DEYAkbp9Ha0YJi6dnGf+9BUG/QKAMpV1hDpLBvhYlHGjYlBQlAVREw1psPlzA68N8pEKgNQ16r78folvP9aZOXiMYRmJGpk52uLB87ukvAXcIN/+vvXq3rO0YKqYGqqKmaEpYX6WeGKDQ9MFRRoSNbLza4fe7ymOl9dfA8h+pvHq8sUv7en2uRgT3W7388en67N71vsd5/OPZj+kYUqfVr7OjZ//BRjUGmnYsJxdAAAAAElFTkSuQmCC"

# Create Temporary Directory
for i in range(0,16):
    random_number += random.choice(numbers)
temp_directory = "ProotClient-Installer-TemporaryFiles_" + str(random_number)
os.mkdir(temp_directory, 0o666)
subprocess.check_call(["attrib","+H",temp_directory])

# Add the Base64 Images to the Temporary Directory
image_icon_file = open(temp_directory + "\\icon.png", "wb")
image_icon_file.write(base64.decodebytes(image_icon))
image_icon_file.close()
image_ui_icon_file = open(temp_directory + "\\ui_icon.png", "wb")
image_ui_icon_file.write(base64.decodebytes(image_ui_icon))
image_ui_icon_file.close()

# Download versions.json from the ✨internet✨ and add to the Temporary Directory
versions_file_download = requests.get("https://prootclient.github.io/installer/versions.json")
open(temp_directory + "\\versions.json", "wb").write(versions_file_download.content)

versions_file = open(temp_directory + "\\versions.json", "r")
versions = json.loads(versions_file.read())
versions_file.close()



# Tkinter Randomness
window = Tk(); window.geometry("420x210"); window.title("ProotClient Installer")
window_icon = PhotoImage(file=temp_directory + "\\ui_icon.png"); window.iconphoto(True, window_icon); window.resizable(False, False)
icon = PhotoImage(file=temp_directory + "\\icon.png"); title_icon = Label(window, image=icon); title_icon.place(x=16, y=16)
title = Label(window, text="ProotClient Installer", font=("Calibry", 18, "bold")); title.place(x=64, y=16)
text1 = Label(window, text="Enter the path of your Minecraft directory:"); text1.place(x=64, y=48)
text2 = Entry(window, width=56); text2.pack(padx=10); text2.place(x=64, y=72); text2.insert(10, "C:\\Users\\" + os.environ.get('USERNAME') + "\\AppData\\Roaming\\.minecraft\\")
def button_continue():
    global path, pressed_continue
    path = text2.get().replace("/", "\\")
    if not (path.endswith("\\")): path+="\\"
    pressed_continue = True
    window.destroy()
text3 = Label(window, text="Select what version you want to install:"); text3.place(x=64, y=104)
version = StringVar(window)
version.set(versions[0]["version"])
versions_dropdown = []
for version_dictionary in versions:
    versions_dropdown.append(version_dictionary["version"])
text4 = OptionMenu(window, version, *versions_dropdown); text4.place(x=64, y=128)
text5 = Checkbutton(window, text = "Add a Launcher Profile for ProotClient"); text5.place(x=176, y=176)
continue_button = Button(window, text="Continue", command=button_continue); continue_button.place(x=13, y=176)
window.mainloop()

if (pressed_continue):

    for version_dictionary in versions:

        if (version_dictionary["version"] == version.get()):
            
            zip_to_download = requests.get(version_dictionary["link"])
            open(temp_directory + "\\" + version_dictionary["version"] + "-ProotClient.zip", "wb").write(zip_to_download.content)
            zip = temp_directory + "\\" + version_dictionary["version"] + "-ProotClient.zip"

    target = path
    versions_path = "versions\\"
    name = version.get() + "-" + "ProotClient\\"

    # Create the Directory where the files are installed to
    os.mkdir(target + versions_path + name, 0o666)

    with ZipFile(zip, "r") as zObject:
    
        zObject.extractall(path=target + versions_path + name)

    # Tkinter Randomness
    window = Tk(); window.geometry("420x210"); window.title("ProotClient Installer")
    window_icon = PhotoImage(file=temp_directory + "\\ui_icon.png"); window.iconphoto(True, window_icon); window.resizable(False, False)
    icon = PhotoImage(file=temp_directory + "\\icon.png"); title_icon = Label(window, image=icon); title_icon.place(x=16, y=16)
    title = Label(window, text="ProotClient Installer", font=("Calibry", 18, "bold")); title.place(x=64, y=16)
    text1 = Label(window, text="ProotClient has been successfully installed. You can close"); text1.place(x=64, y=48)
    text2 = Label(window, text="this window now."); text2.place(x=64, y=64)
    def button_continue():
        window.destroy()
    continue_button = Button(window, text="Close", command=button_continue); continue_button.place(x=13, y=176)
    window.mainloop()

shutil.rmtree(temp_directory)
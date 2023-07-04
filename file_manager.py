import os
import filetype as ft
from exif_editor import ExifEditor


folder_path: str = ""
keys: dict = {}

def keyword_frequency(folderpath: str = "") -> dict:
    for file in os.listdir(folder_path if folder_path != "" else os.getcwd()):
        if os.path.isfile(file) and ft.image_match(file) != None:
            img = ExifEditor(file)
            print(img.keywords)
            for keyword in img.keywords:                
                if keyword in keys:
                    keys[keyword] += 1
                else:
                    keys[keyword] = 1
            img.close_image()
    return keys


print(keyword_frequency())
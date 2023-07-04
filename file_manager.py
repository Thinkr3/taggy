import os
from exif_editor import ExifEditor


folder_path: str = ""
keys: dict = {}

def keyword_frequency(folderpath: str = "") -> dict:
    for file in os.listdir(folder_path if folder_path != "" else os.getcwd()):
        if os.path.isfile(file) and img.verify_image():
            img = ExifEditor(file)
            for keyword in img.keywords:
                if keyword in keys:
                    keys[keyword] += 1
                else:
                    keys[keyword] = 1
            img.close_image()
    return keys


print(keyword_frequency())
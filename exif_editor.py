from PIL import Image
from PIL.ExifTags import TAGS

# Windows Keyword Exif Code: 40094
# Windows Title Exif Code: 40091 / 270
# TAGS.get(int) -> returns the name of the exif code

class ExifEditor:
    '''Class that edits the exif data of an image'''

    def __init__(self, path: str) -> None:
        self.src = path
        self.img = Image.open(path)
        self.img_exif = self.img.getexif()

    @property
    def title(self) -> str:
        '''Returns the image title exif'''
        return self.img_exif[270].decode("utf-16")

    def set_title(self, title: str) -> None:
        '''Takes a title and sets it as the image title exif'''
        self.img_exif[270] = title.encode("utf-16")

    def clear_title(self) -> None:
        '''Clears the image title exif'''
        self.img_exif[270] = "".encode("utf-16")

    @property
    def keywords(self) -> list:
        '''Returns the image keywords exif'''
        if self.img_exif.get(40094) == None:
            return []
        return [decoded.replace("\ufeff", "") for decoded in self.img_exif[40094].decode("utf-16").split("; ")]

    def set_keywords(self, keywords: list) -> None:
        '''Takes a list of keywords and sets them as the image keyword exif'''
        self.img_exif[40094] = "".encode("utf-16")
        for keyword in keywords:
            self.add_keyword(keyword)

    def clear_keywords(self) -> None:
        '''Clears all keywords from the image keyword exif'''
        self.img_exif[40094] = "".encode("utf-16")

    def remove_keyword(self, keyword: str) -> None:
        '''Takes a keyword and removes it from the image keyword exif'''
        if self.img_exif.get(40094) == None:
            return
        if keyword.__contains__(";"):
            keyword = keyword.replace(";", "")
        self.img_exif[40094] = self.img_exif[40094].replace(keyword.encode("utf-16"), "".encode("utf-16")).removesuffix("; ".encode("utf-16"))

    def add_keyword(self, keyword: str) -> None:
        '''Takes a keyword and adds it to the image keyword exif'''

        # If there is no keyword exif, create one
        if self.img_exif.get(40094) == None or self.img_exif.get(40094) == "".encode("utf-16"):
            self.img_exif[40094] = "".encode("utf-16") + keyword.encode("utf-16")
            return
        
        # If the keyword is already in the exif, don't add it
        if self.img_exif[40094].__contains__(keyword.encode("utf-16")):
            return
        
        # If the keyword contains a semicolon, remove it (Windows doesn't like semicolons)
        if keyword.__contains__(";"):
            keyword = keyword.replace(";", "")

        # If the keyword is not in the exif, add it
        self.img_exif[40094] += "; ".encode("utf-16") + keyword.encode("utf-16")

    def get_exif_data(self) -> dict:
        '''Returns the exif data of the image'''
        return {key: value.decode("utf-16") if type(value) == bytes else value for key, value in self.img_exif.items()}

    def print_exif_data(self) -> None:
        '''Takes an image exif and prints out all the exif data of the image'''
        for img_data in self.img_exif.items():
            if type(img_data[1]) == bytes:
                print(img_data[0], img_data[1].decode("utf-16"))
            else:
                print(img_data[0], img_data[1])

    def save_image(self) -> None:
        '''Saves the image with the new exif data'''
        self.img.save(self.src, exif=self.img_exif)

# def open_image(path: str) -> Image: # FIXME: This function is not used
#     '''Takes a path to an image and returns the image'''
#     src = path
#     img = Image.open(src)
#     img_exif = img.getexif()
#     return img

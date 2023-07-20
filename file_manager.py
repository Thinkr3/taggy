import os
import shutil
import filetype as ft
from exif_editor import ExifEditor


# folder_path: str = ""

def keyword_frequency(folderpath: str = os.getcwd()) -> dict:
    '''Returns a dictionary of keywords and their frequency in the folderpath'''
    keys: dict = {}
    for file in os.listdir(folderpath):
        if os.path.isfile(file) and ft.image_match(file) != None:
            img = ExifEditor(file)
            for keyword in img.keywords:                
                if keyword in keys:
                    keys[keyword] += 1
                else:
                    keys[keyword] = 1
            img.close_image()
    
    # Sorts the dictionary by most popular keyword
    keys = dict(sorted(keys.items(), key=lambda x: x[1], reverse=True))
    return keys

def repeat_all_sort(folderpath: str = os.getcwd(), threshold: int = 0, hardlinks: bool = True) -> None:
    '''
    Sorts the images in the folderpath by their keywords. 
    Image is sorted into every keyword.
    '''
    keys = keyword_frequency(folderpath)
    for file in os.listdir(folderpath):
        if os.path.isfile(file) and ft.image_match(file) != None:
            img = ExifEditor(file)
            img.close_image() # Prevents System Error 32 and memory leaks

            # Filters out keywords that don't meet the threshold
            for keyword in filter(lambda x: keys[x] >= threshold, img.keywords):
                if not os.path.exists(keyword):
                    os.mkdir(keyword)
                if hardlinks:
                    os.link(file, keyword + "/" + file)
                else:
                    shutil.copy(file, keyword + "/" + file)

def most_popular_sort(folderpath: str = os.getcwd(), threshold: int = 0, hardlinks: bool = True, *exclude: str) -> None:
    '''
    Sorts the images in the folderpath by their most popular keywords. 
    Only sorts the image into most popular keyword.
    '''
    keys = keyword_frequency(folderpath)
    for file in os.listdir(folderpath):
        if os.path.isfile(file) and ft.image_match(file) != None:
            img = ExifEditor(file)
            img.close_image() # Prevents System Error 32 and memory leaks
            
            # Filters out keywords that don't meet the threshold
            reduced_keywords = list(filter(lambda keyword: keys[keyword] >= threshold and keyword not in exclude, img.keywords))

            # If there are no keywords that meet the threshold, skip the file
            if len(reduced_keywords) == 0:
                continue
            
            # Finds the most popular keyword
            keyword = max(reduced_keywords, key=lambda x: keys[x])
            
            if not os.path.exists(keyword):
                os.mkdir(keyword)
            if hardlinks:
                os.link(file, keyword + "/" + file)
            else:
                shutil.copy(file, keyword + "/" + file)

def unique_sort(folderpath: str = os.getcwd(), threshold: int = 0, hardlinks: bool = True) -> None:
    '''
    Sorts the images in the folderpath by their least popular keywords. 
    Only sorts the image into least popular keyword.
    '''
    keys = keyword_frequency(folderpath)
    for file in os.listdir(folderpath):
        if os.path.isfile(file) and ft.image_match(file) != None:
            img = ExifEditor(file)
            img.close_image() # Prevents System Error 32 and memory leaks
            
            # Filters out keywords that don't meet the threshold
            reduced_keywords = list(filter(lambda x: keys[x] >= threshold, img.keywords))

            # If there are no keywords that meet the threshold, skip the file
            if len(reduced_keywords) == 0:
                continue
            
            # Finds the most popular keyword
            keyword = min(reduced_keywords, key=lambda x: keys[x])
            
            if not os.path.exists(keyword):
                os.mkdir(keyword)
            if hardlinks:
                os.link(file, keyword + "/" + file)
            else:
                shutil.copy(file, keyword + "/" + file)

def populate_dirs(folderpath: str = os.getcwd()) -> None:
    keys = keyword_frequency(folderpath)
    for key in keys:
        if not os.path.exists(key):
            os.mkdir(key)

unique_sort(threshold=1)
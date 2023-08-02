import tensorflow as tf
from tensorflow import keras

from exif_editor import ExifEditor

import deepdanbooru as dd

# Load the model
target_path = "images/forest.jpg"
project_path = "deepdanbooru_model"
model = "deepbooru/resnet_custom_v3.h5"
tags_path = "deepbooru/tags.txt"
threshold = 0.6
allow_gpu = True
compile_model = False
allow_folder = True
save_txt = True
folder_filters = ""
verbose = True


# Evaluate the image
image = dd.commands.evaluate([target_path], project_path, model, tags_path, threshold, allow_gpu, compile_model, allow_folder, save_txt, folder_filters, verbose)

img = ExifEditor(target_path)

img.set_keywords(image)

img.keywords

img.save_image()
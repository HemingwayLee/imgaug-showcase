import os
from PIL import Image
import numpy as np
import imgaug.augmenters as iaa

# set path to image folder
path = './images/'

# define augmentations
seq = iaa.Sequential([
    iaa.Resize({"height": 224, "width": 224}),
    iaa.Fliplr(0.5),
    iaa.GaussianBlur(sigma=(0, 1.0)),
    iaa.Sometimes(0.5, iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05), per_channel=0.5)),
])

# loop through images in folder
for filename in os.listdir(path):
    if filename.endswith('.png'):  # only apply to image files
        # load image with Pillow library
        img = Image.open(os.path.join(path, filename))
        # convert image to numpy array
        img_array = np.array(img)
        # apply augmentations
        aug_img = seq(image=img_array)
        # convert back to Pillow image and save
        aug_img = Image.fromarray(aug_img)
        aug_img.save(os.path.join(path, 'aug_'+filename))


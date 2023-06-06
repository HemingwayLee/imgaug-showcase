import os
from PIL import Image
import numpy as np
import imgaug.augmenters as iaa

path = './images/'

seq = iaa.Sequential([
    iaa.Resize({"height": 224, "width": 224}),
    iaa.Fliplr(0.5),
    iaa.GaussianBlur(sigma=(0, 1.0)),
    iaa.Sometimes(0.5, iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05), per_channel=0.5)),
])

for filename in os.listdir(path):
    if filename.endswith('.png'):  
        img = Image.open(os.path.join(path, filename))
        
        img_array = np.array(img)
        aug_img = seq(image=img_array)
        
        aug_img = Image.fromarray(aug_img)
        aug_img.save(os.path.join(path, 'aug_'+filename))

import os
from PIL import Image
import numpy as np
import imgaug.augmenters as iaa
from pathlib import Path

mySometimes05 = lambda aug: iaa.Sometimes(0.5, aug)
mySometimes09 = lambda aug: iaa.Sometimes(0.9, aug)

seq = iaa.Sequential([
    iaa.Resize({"height": 224, "width": 224}),
    mySometimes09(iaa.Fliplr(0.5)),
    mySometimes05(iaa.GaussianBlur(sigma=(0, 1.0))),
    mySometimes05(iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05), per_channel=0.5)),
])


ori_path = './images/'
filename = 'ranking.png'

tar_path = './results/'
Path(tar_path).mkdir(parents=True, exist_ok=True)

for i in range(5):    
    img = Image.open(os.path.join(ori_path, filename))
        
    img_array = np.array(img)
    aug_img = seq(image=img_array)
    
    aug_img = Image.fromarray(aug_img)
    aug_img.save(os.path.join(tar_path, f'aug_{i}_'+filename))

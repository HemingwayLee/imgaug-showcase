import os
from PIL import Image
import numpy as np
import imgaug.augmenters as iaa
import imgaug as ia
from pathlib import Path

ori_path = './images/'
filename = 'ranking.png'
img = Image.open(os.path.join(ori_path, filename))
width, height = img.size

mySometimes10 = lambda aug: iaa.Sometimes(1.0, aug)
resizeAndPad = iaa.Sequential([
    mySometimes10(
        iaa.Resize({"height": (0.5, 0.9), "width": (0.5, 0.9)})
    ),
    iaa.PadToFixedSize(
        width=width, 
        height=height, 
        position="center",
        pad_mode="edge"
    )
])

tar_path = './results/'
Path(tar_path).mkdir(parents=True, exist_ok=True)

for i in range(5):    
    img_array = np.array(img)
    aug_img = resizeAndPad(image=img_array)
    
    aug_img = Image.fromarray(aug_img)
    aug_img.save(os.path.join(tar_path, f'scale_{i}_'+filename))

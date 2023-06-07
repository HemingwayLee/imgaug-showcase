import os
from PIL import Image
import numpy as np
import imgaug.augmenters as iaa
from pathlib import Path

mySometimes10 = lambda aug: iaa.Sometimes(1.0, aug)

seq = iaa.Sequential([
    mySometimes10(
        # iaa.Resize((0.5, 0.5))
        iaa.Resize({"height": (0.1, 0.9), "width": (0.1, 0.9)})
    ),
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
    aug_img.save(os.path.join(tar_path, f'scale_{i}_'+filename))

#!/usr/bin/env python3
import os
from PIL import Image
src="supplier-data/images/"
img_files=[f for f in os.listdir(src) if f.endswith(".tiff")]
for img_file in img_files:
    img=Image.open(src+img_file)
    img=img.resize((600,400))

    if img.mode != 'RGB':
        img=img.convert('RGB')
    f, ext = os.path.splitext(img_file)
    f += ".jpeg"
    img.save(src+f,'JPEG')
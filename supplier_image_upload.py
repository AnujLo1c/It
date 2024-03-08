#!/usr/bin/env python3
import os
import requests
img_src="supplier-data/images/"
img_files=[f for f in os.listdir(img_src) if f.endswith('.jpeg')]
for img_file in img_files:
    with open(img_src+img_file,'rb') as img:
       requests.post("http://34.16.141.136/upload/",files={'file':img})
#! /usr/bin/env python3
import os
import requests

src="supplier-data/descriptions/"
des_files=os.listdir(src)
data={}
for file in des_files:
    with open(src+file,'rb') as des:
        data["name"]=des.readline()
        data["weight"]=int(des.readline().split()[0])
        data["description"]=des.read()
        data['image_name']=file.split('.')[0]+'.jpeg'
    response=requests.post("http://34.16.141.136/fruits/",data=data)
    if response.ok:
        print("uploaded data")
    else:
        print(f"error: {response.status_code}")
        print(response.raise_for_status)
    data.clear()
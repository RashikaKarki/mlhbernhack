import cv2
import numpy as np
import sys
import base64
import json


with open('myjsonfile.json') as f:
  data = json.load(f)

# data = str(data)
data = data['image']
# print(data)
img_data = base64.b64decode(data)
# print(img_data)

with open("tmp.jpg", "wb") as fh:
    # res = base64.decodebytes(img_data)
    fh.write(base64.decodebytes(img_data))

# img = cv2.imread('tmp.jpg');
# print(img.shape)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print(gray.shape)
# edges = cv2.Canny(gray,30,120)
# img = cv2.resize(edges,(32,32))
# print(edges.shape)



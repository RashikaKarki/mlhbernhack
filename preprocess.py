import numpy as np
import cv2
import sys
import json
import os
import tensorflow as tf

labels = {
    0: 'ka',
    1 : 'kha',
    2 : 'none'
}

model = tf.keras.models.load_model('model_5.h5');
data = sys.argv[1]
# with open('temp.jpg','wb') as f:
#     f.write(data)

img = cv2.imread(sys.argv[1]);
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,30,120)
cv2.imshow("widnow",edges)
img = cv2.resize(edges,(64,64))
img = np.array(img).astype('float32')
img = np.reshape(img,(1,64,64,3))


#Send image to predict


result = model.predict(img)
result = np.argmax(result)

letter = labels[result]
print(letter)

#Send letter to server
import numpy as np
import cv2
import sys
import json
import os
import tensorflow as tf
import base64
import json

# labels = [f for f in os.listdir('processed_data')]
labels = ['none','character_01_ka','character_02_kha']


# with open('myjsonfile.json') as f:
#   data = json.load(f)

# # data = str(data)
# data = data['image']

# # print(data)


# with open("tmp.jpg", "wb") as fh:
#     fh.write(base64.decodebytes(data.encode()))


model = tf.keras.models.load_model('model_5.h5');
print(model.summary())
img = cv2.imread('tmp.jpg');
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,30,120)
# cv2.imshow("widnow",edges)
img = cv2.resize(edges,(64,64))
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img = np.array(img).astype('float32')
img = np.reshape(img,(1,64,64,3))




# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edge = cv2.Canny(gray,30,120)
# cv2.imshow("Windwo",edge)
# img = np.reshape(edge,(1,32,32,1)).astype('float32')

#Send image to predict
# cv2.waitKey(0)
# cv2.destroyAllWindows()

result = model.predict(img)
result = np.argmax(result)

letter = labels[result]
results = json.dumps({"result":letter})
print(results)
sys.stdout.flush()

#Send letter to server
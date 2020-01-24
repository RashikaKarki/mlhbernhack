import cv2
import numpy as np
import sys
img = cv2.imread(sys.argv[1]);
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)
edges = cv2.Canny(gray,30,120)
img = cv2.resize(edges,(32,32))
print(edges.shape)
print(img.shape)
cv2.imshow("widnow",edges)

# img = np.array(img).astype('float32')
# img = np.reshape(img,(1,32,32,3))
cv2.waitKey(0)
cv2.destroyAllWindows()
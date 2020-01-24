import cv2
import numpy as np
import os


folders = ['data/none', 'data/ka','data/kha']
new_folders = ['processed_data/none','processed_data/ka','processed_data/kha']
for i,folder in enumerate(folders):
    for f in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,f))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,30,250)

        if(not os.path.exists(new_folders[i])):
            os.mkdir(new_folders[i])
        cv2.imwrite(os.path.join(new_folders[i],f),edges)
        print(f,"Saved");
# f = os.listdir(folders[1])[0]
# img = cv2.imread(os.path.join(folders[1],f))
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,30,250)
# cv2.imshow("widnow",edges)
# # if(not os.path.exists(new_folders[i])):
#     # os.mkdir(new_folders[i])
# # cv2.imwrite(os.path.join(new_folders[i],f),gray)
# # print(f,"Saved")

# cv2.waitKey(0)
# cv2.destroyAllWindows()
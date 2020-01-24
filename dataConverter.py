import cv2
import numpy as np
import os


folders = ['data/'+folder for folder in os.listdir('data')]

new_folders = ['processed_data/'+folder for folder in os.listdir('data')]
for i,folder in enumerate(folders):
    for f in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,f))
        # print(img.shape)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = np.resize(img,(64,64))
        edges = cv2.Canny(gray,30,120)

        if(not os.path.exists(new_folders[i])):
            os.mkdir(new_folders[i])
        cv2.imwrite(os.path.join(new_folders[i],f),edges)
        print(f,"Saved")

# f = "C:\\Users\\Dell\\Desktop\\mlhbernhack\\test.jpg"
# img = cv2.imread(os.path.join(f))
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,10,250)
# cv2.imshow("widnow",edges)
# cv2.imwrite('test_edge.jpg',edges)
# # if(not os.path.exists(new_folders[i])):
#     # os.mkdir(new_folders[i])
# # cv2.imwrite(os.path.join(new_folders[i],f),gray)
# # print(f,"Saved")

# cv2.waitKey(0)
# cv2.destroyAllWindows()
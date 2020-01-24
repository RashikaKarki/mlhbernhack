import cv2
import numpy as np
import os


folders = ['data/none', 'data/ka','data/kha']
new_folders = ['processed_data/none','processed_data/ka','processed_data/kha']
for i,folder in enumerate(folders):
    # for f in os.listdir(folder):
    #     img = cv2.imread(os.path.join(folder,f))
    #     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #     if(not os.path.exists(new_folders[i])):
    #         os.mkdir(new_folders[i])
    #     cv2.imwrite(os.path.join(new_folders[i],f),gray)
    #     print(f,"Saved");
    pass
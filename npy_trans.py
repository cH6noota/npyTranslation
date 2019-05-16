from tqdm import tqdm
from PIL import Image
import glob
import numpy as np
from keras.preprocessing.image import load_img,img_to_array
import time
IMG_SIZE=32
#True=Grayscale, False=RGB
COLOR=False
#Name to load images Folder
DIR_NAME='./Images'
#Name to save
SAVE_FILE_NAME='SaveImages'
#sahpe File Name
if COLOR:
    SAVE_FILE_NAME=SAVE_FILE_NAME+'_'+str(IMG_SIZE)+'Gray'
else:
    SAVE_FILE_NAME=SAVE_FILE_NAME+'_'+str(IMG_SIZE)+'RGB'


#load images and image to array
img_list = glob.glob('/Users/moritachikara/Desktop/hand/*')
#load madomagi images and reshape
temp_img_array_list=[]
for img in tqdm(img_list):
    temp_img=load_img(img,grayscale=COLOR,target_size=(32,32))
    temp_img_array=img_to_array(temp_img)
    temp_img_array_list.append(temp_img_array)


temp_img_array_list=np.array(temp_img_array_list)

#save np.array
np.save(str(len(img_list) )+'X.npy',temp_img_array_list)



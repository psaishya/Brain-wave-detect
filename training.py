import cv2
import os
from PIL import Image
import numpy as np

image_folder="datasets/"

no_tumorimages=os.listdir(image_folder+"no_tumor/")
# print(no_tumorimages)

tumorimages=os.listdir(image_folder+"tumor/")
# print(tumorimages)

dataset=[]
label=[]

image_size=64

for index,filename in enumerate(no_tumorimages):
    # print(index,filename)
    # usiing jpg files only
    if (filename.split('.')[1])=='jpg':
        image=cv2.imread(image_folder+'no_tumor/'+filename)
        image=Image.fromarray(image,'RGB')
        # print(image)
        image=image.resize((image_size,image_size)) # resizing all the images to size 64 x 64
        # print(image)
        dataset.append(np.array(image))
        label.append(0)
        
for index,filename in enumerate(tumorimages):
    # print(index,filename)
    # usiing jpg files only
    if (filename.split('.')[1])=='jpg':
        image=cv2.imread(image_folder+'tumor/'+filename)
        image=Image.fromarray(image,'RGB')
        # print(image)
        image=image.resize((image_size,image_size)) # resizing all the images to size 64 x 64
        # print(image)
        dataset.append(np.array(image))
        label.append(1)
# print(dataset)
# print(label)
print(len(dataset))
print(len(label))




        
        
        


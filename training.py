import cv2
import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras.utils import normalize


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

dataset=np.array(dataset)
label=np.array(label)

x_train,x_test,y_train,y_test=train_test_split(dataset,label,test_size=0.2,random_state=0)#returns shape of x_train,y_train
print(len(x_train),len(y_train),len(x_test),len(y_test)) #checking the number of dataimages splitted as train and test
print(x_train.shape) #gives (no.of images in x_train, image_width, image_height, 3 -channel (rgb))
print(y_train.shape)

#normalization
x_train=normalize(x_train,axis=1)
x_test=normalize(x_test,axis=1)




        
        
        


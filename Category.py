import os
import PIL
import pathlib
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
from tensorflow import keras
from keras.preprocessing import image_dataset_from_directory
from keras.models import Sequential
from keras.layers import RandomFlip,RandomRotation,RandomZoom
from keras.layers import BatchNormalization,Conv2D,MaxPooling2D,Dropout,Flatten,Dense
from keras.models import load_model
from PIL import Image



import warnings
warnings.filterwarnings('ignore')

# We define some parameters for our data and model:

TRAINING_DATA_DIR = 'datasets/'
# TEST_DATA_DIR = 'Testing/'
BATCH_SIZE = 32
IMG_HEIGHT = 64
IMG_WIDTH = 64
EPOCHS=200

data_dir = pathlib.Path(TRAINING_DATA_DIR)
# .with_suffix('')
# test_data_dir = pathlib.Path(TEST_DATA_DIR).with_suffix('')
print(data_dir)
# print(test_data_dir)
print(list(data_dir.glob('*/*.jpg')))
image_count = len(list(data_dir.glob('*/*.jpg')))
print(f'There are {image_count} images in training dataset.')

# print(list(data_dir.glob('*')))

# pituitary = list(data_dir.glob('pituitary_tumor/*'))
# print(pituitary)
# image=PIL.Image.open(str(pituitary[0]))
# print(image)
# image=cv2.imread(str(pituitary[0]))
# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# meningioma = list(data_dir.glob('meningioma_tumor/*'))
# PIL.Image.open(str(meningioma[0]))
# print(str(meningioma[0]))
# image=cv2.imread(str(meningioma[0]))
# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

train_dataset = image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=100,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)
validation_dataset = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=100,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)
class_names = train_dataset.class_names
print(class_names)


class_counts = {}
label_list=[]

for images, labels in train_dataset:
    label_list.extend(labels.numpy())
    for label in labels.numpy():
        nameofclass = class_names[label]
        class_counts[nameofclass] = class_counts.get(nameofclass, 0) + 1
print(label_list)

for class_name, count in class_counts.items():
    print(f"Number of images in class '{class_name}': {count}")

for image_batch, labels_batch in train_dataset:
    print(image_batch)
    print(image_batch.shape)
    print(labels_batch.shape)
    break
    
AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)
    
data_augmentation = Sequential([
    RandomFlip("horizontal", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    RandomRotation(0.1),
    RandomZoom(0.1)
])
model = Sequential([
    data_augmentation,
    BatchNormalization(input_shape=(180, 180, 3)),
    
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2, 2),
    BatchNormalization(),
    
    Dropout(0.25),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    BatchNormalization(),
    
    Dropout(0.25),
    Conv2D(128, (5,5), activation='relu'),
    MaxPooling2D(2,2),
    BatchNormalization(),
    
    Dropout(0.25),
    Flatten(),
    Dense(256, activation='relu', kernel_regularizer='l2'), #kernel_regularizer=keras.regularizers.l2(l=0.1)
    
    BatchNormalization(),
    Dropout(0.25),
    Dense(256, activation='relu', kernel_regularizer='l2'),
    
    BatchNormalization(),
    Dropout(0.25),
    Dense(256, activation='relu', kernel_regularizer='l2'),
    
    BatchNormalization(),
    Dense(4, activation='softmax')
])

early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0.001, patience=10, restore_best_weights=True)
lr_sch = tf.keras.callbacks.ReduceLROnPlateau(monitor = 'val_loss', patience= 8, factor = 0.1, verbose = 1, min_lr = 5e-10)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['sparse_categorical_accuracy'])


model.fit(train_dataset,
          epochs=EPOCHS,
          validation_data=validation_dataset,
          callbacks=[early_stopping, lr_sch],
          shuffle=False)

model.save('Category_classification.h5')

# model3=load_model('Category_classification.h5')


# # new\Training\no_tumor\image(295).jpg

# image1=cv2.imread('Training/pituitary_tumor/p (1).jpg')
# image2=cv2.imread('Training/no_tumor/1.jpg')

# img1=Image.fromarray(image1)
# img1=img1.resize((64, 64))
# img1=np.array(img1)

# img2=Image.fromarray(image2)
# img2=img2.resize((64, 64))
# img2=np.array(img2)

# input_img1=np.expand_dims(img1,axis=0)
# input_img2=np.expand_dims(img2,axis=0)
# print(input_img1)
# print(input_img2)

# result3_1=model3.predict(input_img1)
# result3_2=model3.predict(input_img2)
# score1=tf.nn.softmax(result3_1[0])
# score2=tf.nn.softmax(result3_2[0])
# print(class_names[np.argmax(score1)])
# print(class_names[np.argmax(score2)])

# def classnames_return():
#     return class_names

    


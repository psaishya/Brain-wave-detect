import cv2
import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras.utils import normalize
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import to_categorical


image_folder = "datasets/"

no_tumorimages = os.listdir(image_folder + "no_tumor/")
# print(no_tumorimages)

glioma_tumorimages = os.listdir(image_folder + "glioma_tumor/")
pituitary_tumorimages = os.listdir(image_folder + "pituitary_tumor/")
meningioma_tumorimages = os.listdir(image_folder + "meningioma_tumor/")


# print(tumorimages)

dataset = []
label = []

image_size = 64

for index, filename in enumerate(no_tumorimages):
    # print(index,filename)
    # usiing jpg files only
    if (filename.split(".")[1]) == "jpg":
        image = cv2.imread(image_folder + "no_tumor/" + filename)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(image, "RGB")
        # print(image)
        image = image.resize(
            (image_size, image_size)
        )  # resizing all the images to size 64 x 64
        # print(image)
        dataset.append(np.array(image))
        label.append(0)

for index, filename in enumerate(glioma_tumorimages):
    # print(index,filename)
    # usiing jpg files only
    if (filename.split(".")[1]) == "jpg":
        image = cv2.imread(image_folder + "glioma_tumor/" + filename)
        if image is not None:

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image = Image.fromarray(image, "RGB")
            # print(image)
            image = image.resize(
                (image_size, image_size)
            )  # resizing all the images to size 64 x 64
            # print(image)
            dataset.append(np.array(image))
            label.append(1)
for index, filename in enumerate(pituitary_tumorimages):
    # print(index,filename)
    # usiing jpg files only
    if (filename.split(".")[1]) == "jpg":
        image = cv2.imread(image_folder + "pituitary_tumor/" + filename)
        if image is not None:

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image = Image.fromarray(image, "RGB")
            # print(image)
            image = image.resize(
                (image_size, image_size)
            )  # resizing all the images to size 64 x 64
            # print(image)
            dataset.append(np.array(image))
            label.append(1)
for index, filename in enumerate(meningioma_tumorimages):
    # print(index,filename)
    # usiing jpg files only
    if (filename.split(".")[1]) == "jpg":
        image = cv2.imread(image_folder + "meningioma_tumor/" + filename)
        if image is not None:

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image = Image.fromarray(image, "RGB")
            # print(image)
            image = image.resize(
                (image_size, image_size)
            )  # resizing all the images to size 64 x 64
            # print(image)
            dataset.append(np.array(image))
            label.append(1)
# print(dataset)
# print(label)
print(len(dataset))
print(len(label))

dataset = np.array(dataset)
label = np.array(label)

x_train, x_test, y_train, y_test = train_test_split(
    dataset, label, test_size=0.2, random_state=0
)  # returns shape of x_train,y_train
print(
    len(x_train), len(y_train), len(x_test), len(y_test)
)  # checking the number of dataimages splitted as train and test
print(
    x_train.shape
)  # gives (no.of images in x_train, image_width, image_height, 3 -channel (rgb))
print(y_train.shape)

# normalization
x_train = normalize(x_train, axis=1)
x_test = normalize(x_test, axis=1)

# for categorical cross entropy , modifying y_train and y_test
# y_train = to_categorical(y_train, num_classes=2)
# y_test = to_categorical(y_test, num_classes=2)

# building the model
model = Sequential()

# adding a convolution layer with 32 filters, (3,3) is size of each filter
# here, input_shape=(INPUT_SIZE,INPUT_SIZE,3) specifies that height and width is INPUT_SIZE and 3 color channels(RGB)

model.add(Conv2D(32, (3, 3), input_shape=(image_size, image_size, 3)))
model.add(Activation(("relu")))  # rectified linear unit
model.add(MaxPooling2D(pool_size=(2, 2)))  # reduce by factor of 2

model.add(Conv2D(32, (3, 3), kernel_initializer="he_uniform"))
model.add(Activation(("relu")))  # rectified linear unit
model.add(MaxPooling2D(pool_size=(2, 2)))  # reduce by factor of 2

model.add(Conv2D(64, (3, 3), input_shape=(image_size, image_size, 3)))
model.add(Activation(("relu")))  # rectified linear unit
model.add(MaxPooling2D(pool_size=(2, 2)))  # reduce by factor of 2

model.add(Flatten())  # flatten 3d output into 1d vector

model.add(Dense(64))  # first fully connected layer with 64 neurons
model.add(Activation("relu"))

model.add(Dropout(0.5))  # to avoid overfit

model.add(Dense(1))#another fully connected layer
# model.add(Dense(2))

model.add(Activation('sigmoid')) #for binary classification
# model.add(Activation("softmax"))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# fitting the model by providing datasets
model.fit(
    x_train,
    y_train,
    batch_size=16,
    verbose=1,
    epochs=10,
    validation_data=(x_test, y_test),
    shuffle=False,
)

# saving binary cross entropy model
model.save("Braintumor10epochs_binarycrossentropy.h5")

# saving categorical cross entropy model
# model.save("Braintumor10epochs_categoricalcrossentropy.h5")

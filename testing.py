# testing images

import numpy as np
import cv2
from keras.models import load_model
from PIL import Image

# loading models
model1 = load_model("Braintumor10epochs_binarycrossentropy.h5")
model2 = load_model("Braintumor10epochs_categoricalcrossentropy.h5")

image1 = cv2.imread("pred/pred0.jpg")
image2 = cv2.imread("pred/pred5.jpg")

img1 = Image.fromarray(image1)
img1 = img1.resize((64, 64))
img1 = np.array(img1)

img2 = Image.fromarray(image2)
img2 = img2.resize((64, 64))
img2 = np.array(img2)

input_img1 = np.expand_dims(img1, axis=0)
input_img2 = np.expand_dims(img2, axis=0)

result1_1 = model1.predict(input_img1)
result1_2 = model1.predict(input_img2)

result2_1 = model2.predict(input_img1)
result2_2 = model2.predict(input_img2)

# printing to check predicted model
print(result1_1)
print(result1_2)
print(result2_1)
print(result2_2)
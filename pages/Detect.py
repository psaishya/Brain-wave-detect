import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from keras.models import load_model
# from testing import test_for_tumor  # Assuming your testing function is in a file named testing.py

# Set page title and icon
st.set_page_config(page_title="Brain Tumor Detection", page_icon=":brain:")

# Title and Description
st.title("Brain Tumor Detection App")
st.write("Upload an MRI image to test for the presence of a brain tumor.")

# File Upload
uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg"])

model1 = load_model("Braintumor10epochs_binarycrossentropy.h5")
model2 = load_model("Braintumor10epochs_categoricalcrossentropy.h5")
model3 = load_model("Category_classification.h5")

classnames=['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded MRI Image.", use_column_width=True)

    # Perform Tumor Detection
    if st.button("Detect Tumor"):
        # Convert the uploaded image to a format suitable for testing
        img = Image.open(uploaded_file)
        img = np.array(img.resize((64, 64)))  # Resize image as needed
        img = np.expand_dims(img, axis=0)
        img = np.expand_dims(img, axis=-1)
        # result1 = model1.predict(img)
        # result2 = model2.predict(img)
        result3=model3.predict(img)
        score=tf.nn.softmax(result3[0])
        category=(classnames[np.argmax(score)])
      
        # Call your testing function
        # result = test_for_tumor(img)

        # Display the result
        # if result1 == 1 and result2[0][0] == 0.0:
        #     st.warning("Tumor detected!")
        #     if st.button("Detect the type of Tumor"):
        #         result3=model3.predict(img)
        #         score=tf.nn.softmax(result3[0])
        #         category=(classnames[np.argmax(score)])
        #         st.write(category)
        if category!='no_tumor':
            st.warning("Tumor detected!")
            st.write(category)

        else:
            st.success("No tumor detected.")
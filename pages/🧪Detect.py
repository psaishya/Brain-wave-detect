import streamlit as st
import requests
from PIL import Image
import numpy as np
from keras.models import load_model

# Set page title and icon
st.set_page_config(page_title="Brain Tumor Detection", page_icon=":brain:")

# Define CSS styles
page_bg = """
<style>
body {
    background-image: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
    background-size: cover;
    height: 100vh;
    margin: 0;
    font-family: Arial, sans-serif;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

title_style = """
<style>
h1 {
    color: white;
    text-align: center;
    transition: color 0.5s ease-in-out; 
}
h1:hover {
    color: #ff5733; 
}

</style>
"""


st.markdown(title_style, unsafe_allow_html=True)

# Title and Description with title icon
title_container = st.container()
with title_container:
    st.markdown('<div class="title-container"><h1>🧠 Brain Tumor Detection App</h1></div>', unsafe_allow_html=True)
st.write("Upload an MRI image to test for the presence of a brain tumor.")

# File Upload
uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg"])

model1 = load_model("Braintumor10epochs_binarycrossentropy.h5")
model2 = load_model("Braintumor10epochs_categoricalcrossentropy.h5")

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
        result1 = model1.predict(img)
        result2 = model2.predict(img)
      
        # Display the result
        if result1 == 1 and result2[0][0] == 0.0:
            st.warning("Tumor detected!")
        else:
            st.success("No tumor detected!")

import streamlit as st
import requests
import time
import json
from PIL import Image
import numpy as np
import tensorflow as tf
from keras.models import load_model
# from testing import test_for_tumor  # Assuming your testing function is in a file named testing.py

# Set page title and icon
st.set_page_config(page_title="Brain Tumor Detection", page_icon=":brain:")
# Title and Description
st.title(":brain: Brain Tumor Detection App ")
st.subheader("Upload an MRI scan to begin analysis :mag:")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
# loading assets
lottie_animation = load_lottiefile("animation3.json")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        # Define CSS styles
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
        # with title_container:
        #     st.markdown('<div class="title-container"><h1>🧠 Brain Tumor Detection App</h1></div>', unsafe_allow_html=True)
        # st.write("Upload an MRI image to test for the presence of a brain tumor.")

        # File Upload
        uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg"])

        model1 = load_model("Braintumor10epochs_binarycrossentropy.h5")
        model2 = load_model("Braintumor10epochs_categoricalcrossentropy.h5")
        model3 = load_model("Category_classification1.h5")

        classnames=['Glioma tumor', 'Meningioma tumor', 'No tumor', 'Pituitary tumor']

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
                bar=st.progress(0)
                # result1 = model1.predict(img)
                # result2 = model2.predict(img)
                result3=model3.predict(img)
                score=tf.nn.softmax(result3[0])
                category=(classnames[np.argmax(score)])

            
                # Display the result
                if category!='No tumor':
                    for i in range(10):
                    #loading bar
                        bar.progress((i+1)*10)
                    st.warning("Tumor detected!")
                    # st.write(category)
                    if(category=='Meningioma tumor'):
                        st.write("Meningioma tumor[ See more about it](http://localhost:8501/Meningioma)")

                    elif(category=='Pituitary tumor'):
                        st.write("Pituitary tumor[ See more about it](http://localhost:8501/Pituitary-adenoma)")
                    
                    elif (category=='Glioma tumor'):
                        st.write("Glioma tumor[ See more about it](http://localhost:8501/Glioma)")

                    
                else:
                    for i in range(10):
                        bar.progress((i+1)*10)
                    st.success("No tumor detected!")


with right_column:
    st.lottie(
        lottie_animation,
        speed=1.5,
        reverse=False,
        loop=True,
        quality="high",
        height=None,
        width=None,
        key=None,
    )

# File Upload
###################################33

    #
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
        
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Brain Wave", page_icon=":tada: ", layout="wide")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# ---------- loading assets ---------
lottie_animation = load_lottiefile("animation1.json")
# ---------header section----------
# selected = option_menu(
#     menu_title=None,
#     options=["Home", "About Us", "Contact"],
#     icons=["house", "book", "envelope"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
# )
with st.container():
    st.subheader("Welcome to Brain Wave Detect :brain:")
    st.title("Empowering Early Diagnosis, Improving Lives")
    st.write("Brain tumors are abnormal growths of cells in the brain. They can be benign (non-cancerous) or malignant (cancerous), and they can affect anyone, regardless of age or gender. ")

    st.write("[Learn More>](https://www.mayoclinic.org/diseases-conditions/brain-tumor/symptoms-causes/syc-20350084)")


# ------body of the program--------
with st.container():
    st.write("------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How does this work?")
        st.write("###")
        st.write(
            """
          -Our app leverages artificial intelligence and deep learning to analyze MRI images of the brain and detect potential tumors.
        \nTechnologies:
          \n-We use TensorFlow and OpenCV, leading technologies in AI and image processing, to power the analysis."""
        )

        st.header("Features:")
        st.write("""
        -Upload your MRI images and let the app identify potential tumors.
   \n Tumor Type Classification:
       Dsiscover the type of brain tumor detected, aiding in early diagnosis and treatment planning."""
                 )
    with right_column:
        st.lottie(
            lottie_animation,
            speed=1,
            reverse=True,
            loop=True,
            quality="high",
            height=None,
            width=None,
            key=None,
        )
import streamlit as st
from streamlit_lottie import st_lottie
import json
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Brain Wave", page_icon=":brain:", layout="wide")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# ---------- loading assets ---------
lottie_animation = load_lottiefile("animation1.json")

with st.container():
    st.subheader("Welcome to Brain Wave Detect :brain:")
    st.title("Empowering Early Diagnosis, Improving Lives")
    st.write(
        "Brain tumors are abnormal growths of cells in the brain. They can be benign (non-cancerous) or malignant (cancerous), and they can affect anyone, regardless of age or gender. "
    )

    st.write(
        "[Learn More>](https://www.mayoclinic.org/diseases-conditions/brain-tumor/symptoms-causes/syc-20350084)"
    )


# ------body of the program--------
with st.container():
    st.write("------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How does this work?")
        st.write("###")
        st.write(
            """
          - Our app leverages artificial intelligence and deep learning to analyze MRI images of the brain and detect potential tumors.
        \nTechnologies:
          \n- We use TensorFlow and OpenCV, leading technologies in AI and image processing, to power the analysis."""
        )

        st.header("Features:")
<<<<<<< HEAD
        st.write(
            """
        -Upload your MRI images and let the app identify potential tumors.
=======
        st.write("""
        - Upload your MRI images and let the app identify potential tumors.
>>>>>>> 104b997e347b9cbd91591720dabcf24d75bca32c
   \n Tumor Type Classification:
       Discover the type of brain tumor detected, aiding in early diagnosis and treatment planning."""
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
<<<<<<< HEAD
=======
with st.container():
    st.write("---")
    footer = """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #f8f9fa;
                text-align: center;
                padding: 10px;
            }
        </style>
        <div class="footer">
            <p>Follow Brain-Wave Detect for awesome brain health tips: &nbsp;&nbsp;&nbsp; 
            <img src="https://i.ibb.co/GkTspCK/twitter.png" alt="twitter" width=32 height=32>&nbsp; &nbsp;            
            <img src="https://i.ibb.co/BTv56bd/facebook.png" alt="facebook" width=32 height=32>
            </p>
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
>>>>>>> 104b997e347b9cbd91591720dabcf24d75bca32c

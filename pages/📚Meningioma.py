import streamlit as st
from streamlit_lottie import st_lottie
import json
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Meningioma", page_icon=":brain:", layout="wide")


# ---------define animation resource for animation json file---------

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# ---------Loading asset---------
lottie_animation = load_lottiefile("animation2.json")

# -----defining resource for css----------


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")

with st.container():
    st.title("Meningioma :brain:")
    st.title("")


# --------body of the program---------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
        - Most common kind of primary brain tumor \n
        - More than 30% of all brain tumor cases are meningiomas \n
        - 85% of meningiomas are non cancerous, slow growing tumors \n
        - almost all meningiomas can be considered benign but some meningiomas can be persistent and come back after treatment \n

""")
        st.subheader("Recommendation:")
        st.write("""
                 
                 - Surgery
                 - Radiation Therapy
                 """)

        st.write(
            ":point_right:[What to expect on surgery?](https://www.youtube.com/watch?v=7H6vLuELqeQ)")
        st.write(
            ":point_right:[More about Meningioma](https://www.cancer.gov/rare-brain-spine-tumor/tumors/meningioma)")
        with right_column:
            st.lottie(lottie_animation,
                      speed=1.5,
                      reverse=False,
                      loop=True,
                      quality="high",
                      height=None,
                      width=None,
                      key=None,
                      )

import streamlit as st
from streamlit_lottie import st_lottie
import json
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Contact", page_icon=":phone: ", layout="wide")


# ---------defining resoursce for animation json file-------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# ---------- loading assets ---------
lottie_animation = load_lottiefile("animation5.json")

# ---------defining resoursce for css-------


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


with st.container():
    st.subheader("Brain Wave Detect :brain:")
    st.title("Empowering Early Diagnosis, Improving Lives")


# ------body of the program--------
with st.container():
    st.write("------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Contact Us :envelope:")
        st.write("###")
        contact_info = """
            <form action="https://formsubmit.co/shubhashishkarki@gmail.com" method="POST">
            <input type ="hidden" name ="_captcha" value = "false">
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name = "message"  placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
     
    
</form> 


"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_info, unsafe_allow_html=True)
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

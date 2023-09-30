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
    st.subheader("Glioma :brain:")
    st.title("")


# --------body of the program---------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
                  What is a Glioma?\n
                - Glioma is a common type of brain tumor arising from glial cells that support neurons in the brain.\n
                - Represents about 33% of all brain tumors and grows within the brain substance.\n
""")
        st.title("Types of Gliomas: \n")
        st.write("""
                - Astrocytomas: Most common glioma, originating from astrocytes; high-grade astrocytomas are highly malignant.\n
                - Brain Stem Gliomas: Rare tumors in the brain stem, difficult to remove surgically, often in children.\n
                - Ependymomas: Develop from ependymal cells, rare but common in children, affecting cerebellum.\n
                - Oligodendrogliomas: Arise from oligodendrocytes, affecting cerebrum, relatively better prognosis.\n
                - Optic Pathway Gliomas: Low-grade tumors in optic nerves or chiasm, often in people with neurofibromatosis.\n
                 """)

        st.title("Symptoms of Gliomas:")
        st.write("""
                - Headaches, seizures, personality changes, weakness, numbness, speech problems. \n
                - Additional symptoms: Nausea, vomiting, vision loss, dizziness; symptoms may appear slowly. \n
                 """)
        st.title("Risk Factors of Gliomas:")
        st.write("""
                - No known specific cause; can occur in people of all ages, more common in adults.\n
                - Slightly higher occurrence in men and Caucasian individuals.\n
                 """)
        st.title("Glioma Diagnosis and Treatment:")
        st.write("""
                - Diagnosis involves medical history, physical and neurological exams, brain scans, and biopsy.\n
                - Treatment customized based on tumor grade, including surgery, radiation therapy, chemotherapy, or observation.\n
                - Surgery is often the first line, followed by adjuvant treatments like radiation and chemotherapy.\n
                - Monitoring post-treatment with brain scans to check for tumor growth and recurrence; further surgeries may be recommended.\n
                 """)
    st.write(
        "[What to expect on surgery? :right:](https://www.youtube.com/watch?v=7H6vLuELqeQ)")
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

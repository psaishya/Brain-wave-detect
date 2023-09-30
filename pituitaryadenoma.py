import streamlit as st
from streamlit_lottie import st_lottie
import json
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Pituitary Adenoma",
                   page_icon=":brain:", layout="wide")

# Define animation resource for animation json file


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# Load lottie animation
lottie_animation = load_lottiefile("animation2.json")

# Define CSS styling


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")

# Header and basic information
with st.container():
    st.subheader("Pituitary Adenoma :brain:")
    st.write(
        """
        - A pituitary adenoma is a benign (noncancerous) growth on your pituitary gland.
        - Unlike cancer, it doesn’t spread to other parts of your body.
        - As pituitary adenomas grow, they can put pressure on nearby structures and cause symptoms.
        """
    )

# Description of the Pituitary Gland
with st.container():
    st.write("---")
    st.title("The Pituitary Gland:")
    st.write(
        """
        - Your pituitary is a small gland about the size of a pea that’s joined to your hypothalamus (the base of your brain) right behind your nose.
        - It has two lobes: the anterior (front) lobe and the posterior (back) lobe.
        - Each lobe releases different hormones.
        """
    )

# Hormones released by the Pituitary Gland
with st.container():
    st.write("---")
    st.title("Hormones Released by the Pituitary Gland:")
    st.write(
        """
        - Adrenocorticotropic hormone (ACTH or corticotropin).
        - Antidiuretic hormone (ADH, or vasopressin).
        - Follicle-stimulating hormone (FSH).
        - Growth hormone (GH).
        - Luteinizing hormone (LH).
        - Oxytocin.
        - Prolactin.
        - Thyroid-stimulating hormone (TSH).
        """
    )

# Categories of Pituitary Adenomas
with st.container():
    st.write("---")
    st.title("Categories of Pituitary Adenomas:")
    st.write(
        """
        - Functioning (secreting) adenomas: These adenomas release extra pituitary hormones, which cause certain symptoms and/or conditions depending on the hormone it releases.
        - Nonfunctioning (non-secreting) adenomas: These adenomas don’t release hormones, but they can compress nearby structures if they grow.
        """
    )

# Size Categories of Pituitary Adenomas
with st.container():
    st.write("---")
    st.title("Size Categories of Pituitary Adenomas:")
    st.write(
        """
        - Microadenomas: These adenomas are smaller than 10 millimeters or 1 centimeter.
        - Macroadenomas: These adenomas are larger than 10 millimeters.
        """
    )

# Who Pituitary Adenomas Affect
with st.container():
    st.write("---")
    st.title("Who Pituitary Adenomas Affect:")
    st.write(
        """
        - Pituitary adenomas can occur at any age but are more common in people in their 30s or 40s.
        - Women and people assigned female at birth (AFAB) are more likely to have pituitary adenomas than men and people assigned male at birth (AMAB).
        """
    )

# Commonality of Pituitary Adenomas
with st.container():
    st.write("---")
    st.title("Commonality of Pituitary Adenomas:")
    st.write(
        """
        - Pituitary adenomas make up 10% to 15% of all tumors that develop within your skull.
        - About 77 out of 100,000 people have a pituitary adenoma, but researchers think adenomas actually occur in as many as 20% of people at some point in their lives.
        """
    )

# Symptoms of Pituitary Adenomas
with st.container():
    st.write("---")
    st.title("Symptoms of Pituitary Adenomas:")
    st.write(
        """
        - Vision problems (40% to 60% of people with pituitary macroadenoma).
        - Headaches.
        - Hormonal deficiency leading to various symptoms based on the affected hormone.
        """
    )

# Causes of Pituitary Adenomas
with st.container():
    st.write("---")
    st.title("Causes of Pituitary Adenomas:")
    st.write(
        """
        - Scientists aren’t sure of the exact cause of pituitary adenomas.
        - Some adenomas have been linked to accidental changes or mutations in DNA.
        - Pituitary adenomas are also associated with certain genetic conditions.
        """
    )
# Diagnosis and Tests for Pituitary Adenomas
with st.container():
    st.write("---")
    st.title("Diagnosis and Tests for Pituitary Adenomas:")
    st.write(
        """
        - Diagnostic process depends on the type of adenoma and whether it's causing symptoms or not.
        - Blood tests: To check certain hormone levels based on symptoms.
        - Imaging tests: MRI or CT scan of the head to provide images of the structures inside the head.
        - Eye exam: Visual field test to check eye function, especially if experiencing vision problems.
        """
    )

# Treatment Options for Pituitary Adenomas
with st.container():
    st.write("---")
    st.title("Treatment Options for Pituitary Adenomas:")
    st.write(
        """
        - Treatment usually involves surgery, medicine, radiation, or a combination of these therapies.
        - Surgery: To remove all or part of the adenoma, usually through transsphenoidal surgery (through the nose and sinus).
        - Medication: Dopamine agonists (e.g., cabergoline) for prolactinomas; shrink adenoma and relieve symptoms.
        - Radiation Therapy: Stereotactic radiosurgery using high-energy X-rays to shrink adenomas.
        """
    )

# Side Effects of Pituitary Adenoma Treatment
with st.container():
    st.write("---")
    st.title("Side Effects of Pituitary Adenoma Treatment:")
    st.write(
        """
        - Surgery: Possible complications include bleeding, cerebrospinal fluid (CSF) leaks, meningitis, and diabetes insipidus.
        - Medication: Common side effects of dopamine agonists include headaches, nausea, vomiting, dizziness, and increased compulsive behavior.
        - Radiation Therapy: Possible side effects include pituitary hormonal deficiency, impaired fertility, vision loss, brain injury, and tumor development several years after treatment (rare).
        """
    )

# Closing Note and Additional Resources
with st.container():
    st.write("---")
    st.write(
        "[More about Pituitary Adenoma :arrow_right:](https://www.ncbi.nlm.nih.gov/books/NBK554451/")

with st.container():
    st.lottie(lottie_animation,
              speed=1.5,
              reverse=False,
              loop=True,
              quality="high",
              height=None,
              width=None,
              key=None,
              )

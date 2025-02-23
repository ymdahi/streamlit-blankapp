import streamlit as st
from streamlit_extras.app_logo import add_logo



LOGO_URL_LARGE = "media/uwlogo.png"
st.logo(
    LOGO_URL_LARGE,
)



st.title("GenAI Lab")
st.write(
    "## Welcome"
)

st.write(
    "Welcome to GenAI Lab, your gateway to an of AI tools designed to simplify common tasks and processes for designing educational materials."
)
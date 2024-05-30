import pandas as pd
import streamlit as st
from PIL import Image
import os


@st.cache_data(ttl=3600)
def load_data(path="data/Instructional_Design_Models_v3.xlsx"):
    try:
        data = pd.read_excel(path)
        data.fillna("No available data", inplace=True)
        return data
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on failure

    from PIL import Image


@st.cache_data(ttl=3600)
def find_and_load_image(image_name, directory="data/images"):
    extensions = ["png", "jpg", "gif", "JPG"]

    for ext in extensions:
        image_path = os.path.join(directory, f"{image_name}.{ext}")
        if os.path.exists(image_path):
            try:
                # Open and return the image without closing the file stream
                img = Image.open(image_path)
                return img
            except Exception as e:
                st.error(f"Error loading image: {e}")
                return None

    st.error("Image not found.")
    return None


def display_image(image):
    """Displays the PIL image directly in Streamlit."""
    if image:
        st.image(image, caption="Design (Scheme and source)")
    else:
        st.error("Failed to load and display the image.")


@st.cache_data(ttl=3600)
def add_logo():
    st.markdown(
        f"""
            <style>
                [data-testid="stSidebar"] {{
                    background-image: url(https://www.thevillageproject.eu/wp-content/uploads/2023/05/cropped-village-logo_web-300x128.png);
                    background-repeat: no-repeat;
                    padding-top: 80px;
                    background-position: 20px 20px;
                }}
            </style>
            """,
        unsafe_allow_html=True,
    )

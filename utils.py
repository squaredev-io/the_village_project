import pandas as pd
import streamlit as st

def load_data(path = "data/Instructional_Design_Models.xlsx"):
    try:
        data = pd.read_excel(path)
        data.fillna('No available data', inplace=True)
        return data
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on failure
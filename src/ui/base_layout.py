import streamlit as st

def style_base_layout():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f5f5f5;
            color: #333333;
            font-family: Arial, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )   


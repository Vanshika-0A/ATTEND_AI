import streamlit as st
import base64

def header_home():

    st.markdown("""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{}"
             width="250">
        <h1 style="
            color:#E0E3FF;
            margin-top:10px;
            font-size:70px;
            font-weight:bold;">
            ATTEND<br>AI
        </h1>
    </div>
    """.format(get_base64("logo.png")),
    unsafe_allow_html=True)


def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
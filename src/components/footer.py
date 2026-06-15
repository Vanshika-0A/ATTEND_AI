import streamlit as st
import base64

def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def footer_home():
    img_base64 = get_image_base64("footer.png")
    st.markdown(
        f"""
        <style>
            .fixed-footer {{
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                z-index: 9999;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 12px 0 10px 0;
                background: transparent;
                pointer-events: none;
            }}
            .fixed-footer img {{
                width: 250px;
                border-radius: 20px;
                pointer-events: auto;
            }}
            .main .block-container {{
                padding-bottom: 100px;
            }}
        </style>
        <div class="fixed-footer">
            <img src="data:image/png;base64,{img_base64}" alt="Crafted with love by Vanshika Teotia" />
        </div>
        """,
        unsafe_allow_html=True,
    )
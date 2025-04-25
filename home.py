# File: home.py
import streamlit as st

# st.set_page_config(
#     page_title="Dividend Trend Predictor",
#     page_icon="📈",
#     layout="wide"
# )

# Set page config
# Set page configuration
st.set_page_config(page_title="Home", layout="wide")

# Inject custom CSS for dark background image
st.markdown(
    """
    <style>
    .stApp {
        # background-image: url('https://images.unsplash.com/photo-1508780709619-79562169bc64');
        background-image: url('https://www.google.com/search?q=divident+prediction+&sca_esv=19f8f2d2dec41c53&rlz=1C5CHFA_enIN994IN994&udm=2&biw=1384&bih=693&sxsrf=AHTn8zrHWRUL2mczlsT6Gk22IR_MXWBpyg%3A1745584328437&ei=yIALaPm7Gsm9ptQPqbzLkQs&ved=0ahUKEwj5v8mumPOMAxXJnokEHSneMrIQ4dUDCBE&oq=divident+prediction+&gs_lp=EgNpbWciFGRpdmlkZW50IHByZWRpY3Rpb24gSI5vUL8PWPlLcAJ4AJABAJgBTaABrAiqAQIxNrgBDMgBAPgBAZgCDaACvQaoAgrCAgoQABiABBhDGIoFwgIGEAAYBxgewgIKECMYJxjJAhjqAsICDhAAGIAEGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAgUQABiABMICCBAAGIAEGLEDwgINEAAYgAQYsQMYQxiKBcICChAAGIAEGLEDGArCAg0QABiABBixAxiDARgKwgIHEAAYgAQYCpgDBYgGAZIHAjEzoAebR7IHAjExuAeyBg&sclient=img#imgrc=U0xQQxIsWmRKRM&imgdii=BznL36nPCiNuCM');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Optional: make main content darker for better readability */
    .main {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 10px;
    }

    /* Optional: style titles */
    h1 {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Dividend Trend Predictor")

st.markdown("""

<span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

<br>

Team Members:
- Akshara Ramprasad MSDS'25Samritha Aadhi Ravikumar MSDS'25
- Akshara Ramprasad MSDS'25
- Crystal Leatvanich MSBA'25
""", unsafe_allow_html=True)


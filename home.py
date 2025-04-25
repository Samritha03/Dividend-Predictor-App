# File: home.py
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Inject custom CSS for dark background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1508780709619-79562169bc64');
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
- Samritha Aadhi Ravikumar MSDS'25
- Akshara Ramprasad MSDS'25
- Crystal Leatvanich MSBA'25
""", unsafe_allow_html=True)


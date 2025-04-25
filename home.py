# File: home.py
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
/* App-wide background image */
.stApp {
    background-image: url('https://images.unsplash.com/photo-1508780709619-79562169bc64');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Make all text inside white */
h1, h2, h3, p, li, span {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# --- Main Content ---
with st.container():
    st.markdown("<div class='main-block'>", unsafe_allow_html=True)

    st.title("📊 Dividend Trend Predictor")

    st.markdown("""
    <span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

    <br><br>

    Team Members:
    - Samritha Aadhi Ravikumar MSDS'25
    - Akshara Ramprasad MSDS'25
    - Crystal Leatvanich MSBA'25
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

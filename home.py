# File: home.py
import streamlit as st

# --- Set page configuration ---
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# --- Background image CSS (Finance Theme) ---
page_bg_img = '''
<style>
.stApp {
    background-image: url('https://images.unsplash.com/photo-1605902711622-cfb43c44367f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Render main content ---
st.title("📊 Dividend Trend Predictor")

st.markdown("""
<span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

<br>

Team Members:
- Samritha Aadhi Ravikumar MSDS'25
- Akshara Ramprasad MSDS'25
- Crystal Leatvanich MSBA'25
""", unsafe_allow_html=True)

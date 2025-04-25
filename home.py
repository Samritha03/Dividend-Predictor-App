# File: home.py
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# --- Background image CSS ---
page_bg_img = '''
<style>
.stApp {
    background-image: url('https://www.pristinemarketinsights.com/assets/images/banking-and-finance-bg.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

# st.markdown(page_bg_img, unsafe_allow_html=True)

# # --- Render content ---
# st.title("📊 Dividend Trend Predictor")

# st.markdown("""
# <span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

# <br>

# Team Members:
# - Samritha Aadhi Ravikumar MSDS'25
# - Akshara Ramprasad MSDS'25
# - Crystal Leatvanich MSBA'25
# """, unsafe_allow_html=True)



st.markdown("""
<div style='background-color: rgba(0,0,0,0.6); padding: 2rem; border-radius: 5px;'>

<h1 style='color: white;'>📊 Dividend Trend Predictor</h1>

<p style='font-size: 24px; font-weight: bold; color: white;'>BA870 Financial Analytics - Final Project</p>

<br>

<p style='font-size: 18px; font-weight: bold; color: white;'>Team Members:</p>
<ul style='font-size: 18px; font-weight: bold; color: white;'>
    <li>Samritha Aadhi Ravikumar MSDS'25</li>
    <li>Akshara Ramprasad MSDS'25</li>
    <li>Crystal Leatvanich MSBA'25</li>
</ul>

</div>
""", unsafe_allow_html=True)


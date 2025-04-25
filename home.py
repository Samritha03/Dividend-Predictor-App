# # File: home.py
# import streamlit as st

# # Set page configuration
# st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# # --- Background image CSS ---
# page_bg_img = '''
# <style>
# .stApp {
#     background-image: url('https://www.pristinemarketinsights.com/assets/images/banking-and-finance-bg.jpg');
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }
# </style>
# '''

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

#################
# # File: home.py
# import streamlit as st

# # Set page configuration
# st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# # --- Background image CSS ---
# page_bg_img = '''
# <style>
# .stApp {
#     background-image: url('https://www.pristinemarketinsights.com/assets/images/banking-and-finance-bg.jpg');
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }
# </style>
# '''
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # --- Render content ---
# st.title("📊 Dividend Trend Predictor")

# st.markdown("""
# <span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

# <br><br>

# <span style='font-size: 18px; font-weight: bold;'>Team Members:</span><br>
# <ul style='font-size: 18px; font-weight: bold;'>
#   <li>Samritha Aadhi Ravikumar MSDS'25</li>
#   <li>Akshara Ramprasad MSDS'25</li>
#   <li>Crystal Leatvanich MSBA'25</li>
# </ul>
# """, unsafe_allow_html=True)


#############
# File: home.py
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# --- Background image and box CSS ---
page_bg_img = '''
<style>
.stApp {
    background-image: url('https://www.pristinemarketinsights.com/assets/images/banking-and-finance-bg.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Transparent left-aligned box */
.transparent-box {
    background-color: rgba(0, 0, 0, 0.1);
    padding: 1.5rem 2rem;
    border-radius: 10px;
    width: 60%;
    margin: 0.5rem 0 1rem 0.5rem;
}

.transparent-box h1 {
    color: white;
    font-size: 36px;
}
.transparent-box h2 {
    color: white;
    font-size: 24px;
}
.transparent-box ul {
    list-style-type: none;
    padding-left: 1rem;
}
.transparent-box li {
    color: white;
    font-size: 18px;
    margin-bottom: 0.5rem;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Render content ---
st.markdown("""
<div class="transparent-box">
    <h1>📊 Dividend Trend Predictor</h1>
    <h2>BA870 Financial Analytics - Final Project</h2>
    <br>
    <h5>Team Members:</h5>
    <ul>
        <li>- Samritha Aadhi Ravikumar MSDS'25</li>
        <li>- Akshara Ramprasad MSDS'25</li>
        <li>- Crystal Leatvanich MSBA'25</li>
    </ul>
</div>
""", unsafe_allow_html=True)



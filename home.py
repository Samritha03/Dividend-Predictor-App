# # File: home.py
# import streamlit as st

# # --- Set page configuration ---
# st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# # --- Background image CSS (Finance Theme) ---
# page_bg_img = '''
# <style>
# .stApp {
#     background-image: url('https://images.unsplash.com/photo-1605902711622-cfb43c44367f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80');
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }
# </style>
# '''
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # --- Render main content ---
# st.title("📊 Dividend Trend Predictor")

# st.markdown("""
# <span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

# <br>

# Team Members:
# - Samritha Aadhi Ravikumar MSDS'25
# - Akshara Ramprasad MSDS'25
# - Crystal Leatvanich MSBA'25
# """, unsafe_allow_html=True)

# File: home.py
import streamlit as st

# Page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# CSS for background + translucent blur block
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1508780709619-79562169bc64');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Blur + transparency for main container */
    .main-block {
        background: rgba(0, 0, 0, 0.6); /* semi-transparent black */
        backdrop-filter: blur(6px);     /* actual blur */
        -webkit-backdrop-filter: blur(6px);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem;
    }

    h1, h2, h3, p, li, span {
        color: white !important;
    }

    /* Optional: Remove top search tab */
    [data-testid="stToolbar"] {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# Render content
with st.container():
    st.markdown("<div class='main-block'>", unsafe_allow_html=True)

    st.title("📊 Dividend Trend Predictor")

    st.markdown("""
    <span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

    <br>

    Team Members:
    - Samritha Aadhi Ravikumar MSDS'25
    - Akshara Ramprasad MSDS'25
    - Crystal Leatvanich MSBA'25
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


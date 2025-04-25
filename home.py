# # File: home.py
# import streamlit as st

# # Set page configuration
# st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# # --- Background image CSS ---
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('https://images.unsplash.com/photo-1508780709619-79562169bc64');
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }
# </style>
# '''
# st.markdown(page_bg_img, unsafe_allow_html=True)
# )

# # # Responsive background + text color based on system theme
# # st.markdown("""
# # <style>
# # /* Background styling */
# # .stApp {
# #     background-size: cover;
# #     background-position: center;
# #     background-repeat: no-repeat;
# #     background-attachment: fixed;
# # }

# # /* Light mode: dark text on light background */
# # @media (prefers-color-scheme: light) {
# #     .custom-header {
# #         color: #111111;
# #         font-size: 24px;
# #         font-weight: bold;
# #     }
# #     .team-names {
# #         color: #222222;
# #     }
# # }

# # /* Dark mode: light text on dark background */
# # @media (prefers-color-scheme: dark) {
# #     .custom-header {
# #         color: #ffffff;
# #         font-size: 24px;
# #         font-weight: bold;
# #     }
# #     .team-names {
# #         color: #dddddd;
# #     }
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # Render content with classes
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

# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# --- Background image CSS ---
page_bg_img = '''
<style>
.stApp {
    background-image: url('https://images.unsplash.com/photo-1508780709619-79562169bc64');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Render content ---
st.title("📊 Dividend Trend Predictor")

st.markdown("""
<span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

<br>

Team Members:
- Samritha Aadhi Ravikumar MSDS'25
- Akshara Ramprasad MSDS'25
- Crystal Leatvanich MSBA'25
""", unsafe_allow_html=True)



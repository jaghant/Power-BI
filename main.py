import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
# Page title
st.set_page_config(page_title = "Power BI Projects",
                   page_icon = ":dart:",
                   layout = "wide")

# Nave bar
with st.sidebar:
    image = Image.open('logo.png')
    st.image(image,  width = 200)
    selected = option_menu(
    menu_title    = "Menu",
    options       = ["Hotel" , "Lottery", "Sports", "Sales"],
    icons         = ["building", "ticket-detailed-fill", "dribbble", "cart4"],
    menu_icon     = "cast",
    default_index = 0,
    orientation   = "parellel"
)
    
# Hotel Dashboard
if selected == "Hotel":
    st.subheader(f"🏩{selected}")   
    st.markdown("""
<iframe src="https://app.powerbi.com/view?r=eyJrIjoiNjZjMGUxNTctYzUwNC00MzU1LTk4MjMtMTE0ZGUyZmE4Nzc1IiwidCI6IjJkMWUxN2Q0LWRlYzMtNGM4NS05MjcxLTIzYjIxZmM5ODhkMCJ9" 
width="1400" height="800">
</iframe>
""", unsafe_allow_html=True)
    
# Lottery Dashboard
if selected == "Lottery":
    st.subheader(f"🎫{selected}")    
    st.markdown("""
<iframe src="https://app.powerbi.com/view?r=eyJrIjoiZjQzMTI0MmMtYWZhNy00MmJiLTk1OTktN2I5YjcyODNjZjgwIiwidCI6IjJkMWUxN2Q0LWRlYzMtNGM4NS05MjcxLTIzYjIxZmM5ODhkMCJ9" 
width="1400" height="800">
</iframe>
""", unsafe_allow_html=True)
    
    
if selected == "Sports":
    st.subheader(f"⚽{selected}")  
    st.markdown("""
<iframe src="https://app.powerbi.com/view?r=eyJrIjoiMTM0MTI2ZjMtNDRjZi00MTM5LWI5MmQtNDAzNDRhNzYyZjYzIiwidCI6IjJkMWUxN2Q0LWRlYzMtNGM4NS05MjcxLTIzYjIxZmM5ODhkMCJ9" 
width="1400" height="800">
</iframe>
""", unsafe_allow_html=True)  
    
    
    
if selected == "Sales":
    st.subheader(f"🏬{selected}")
    
    st.markdown("""
<iframe src="https://app.powerbi.com/view?r=eyJrIjoiMmQyMzA4YWYtNjAxYS00YzY1LWJhYTgtOWFiZGU3YmM3MWEzIiwidCI6IjJkMWUxN2Q0LWRlYzMtNGM4NS05MjcxLTIzYjIxZmM5ODhkMCJ9" 
width="1400" height="800">
</iframe>
""", unsafe_allow_html=True)
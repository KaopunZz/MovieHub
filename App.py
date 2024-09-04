import pickle
from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, Section, show_pages, add_page_title, show_pages_from_config
import streamlit_authenticator as stauth
from PIL import Image
    
add_page_title()

show_pages(
    [
        Page("App.py","Main page","🎥"),
        Section(name="Movie list", icon="🎞"),
        # Pages after a section will be indented
        Page("pages/OnAir.py",'On-Air', icon="🎬"),
        Page("pages/Coming Soon.py",'Coming Soon', icon="🎬"),
        Page("pages/Out.py","Out","🎬"),
        # Unless you explicitly say in_section=False
        Page("pages/Playlist.py",'Playlist', icon="📼", in_section=False)
    ]
)

# --- USER AUTHENTICATION ---
names = ["Namo Puttaya", "John Osen"]
usernames = ["lnwza007", "jonh"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=1)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    #sidebar menu
    st.sidebar.title(f"Welcome {name}")
    authenticator.logout("Logout", "sidebar")
    selected = option_menu(None,["On-Air", 'Coming Soon', "Out"], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0, orientation="horizontal")

    if selected == "On-Air":
        st.title("On-Air")
        st.image(Image.open('img\on air.jpg'))
        OnAir_button = st.button("More")
        if OnAir_button:
            switch_page("On-Air")
        
    if selected == "Coming Soon":
        st.title("Coming Soon")
        st.image(Image.open('img\Coming Soon.jpg'))
        ComingSoon_button = st.button("More")
        if ComingSoon_button:
            switch_page("Coming Soon")

    if selected == "Out":
        st.title("Out")
        st.image(Image.open('img\out.jpg'))
        Out_button = st.button("More")
        if Out_button:
            switch_page("Out")



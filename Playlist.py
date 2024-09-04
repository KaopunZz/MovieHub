import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, show_pages_from_config

add_page_title()

show_pages(
    [
        Page("App.py","Main page","🎥"),
        # Unless you explicitly say in_section=False
        Page("pages/Playlist.py",'Playlist', icon="📼", in_section=False)
    ]
)

st.title("Playlist")
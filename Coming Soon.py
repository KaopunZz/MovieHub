import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, show_pages_from_config

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

st.subheader("Coming Soon")
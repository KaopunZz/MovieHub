import streamlit as st
import pandas as pd
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

st.write("On Airr")

df = pd.read_csv("data/imdb_top_1000.csv")  # read a CSV file
# df = pd.read_excel(...)  # will work for Excel files

df.index = df.loc[:,'Series_Title'] #change index to Series_Title
df.drop('Series_Title', axis=1, inplace=True) #delete Series_Title column

st.write(df)
st.write(df.loc['The Godfather'])  # data from Movie name
st.write(df.loc['The Godfather'][0])  # Poster_Link data
st.write(df.loc['The Godfather'][1])  # Released_Year data

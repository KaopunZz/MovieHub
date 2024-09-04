import streamlit as st
import pandas as pd
from PIL import Image


df = pd.read_csv("data/imdb_top_1000.csv")  # read a CSV file
# df = pd.read_excel(...)  # will work for Excel files

df.index = df.loc[:,'Series_Title'] #change index to Series_Title
df.drop('Series_Title', axis=1, inplace=True) #delete Series_Title column

st.write(df)
st.write(df.loc['The Godfather'])  # data from Movie name
st.write(df.loc['The Godfather'][0])  # Poster_Link data
st.write(df.loc['The Godfather'][1])  # Released_Year data


image = df.loc['The Godfather'][0]

st.image(image, caption='Sunrise by the mountains')
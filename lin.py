import streamlit as st
import pandas as pd
# from pydataset import data


# cred = credentials.Certificate("commenttt-28708-8720b90b9c8b.json")
# firebase_admin.initialize_app(cred)
# firebase_admin.get_app()

st.title('🎈 Movie :red[all]')

df = pd.read_csv(r"data/imdb_top_1000.csv")  # read a CSV file


df.index = df.loc[:,'Series_Title'] #change index to Series_Title
df.drop('Series_Title', axis=1, inplace=True) #delete Series_Title column


selected_movie = st.sidebar.selectbox('Select Movie', (df.index))

st.write(df)


st.title('🎈 Movie :red[find]')
st.write(df.loc[selected_movie])  # data from Movie name

image = df.loc[selected_movie][0]
st.image(image,width=400)

# st.write(df.loc[selected_movie][0])  # Poster_Link data

st.write(df.loc[selected_movie][1])  # Released_Year data


title_data = df.loc[selected_movie][6]
st.write(title_data)


st.button('FAV')
st.button('LIKE')
st.button('DISLIKE')
tab1, tab2 = st.tabs(['TAB 1','TAB 2'])
tab1.text_area('comments')
tab2.text_area('add comment')
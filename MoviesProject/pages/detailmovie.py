import streamlit as st
import pandas as pd
import database as db
import numpy as np 

import sys
sys.path.append('\\MoviesProject\\')


global dc
global selected_movie
global user_uid 

try:
    user_uid = st.session_state.username
except:
    pass

dc = pd.read_csv(r"MoviesProject/data/comments.csv", index_col=[0])
# dc.index = dc.loc[:,'Series_Title'] #change index to Series_Title
# dc.drop('Series_Title', axis=1, inplace=True)
# st.write(dc)


df = pd.read_csv(r"MoviesProject/data/moviedata.csv")  # read a CSV file
df.index = df.loc[:,'Series_Title'] #change index to Series_Title
df.drop('Series_Title', axis=1, inplace=True)#delete Series_Title column

def removewatchlist(movie_name):
    movielist = db.get_data(user_uid)['movielist']
    movielist.remove(movie_name)
    data = {'movielist':movielist}
    db.update_data(user_uid,data)

def addwatchlist(movie_name):
    movielist = db.get_data(user_uid)['movielist']
    movielist.append(movie_name)
    data = {'movielist':movielist}
    db.update_data(user_uid,data)

def checkNaN():
    try:
        np.isnan(dc['comments'][selected_movie])
        return True
    except:
        return False


def detail(selected_movie):
    st.title('🎈 Movie :red[find]')
    image = df.loc[selected_movie]['Poster_Link']
    st.image(image,width=400)
    st.write(df.loc[selected_movie])  # data from Movie name
    st.write(df.loc[selected_movie]['Released_Year'])  # Released_Year data
    st.write(df.loc[selected_movie]['Overview'])
    try:
        #### Watchlist Button #####
        user_uid = st.session_state.username
        if selected_movie in db.get_data(user_uid)['movielist']:
            if st.button('Remove from Watchlist'):
                removewatchlist(selected_movie)
        else:
            if st.button('Add to Watchlist'):
                addwatchlist(selected_movie)
                
        #### Like Button #####
        col1, col2, col3 = st.columns((1,1,5))

        with col1:
            like = df.loc[selected_movie]['Like']
            if st.button(f'{like} LIKE'):
                df.at[selected_movie,'Like'] += 1
                df.to_csv(r"MoviesProject/data/moviedata.csv")

        with col2:
            dislike = df.loc[selected_movie]['Dislike']
            if st.button(f'{dislike} DISLIKE'):
                df.at[selected_movie,'Dislike'] += 1
                df.to_csv(r"MoviesProject/data/moviedata.csv")

        ####COMMENT####
        ####tab1####
        tab1, tab2 = st.tabs(['Commends','Send'])
        if checkNaN():
            tab1.write('No comments')
        else:
            comment_list = eval(dc['comments'][selected_movie])
            for i in range(len(comment_list)):
                tab1.write(comment_list[i])

        ####tab2####
        comment=tab2.text_input('Your comments')
        if tab2.button('comment'):
            if checkNaN():
                comment_list = []
            else:
                comment_list = eval(dc['comments'][selected_movie])
            comment_list.append(f'{user_uid} : {comment}')
            dc['comments'][selected_movie] = comment_list
            dc.to_csv(r"MoviesProject/data/comments.csv")
    except:
        # st.write('Error')
        pass

selected_movie = st.sidebar.selectbox('Select Movie', (df.index))
# st.write('Select movie',selected_movie)

detail(selected_movie)


#comment parent




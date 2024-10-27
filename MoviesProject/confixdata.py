import streamlit as st
import pandas as pd
import database as db
import numpy as np 

df = pd.read_csv("data\moviedata.csv", index_col=[0])  # read a CSV file
dc = pd.read_csv("data\comments.csv", index_col=[0])

selected_movie = st.sidebar.selectbox('Select Movie Onair', df.index)

# df.drop('Unnamed: 0', axis=1, inplace=True)
# df.to_csv("data\moviedata.csv")

# df2 = df['Series_Title']
# df2.to_csv('data/comments2.csv')
# dc['comments'] = None
# dc.to_csv("data\comments.csv")

# st.write(df)
st.write(dc)

tab1, tab2 = st.tabs(['TAB 1','TAB 2'])
comment=tab1.text_input('comments')
st.write('VVV comment VVV')
st.write(comment)
st.write('VVV selected_movie VVV')
st.write(selected_movie)
st.write('VVV movie comment VVV')
st.write(dc['comments'][selected_movie])
st.write(dc)
st.write(np.isnan(dc['comments'][selected_movie]))
user = 'admin'
if st.button('comment'):
    try:
        np.isnan(dc['comments'][selected_movie])
        comment_list = [] 
        st.write('None<<<<<')
    except:
        comment_list = eval(dc['comments'][selected_movie])
        st.write('Something<<<<<')
    

    comment_list.append(f'{user} : {comment}')
    dc['comments'][selected_movie] = comment_list
    dc.to_csv("data\comments.csv")

# st.write(eval(dc['comments'][selected_movie])[0])

#     st.write(comment_list)
#     st.write('comment_list')
# st.write(dc)

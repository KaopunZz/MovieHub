import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, Section, show_pages, add_page_title, show_pages_from_config
import streamlit_authenticator as stauth
from PIL import Image
from st_click_detector import click_detector
import time
from pages import detailmovie
import database as db
import sys

sys.path.append('\\MoviesProject\\')


add_page_title()

show_pages(
    [
        Page(r"MoviesProject/main.py", "Main page", icon="🎥"),
        Page(r"MoviesProject/watchlist.py", 'Watchlist', icon="📼"),
        Page(r"MoviesProject/pages/loginpage.py", 'Login', icon="🍿"),
        Page(r"MoviesProject/pages/detailmovie.py", 'detail', icon="🎬"),
        #Page("testWebpage.py", 'testWebpage', icon="🎬"),
        #Page("file path", 'page name', icon="🎬")
    ]
)

def change_page():
    switch_page("detail")




selected = option_menu(None,["On-Air", 'Coming Soon', "All"], 
    icons=['house', 'gear'], menu_icon="cast", default_index=0, orientation="horizontal")

if selected == "On-Air":
    df = pd.read_csv(r"MoviesProject/data/onair.csv")  # read a CSV file

    st.title("Find movie On-Air")
    text_search = st.text_input("Search ", value="")

    m1 = df["Series_Title"].str.contains(text_search)
    m2 = df["Genre"].str.contains(text_search)
    df_search = df[m1 | m2]
    
    if text_search:
        #st.write(df_search)
        
        #st.write(df.loc[:,'Series_Title'][m1])  
        #st.write(df.loc[:,'Genre'][m2])
        st.write(text_search,": Movie Title")
        for i in range (0,len(df.loc[:,'Series_Title'][m1])):
            if i >= 0: 
                st.write(i+1,(df.loc[m1, 'Series_Title'].iloc[i])) 
                image = df.loc[m1, 'Poster_Link'].iloc[i]
                st.image(image,width=400)
                st.markdown("***")
                i+=1 
            else:
                pass
        st.write(text_search,': Genres')
        for i in range (0,len(df.loc[:,'Genre'][m2])):
            if i >= 0: 
                st.write(i+1,(df.loc[m2, 'Genre'].iloc[i])) 
                image = df.loc[m2, 'Poster_Link'].iloc[i]
                st.image(image,width=400)
                st.markdown("***")
                i+=1 
            else:
                pass

    st.title("All movie On-Air")

    for i in range (0,len(df)):
        Series_Title = df.loc[:,'Series_Title'][i]
        content = f"""
                <a href='#' id={Series_Title}><img width='40%' src={df.loc[:,'Poster_Link'][i]}></a>
                """
        clicked = click_detector(content)
        
        if clicked != "":
        # If a movie poster is clicked, change to the "detail" page
            change_page()
        else:
            pass
        
        # st.markdown(change_page() if clicked != "" else "")
        # st.markdown(f"{change_page()}{change_title()}" if clicked != "" else "")

        
        
        st.write(df.loc[:,'Genre'][i])
        st.write(df.loc[:,'Series_Title'][i])  
        st.markdown("***")
    




#    if st.button('more'):
#         st.title("All movie On-Air")
#         for i in range (0,len(df)):
#             image = df.loc[:,'Poster_Link'][i]
#             st.image(image,width=400)
#             st.write(df.loc[:,'Genre'][i])
#             st.write(df.loc[:,'Series_Title'][i])  
#             st.markdown("***")

if selected == "Coming Soon":
    df = pd.read_csv(r"MoviesProject/data/comingsoon.csv")
    st.title("Find movie comingsoon")
    text_search = st.text_input("Search ", value="")

    m1 = df["Series_Title"].str.contains(text_search)
    m2 = df["Genre"].str.contains(text_search)
    df_search = df[m1 | m2]
    
    if text_search:
        #st.write(df_search)
        
        #st.write(df.loc[:,'Series_Title'][m1])  
        #st.write(df.loc[:,'Genre'][m2])
        st.write(text_search,": Movie Title")
        for i in range (0,len(df.loc[:,'Series_Title'][m1])):
            if i >= 0: 
                st.write(i+1,(df.loc[m1, 'Series_Title'].iloc[i])) 
                image = df.loc[m1, 'Poster_Link'].iloc[i]
                st.image(image,width=400)
                st.markdown("***")
                i+=1 
            else:
                pass
        st.write(text_search,': Genres')
        for i in range (0,len(df.loc[:,'Genre'][m2])):
            if i >= 0: 
                st.write(i+1,(df.loc[m2, 'Genre'].iloc[i])) 
                image = df.loc[m2, 'Poster_Link'].iloc[i]
                st.image(image,width=400)
                st.markdown("***")
                i+=1 
            else:
                pass

    
    st.title("Comingsoon")
    for i in range (0,len(df)):
        Series_Title = df.loc[:,'Series_Title'][i]
        content = f"""
                <a href='#' id={Series_Title}><img width='40%' src={df.loc[:,'Poster_Link'][i]}></a>
                """
        clicked = click_detector(content)
        
        if clicked != "":
        # If a movie poster is clicked, change to the "detail" page
            change_page()
        else:
            pass

        st.write(df.loc[:,'Genre'][i])
        st.write(df.loc[:,'Series_Title'][i]) 
        st.markdown("***")
        
if selected == "All":
    df = pd.read_csv(r"MoviesProject/data/imdb_top_1000.csv")

    st.title("Find All movie")
    text_search = st.text_input("Search ", value="")

    m1 = df["Series_Title"].str.contains(text_search)
    m2 = df["Genre"].str.contains(text_search)
    df_search = df[m1 | m2]
    
    if text_search:
        #st.write(df_search)
        
        #st.write(df.loc[:,'Series_Title'][m1])  
        #st.write(df.loc[:,'Genre'][m2])
        st.write(text_search,": Movie Title")
        for i in range (0,len(df.loc[:,'Series_Title'][m1])):
            if i >= 0: 
                st.write(i+1,(df.loc[m1, 'Series_Title'].iloc[i])) 
                image = df.loc[m1, 'Poster_Link'].iloc[i]
                st.image(image,width=400)
                st.markdown("***")
                i+=1 
            else:
                pass
        st.write(text_search,': Genres')
        for i in range (0,len(df.loc[:,'Genre'][m2])):
            if i >= 0: 
                st.write(i+1,(df.loc[m2, 'Genre'].iloc[i])) 
                image = df.loc[m2, 'Poster_Link'].iloc[i]
                st.image(image,width=400)
                st.markdown("***")
                i+=1 
            else:
                pass

    
    st.title("All movie")
    for i in range (0,100):
        Series_Title = df.loc[:,'Series_Title'][i]
        content = f"""
                <a href='#' id={Series_Title}><img width='40%' src={df.loc[:,'Poster_Link'][i]}></a>
                """
        clicked = click_detector(content)
        
        if clicked != "":
        # If a movie poster is clicked, change to the "detail" page
            change_page()
        else:
            pass

        st.write(df.loc[:,'Genre'][i])
        st.write(df.loc[:,'Series_Title'][i]) 
        st.markdown("***")

import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, show_pages_from_config
from streamlit_option_menu import option_menu
import database as db
import pandas as pd
import testforlogin as tfl
import sys

sys.path.append('\\MoviesProject\\')


# add_page_title()

# # Define the list of pages
# show_pages(
#     [
#         Page(r"MoviesProject/main.py", "Main page", icon="🎥"),
#         Page(r"MoviesProject/playlist.py", 'Playlist', icon="📼"),
#         Page(r"MoviesProject/pages/loginpage.py", 'Login', icon="🍿"),
#         Page(r"MoviesProject/pages/detailmovie.py", 'detail', icon="🎬") #ลองแล้วมึนเดียวมาลองต่อT-T
#     ]
# )

# df = pd.read_csv("data/imdb_top_1000.csv")  # read a CSV file
# df.index = df.loc[:, 'Series_Title']  # change index to Series_Title
# df.drop('Series_Title', axis=1, inplace=True)  # delete Series_Title column

# # Get the image URLs from the DataFrame based on movielist
# movielist = db.get_data('Kaopun')['movielist']
# image_urls = [df.loc[movie]['Poster_Link'] for movie in movielist]

# # Display images in a horizontal scrollable list
# st.markdown(
#     """
#     <style>
#         .scroll {
#             display: flex;
#             white-space: nowrap;
#             overflow-x: auto;
#         }
#         .scroll img {
#             margin-right: 10px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Create the HTML content for the scrollable image list
# image_list_html = "<div class='scroll'>"
# for image_url in image_urls:
#     image_list_html += f'<img src="{image_url}" style="width:350px; height:350px;" alt="Image Caption"/>'
# image_list_html += "</div>"

# # Display the HTML content
# st.markdown(image_list_html, unsafe_allow_html=True)



add_page_title()

# Define the list of pages
show_pages(
    [
        Page(r"MoviesProject/main.py", "Main page", icon="🎥"),
        Page(r"MoviesProject/watchlist.py", 'Watchlist', icon="📼"),
        Page(r"MoviesProject/pages/loginpage.py", 'Login', icon="🍿"),
        Page(r"MoviesProject/pages/detailmovie.py", 'detail', icon="🎬")
    ]
)

df = pd.read_csv(r"MoviesProject/data/imdb_top_1000.csv")  # read a CSV file
df.index = df.loc[:, 'Series_Title']  # change index to Series_Title
df.drop('Series_Title', axis=1, inplace=True)  # delete Series_Title column

def watchlist(user_uid):
    movielist = db.get_data(user_uid)['movielist'] if user_uid in db.get_user() else []

    # Get the image URLs from the DataFrame based on movielist
    image_urls = [df.loc[movie]['Poster_Link'] for movie in movielist]

    # Display images in a horizontal scrollable list
    st.markdown(
        """
        <style>
            .scroll {
                display: flex;
                white-space: nowrap;
                overflow-x: auto;
            }
            .scroll img {
                margin-right: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the HTML content for the scrollable image list
    image_list_html = "<div class='scroll'>"
    for image_url in image_urls:
        image_list_html += f'<img src="{image_url}" style="width:350px; height:350px;" alt="Image Caption"/>'
    image_list_html += "</div>"

    # Display the HTML content
    st.markdown(image_list_html, unsafe_allow_html=True)

# Get the user's movielist from Firestore
user_uid = st.session_state.username
watchlist(user_uid)

username = st.text_input('See Other Watchlist')
watchlist(username)

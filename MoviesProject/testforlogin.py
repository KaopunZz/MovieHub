import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import database as db
import sys

sys.path.append('\\MoviesProject\\')


cred = credentials.Certificate(r"MoviesProject/moviehublogindata.json")

try:
    firebase_admin.initialize_app(cred)
    firebase_admin.get_app()
except:
    firebase_admin.delete_app(firebase_admin.get_app())
    firebase_admin.initialize_app(cred)
    firebase_admin.get_app()

def app():
    st.title('Welcome to Movie:red[hub] 🍿')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def f():
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            global Usernm
            Usernm = user.uid

            st.session_state.signedout = True
            st.session_state.signout = True  

            if Usernm in db.get_user():
                pass
            else:
                watchlist = {'movielist':[]}
                db.update_data(Usernm,watchlist)

        except: 
            st.warning('Login Failed')

    

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''

    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False

    if not st.session_state["signedout"]:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password',type='password')
        
        if choice == 'Sign up':
            # email = st.text_input('Email Address')
            # password = st.text_input('Password', type='password')
            username = st.text_input("Enter your unique username")
            
            if st.button('Create my account'):
                user = auth.create_user(email=email, password=password, uid=username)
                
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
        else:
            st.button('Login', on_click=f)
            
    if st.session_state.signout:
        st.text('Name ' + st.session_state.username)
        st.text('Email id: ' + st.session_state.useremail)
        st.button('Sign out', on_click=t)






#

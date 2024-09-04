import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Namo Puttaya", "John Osen"]
usernames = ["lnwza007", "jonh"]
passwords = ["1234", "5678"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
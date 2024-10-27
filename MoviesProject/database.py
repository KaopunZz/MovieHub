import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import testforlogin as tfl
import sys

sys.path.append('\\MoviesProject\\')

# Use a service account.
cred = credentials.Certificate(r"MoviesProject/moviehubdatafirebase.json")

try:
    firebase_admin.initialize_app(cred)
    db = firestore.client()
except:
    firebase_admin.delete_app(firebase_admin.get_app())
    firebase_admin.initialize_app(cred)
    db = firestore.client()



#Update data to database
#data เป็น list
def update_data(user,data):
    db.collection("watchlist").document(user).set(data, merge=True)

#Read data from database
def get_data(user):  
    doc = db.collection("watchlist").document(user).get()
    return doc.to_dict()

def get_user(): 
    docs = db.collection("watchlist").stream()
    return [doc.id for doc in docs]
#Example data
# user = 'admin'
# data = {'movielist': ['Inception', 'Saving Private Ryan', 'Back to the Future']}

# update_data(user,data)

# print(get_data('TonKhing')) #watchlist of tonkhing

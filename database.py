import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('moviehub-150d6-firebase-adminsdk-xv90g-531584a528.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

#Update data to database
#data เป็น list
def update_data(user,data):
    db.collection("watchlist").document(user).set(data, merge=True)

#Read data from database
def get_data(user):  
    doc = db.collection("watchlist").document(user).get()
    return doc.to_dict()


#Example data
user = 'TonKhing'
data = {'movielist': ['khing 56', 'spidy', 'KaopunSlayer']}


update_data(user,data)

print(get_data(user).values()) #watchlist of tonkhing

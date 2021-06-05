import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./service-account.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# collection = db.collection(u'companies')
# documents = list(collection.get())
# print("# of documents in collection: {}".format(len(documents)))


with open("complete_companies.json", "r") as f:
    file_contents = json.load(f)
# for index,value in enumerate(file_contents):
#         if index > 3337:
#             collection.document(value["symbol"]).set(value)


    # if len(value["symbol"]) > 0:
        #


# ref.set(file_contents)

# for doc in collection:
#     print(f'{doc.id} => {doc.to_dict()}')

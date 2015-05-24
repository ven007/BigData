import pymongo
from pprint import pprint
from pymongo import MongoClient
connection = MongoClient()
db=connection.crime
collection=db.crimestats

#names=db.names

#post = {"author": "Mike",
       #"text": "My first blog post!",
       #"tags": ["mongodb", "python", "pymongo"]}

#result = db.collection.insert_one({'x': 1})
#result.inserted_id


item=collection.find()


#print db.crimestats.find()
for doc in collection.find():
    pprint(doc)



import pymongo
import hashlib
import base64
import uuid
from passlib.hash import sha256_crypt



from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.chatroom
collection = db.user


while True:
        
    user = input('username')
    password1 = input('password')
    password = sha256_crypt.encrypt(password1)



    userObj = {
        "username":user,
        "password":password
    }
    res = collection.find_one({"username":user})
    if not (res):
        insertedDoc = collection.insert_one(userObj)
        break 



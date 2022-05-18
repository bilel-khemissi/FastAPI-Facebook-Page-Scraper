from pymongo import MongoClient

## create mongodb to store scrapped data
client = MongoClient("mongodb://localhost:27017") ## by default the port is 27017
db = client["Facebook_scrapper_api"]
collection = db["posts"]


def insert_post(post):
    return collection.insert_one(post)

def insert_posts(posts):
    return collection.insert_many(posts)

def find_posts(page_name = None):
    if page_name is None : 
        return list(collection.find())
    return list(collection.find({'username' : page_name}))

import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.environ["MONGO_URI"]
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
    word_collection = client.games.words

    id = 1
    with open("palabras_rae_completo.txt", "r", encoding="utf-8", newline="\n") as words_file:
        for word in words_file:
            word_collection.insert_one({"Id": id, "Name": word.replace("\n", "")})
            id += 1
    print(f"Exported {id} entries")
except Exception as e:
    print(e)

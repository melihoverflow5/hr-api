from pymongo import MongoClient
from flask import g
from bson import ObjectId

mongo = MongoClient("mongodb://localhost:27017/")

class MongoDbHelper:
        def __init__(self, db_name: str, collection_name: str):
            global mongo
            self.db = mongo[db_name]
            self.collection_name = collection_name

        def get_collection(self):
            return self.db[self.collection_name]

        def add(self, entity: object) -> object:
            result = self.get_collection().insert_one(entity)
            return result.inserted_id

        def get_single(self, predicate: object) -> object:
            result = self.get_collection().find_one(predicate)
            return result

        def get_single_by_id(self, _id) -> object:
            result = self.get_single({"_id": ObjectId(_id), })
            return result

        # def set_database(self):
        #     self.db = mongo[g.database]


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

        def get_all(self, predicate: object = None, fields: object = None, sort: str = None, limit: int = None,
                    skip: int = None) -> object:
            result = self.get_collection().find(predicate, fields)

            if sort is not None:
                # print("sort")
                result = result.sort(sort, -1)

            if limit is not None:
                # print("limit")
                result = result.limit(limit)

            if skip is not None:
                # print("skip")
                result = result.skip(skip)

            return result

        def edit(self, predicate: dict, value: dict, is_upsert: bool = False) -> dict:
            """ UpdateOne({'_id': 4}, {'$inc': {'j': 1}}, upsert=True) """
            result = self.get_collection().update_one(predicate, {'$set': value}, upsert=is_upsert)
            return dict(
                matched_count=result.matched_count,
                modified_count=result.modified_count,
                upserted_id=result.upserted_id
            )

        def remove(self, predicate: dict):
            result = self.get_collection().delete_one(predicate)
            return result.deleted_count
from src.repositories.base_repository import BaseRepository
from flask import g
from bson import ObjectId


class UserRepository(BaseRepository):
        def __init__(self):
            super().__init__(g.database, "users")

        def change_password(self, _id, password):
            result = self.get_collection().update_one({"_id": _id}, {"$set": {"password": password}})
            return dict(
                matched_count=result.matched_count,
                modified_count=result.modified_count,
                upserted_id=result.upserted_id
            )

        def change_first_password(self, _id, password):
            result = self.get_collection().update_one({"_id": ObjectId(_id)}, {"$set": {"password": password, "first_login": False}})
            return dict(
                matched_count=result.matched_count,
                modified_count=result.modified_count,
                upserted_id=result.upserted_id
            )

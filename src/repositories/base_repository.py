from src.helpers.mongodb_helper import MongoDbHelper


class BaseRepository(MongoDbHelper):
    def __init__(self, db_name: str, collection_name: str):
        super().__init__(db_name, collection_name)




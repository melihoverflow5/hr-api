from src.repositories.base_repository import BaseRepository
from flask import g


class UserRepository(BaseRepository):
        def __init__(self):
            super().__init__(g.database, "users")

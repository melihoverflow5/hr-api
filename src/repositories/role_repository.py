from src.repositories.base_repository import BaseRepository

class RoleRepository(BaseRepository):
        def __init__(self):
            super().__init__("hr-api", "roles")
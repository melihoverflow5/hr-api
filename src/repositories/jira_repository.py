from src.repositories.base_repository import BaseRepository
from src.commons.exceptions import ExistError, NotFoundError, ServiceError
from flask import g

class JiraRepository(BaseRepository):
    def __init__(self):
        super().__init__(g.database, "jira")

    def jira_status(self):
        result = self.get_collection().find_one({"key": "jira_username"})
        if result is None:
            return False
        else:
            return True

    def get_jira(self):
        if self.jira_status() == False:
            raise NotFoundError(message="Jira not connected", code=404)
        result = {
            'jira_username': self.get_username(),
            'jira_api_key': self.get_api_key(),
            'jira_cloud': self.get_cloud(),
            'jira_url': self.get_url()
        }
        return result
    def get_username(self):
        result = self.get_single({"key": "jira_username"})
        if result == None:
            return None
        result = result['value']
        return result

    def get_api_key(self):
        result = self.get_single({"key": "jira_api_key"})
        result = result['value']
        return result

    def get_cloud(self):
        result = self.get_single({"key": "jira_cloud"})
        result = result['value']
        return result

    def get_url(self):
        result = self.get_single({"key": "jira_url"})
        result = result['value']
        return result

    def add_jira(self, schema):
        if self.get_username() is not None:
            raise ExistError(message="Jira already connected", code=409)
        for key in schema.keys():
            result = self.get_collection().insert_one({"key": key, "value": schema[key]})
            if result.inserted_id is None:
                raise ServiceError(message="Error adding jira", code=500)
        result = self.get_jira()

        return result

    def delete(self):
        if self.get_username() is None:
            raise NotFoundError(message="Jira not connected", code=404)
        result = self.get_collection().delete_many({})
        return True
    def update(self, schema):
        if self.get_username() is None:
            raise NotFoundError(message="Jira not connected", code=404)
        for key in schema.keys():
            result = self.get_collection().update_one({"key": key}, {"$set": {"value": schema[key]}})
            if result.matched_count != 1:
                raise ServiceError(message="Error updating jira", code=500)

        result = self.get_jira()
        result['jira_api_key'] = "************"

        return result

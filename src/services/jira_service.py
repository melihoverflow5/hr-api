from src.services.base_service import BaseService
from src.helpers.jira_helper import JiraHelper
from src.repositories.jira_repository import JiraRepository
from flask import current_app as app

class JiraService(BaseService):

    def __init__(self):
        super().__init__()
        self.__jira_repository = JiraRepository()
        self.__jira_helper = JiraHelper()


    def get_all_projects(self):
        result = self.__jira_helper.get_all_projects()
        return result

    def get_issues_by_user(self, jira_id):
        result = self.__jira_helper.get_issues_by_user(jira_id)
        return result

    def get_all_users(self):
        result = self.__jira_helper.get_all_users()
        return result

    def get_jira(self):
        result = self.__jira_repository.get_jira()
        result['jira_api_key'] = "************"
        return result

    def add(self, schema):
        result = self.__jira_repository.add_jira(schema)
        return result

    def delete(self):
        result = self.__jira_repository.delete()
        return result

    def update(self, schema):
        result = self.__jira_repository.update(schema)
        return result

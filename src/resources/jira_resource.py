from src.resources.base_resource import BaseResource
from src.services.jira_service import JiraService
from src.schemas.jira_schema import JiraSchema, JiraUpdateSchema
from src.commons.response import ok_result
from flask import request

class JiraCollectionResource(BaseResource):

    def __init__(self):
        super().__init__()
        self.__jira_service = JiraService()

    def get(self):
        result = self.__jira_service.get_jira()
        return ok_result(result)

    def post(self):
        schema = JiraSchema().get_json()
        result = self.__jira_service.add(schema)
        return ok_result(result)

    def put(self):
        schema = JiraUpdateSchema().get_json()
        result = self.__jira_service.update(schema)
        return ok_result(result)

    def delete(self):
        result = self.__jira_service.delete()
        return ok_result(result)


class JiraItemCollectionResource(BaseResource):

    def __init__(self):
        super().__init__()
        self.__jira_service = JiraService()

    def get(self, jira_id):
        result = self.__jira_service.get_issues_by_user(jira_id)
        return ok_result(result)

class JiraUserCollectionResource(BaseResource):

    def __init__(self):
        super().__init__()
        self.__jira_service = JiraService()

    def get(self):
        result = self.__jira_service.get_all_users()
        return ok_result(result)

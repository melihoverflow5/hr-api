from flask_injector import inject

from src.resources.base_resource import BaseResource
from src.services.auth_service import AuthService
from src.schemas.auth_schema import AuthLoginSchema, SSOSchema

from src.commons.response import created_result, no_content_result, ok_result
from flask_jwt_extended import jwt_required


class AuthLoginResource(BaseResource):
    @inject
    def __init__(self, __auth_service: AuthService):
        super().__init__()
        self.__auth_service = __auth_service

    def post(self):
        schema = AuthLoginSchema().get_json()
        result = self.__auth_service.login(schema=schema)
        return created_result(result)

    @jwt_required(refresh=True)
    def put(self):
        result = self.__auth_service.refresh_access_token()
        return created_result(result)

    @jwt_required()
    def delete(self):
        self.__auth_service.logout()
        return no_content_result()


class AuthLoginUserResource(BaseResource):
    @inject
    def __init__(self, __auth_service: AuthService):
        super().__init__()
        self.__auth_service = __auth_service

    @jwt_required()
    def get(self):
        result = self.__auth_service.get_login_user()
        return ok_result(result)

class SSOResource(BaseResource):
    @inject
    def __init__(self, __auth_service: AuthService):
        super().__init__()
        self.__auth_service = __auth_service

    @jwt_required()
    def post(self):
        schema = SSOSchema().get_json()
        result = self.__auth_service.sso(schema=schema)
        return ok_result(result)
from src.resources.base_resource import BaseResource
from src.services.user_service import UserService
from src.schemas.user_schema import UserCollectionSchema, UserCollectionSearchSchema
from src.schemas.pagination_schema import PaginationSchema
from src.commons.response import created_result, ok_result

from flask_jwt_extended import jwt_required
from src.commons.auth import authorize

class UserCollectionResource(BaseResource):
    def __init__(self):
        super().__init__()
        self.__user_service = UserService()

    @jwt_required()
    @authorize(roles=["show_user"])
    def get(self):
        # predicate = UserCollectionSearchSchema().get_args()
        pagination = PaginationSchema().get_args()
        result = self.__user_service.get_all(pagination=pagination)
        return ok_result(data=result)

    @jwt_required()
    @authorize(roles=["create_user"])
    def post(self):
        schema = UserCollectionSchema().get_json()
        result = self.__user_service.add(schema=schema)
        return created_result(data=result)

class UserCollectionItemResource(BaseResource):
    def __init__(self):
        super().__init__()
        self.__user_service = UserService()

    @jwt_required()
    @authorize(roles=["show_user"])
    def get(self, _id):
        result = self.__user_service.get(_id=_id)
        return ok_result(data=result)

    def put(self, _id):
        schema = UserCollectionSearchSchema().get_json()
        result = self.__user_service.edit(_id=_id, schema=schema)
        return ok_result(data=result)

    def delete(self, _id):
        result = self.__user_service.delete(_id=_id)
        return ok_result(data=result)
from src.resources.base_resource import BaseResource
from src.services.title_service import TitleService
from src.schemas.title_schema import TitleCollectionSchema, TitleCollectionSearchSchema
from src.commons.response import ok_result, created_result
from flask_jwt_extended import jwt_required
from src.commons.auth import authorize

class TitleCollectionResource(BaseResource):
    def __init__(self):
        super().__init__()
        self.__title_service = TitleService()


    @jwt_required()
    @authorize(roles=["show_title"])
    def get(self):
        result = self.__title_service.get_all()
        return ok_result(data=result)

    @jwt_required()
    @authorize(roles=["create_title"])
    def post(self):
        schema = TitleCollectionSchema().get_json()
        result = self.__title_service.add(schema=schema)
        return created_result(data=result)

class TitleCollectionItemResource(BaseResource):
    def __init__(self):
        super().__init__()
        self.__title_service = TitleService()

    @jwt_required()
    @authorize(roles=["show_title"])
    def get(self, _id):
        result = self.__title_service.get(_id=_id)
        return ok_result(data=result)

    @jwt_required()
    @authorize(roles=["update_title"])
    def put(self, _id):
        schema = TitleCollectionSearchSchema().get_json()
        result = self.__title_service.edit(_id=_id, schema=schema)

        return ok_result(data=result)

    @jwt_required()
    @authorize(roles=["delete_title"])
    def delete(self, _id):
        result = self.__title_service.delete(_id=_id)
        return ok_result(data=result)
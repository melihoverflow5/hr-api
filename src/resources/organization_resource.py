from src.resources.base_resource import BaseResource
from src.services.organization_service import OrganizationService
from src.schemas.organization_schema import OrganizationCollectionSearchSchema , OrganizationCollectionSchema
from src.commons.response import ok_result, created_result
from flask_jwt_extended import jwt_required
from src.commons.auth import authorize
from bson import ObjectId
class OrganizationCollectionResource(BaseResource):
    def __init__(self):
        super().__init__()
        self.__organization_service = OrganizationService()

    @jwt_required()
    @authorize(roles=["show_organization"])
    def get(self):
        result = self.__organization_service.get_all()
        return ok_result(data=result)

    @jwt_required()
    @authorize(roles=["create_organization"])
    def post(self):
        schema = OrganizationCollectionSchema().get_json()
        result = self.__organization_service.add(schema=schema)
        return created_result(data=result)



class OrganizationItemColletionResource(BaseResource):

    def __init__(self):
        super().__init__()
        self.__organization_service = OrganizationService()


    @jwt_required()
    @authorize(roles=["show_organization"])
    def get(self, _id):
        result = self.__organization_service.get_by_id(_id=_id)
        return ok_result(data=result)

    @jwt_required()
    @authorize(roles=["update_organization"])
    def put(self, _id):
        schema = OrganizationCollectionSearchSchema().get_json()
        result = self.__organization_service.edit(_id=_id, schema=schema)
        return ok_result(data=result)

    @jwt_required()
    @authorize(roles=["delete_organization"])
    def delete(self, _id):
        result = self.__organization_service.delete(_id=_id)
        return ok_result(data=result)


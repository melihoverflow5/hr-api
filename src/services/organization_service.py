import datetime
from bson import ObjectId
from src.utils.datetime_util import get_utc_datetime
from src.services.base_service import BaseService
from src.schemas.organization_schema import OrganizationCollectionSearchSchema
from src.repositories.organization_repository import OrganizationRepository
from src.commons.exceptions import NotFoundError, ArgumentNullOrEmptyError, ExistError, BusinessRuleError


class OrganizationService(BaseService):
    def __init__(self):
        super().__init__()
        self.__organization_repository = OrganizationRepository()


    def organization_dict(self, company):
        return OrganizationCollectionSearchSchema().dump(company)

    def get_all(self):
        items = self.__organization_repository.get_all()

        if not items:
            raise NotFoundError(code="not_found", message="")

        organization_list = []
        for organization in items:
            organization_list.append(self.organization_dict(organization))

        return organization_list

    def add(self, schema):
        schema["created_at"] = get_utc_datetime()

        isCreated = self.__organization_repository.get_single(predicate={"title": schema["title"]})
        if isCreated:
           raise ExistError(code="already_exists", message="")
        result = self.__organization_repository.add(schema)
        schema["_id"] = result
        return self.organization_dict(schema)

    def get_by_id(self, _id):
        result = self.__organization_repository.get_single_by_id(_id)
        if result is None:
            raise NotFoundError(code="not_found", message="")
        return self.organization_dict(result)

    def edit(self, _id, schema):

        result = self.__organization_repository.edit(predicate={"_id": ObjectId(_id)}, value=schema)

        if result["matched_count"] == 0:
            raise NotFoundError(code="not_found", message="")
        elif result["modified_count"] == 0:
            raise BusinessRuleError(code="there_is_no_change", message="")

        result = self.__organization_repository.get_single_by_id(_id)
        return self.organization_dict(result)

    def delete(self, _id):
        result = self.__organization_repository.remove(predicate={"_id": ObjectId(_id)})
        if result == 0:
            raise NotFoundError(code="not_found", message="")
        return True

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

    def get_all(self, predicate):
        items = self.__organization_repository.get_all(predicate=predicate)

        if not items:
            raise NotFoundError(code="not_found", message="")

        organization_list = []
        for organization in items:
            organization_list.append(self.organization_dict(organization))

        return organization_list

    def add(self, schema):
        if schema["title"] is None or  schema["description"] is None or schema["is_demo"] is None:
            raise ArgumentNullOrEmptyError("title, description, is_demo")

        if schema["support_end_date"] is None:
            schema["support_end_date"] = (datetime.datetime.now() + datetime.timedelta(days=365*10))
        schema["created_at"] = get_utc_datetime()
        schema["status"] = True

        created = self.__organization_repository.get_single(predicate={"title": schema["title"]})
        if created:
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
        try:
            result = self.__organization_repository.edit(predicate={"_id": ObjectId(_id)}, value=schema)
        except Exception as ex:
            raise BusinessRuleError(code="already_exists", message=str(ex))

        if result["matched_count"] == 0:
            raise NotFoundError(code="not_found", message="")
        elif result["modified_count"] == 0:
            raise BusinessRuleError(code="there_is_no_change", message="")

        result = self.__organization_repository.get_single(predicate={"_id": ObjectId(_id)})
        return self.organization_dict(result)

    def delete(self, _id):
        result = self.__organization_repository.remove(predicate={"_id": ObjectId(_id)})
        if result == 0:
            raise NotFoundError(code="not_found", message="")
        return True

from src.services.base_service import BaseService
from src.repositories.title_repository import TitleRepository
from src.schemas.title_schema import TitleCollectionSchema
from src.commons.exceptions import ServiceError, NotFoundError, ExistError
from src.utils.datetime_util import get_utc_datetime
from bson import ObjectId

class TitleService(BaseService):
    def __init__(self):
        super().__init__()
        self.__title_repository = TitleRepository()

    def title_dict(self, title):
        title = TitleCollectionSchema().dump(title)

        return title

    def get_all(self):
        items = self.__title_repository.get_all()

        if not items:
            raise NotFoundError(code="not_found", message="")

        title_list = []
        for title in items:
            title_list.append(self.title_dict(title))

        return title_list

    def add(self, schema):
        exist = self.__title_repository.get_single(predicate={"title": schema["title"]})
        if exist:
            raise ExistError(code="already_exists", message="")
        schema["status"] = True
        schema["created_at"] = get_utc_datetime()
        result = self.__title_repository.add(schema)

        if not result["acknowledged"]:
            raise ServiceError(code="system_error", message="Failed to add title")

        schema["_id"] = result["inserted_id"]

        return self.title_dict(schema)

    def get(self, _id):
        result = self.__title_repository.get_single_by_id(_id)
        if result is None:
            raise NotFoundError(code="not_found", message="")
        return self.title_dict(result)

    def edit(self, _id, schema):
        result = self.__title_repository.edit(predicate={"_id": ObjectId(_id)}, value=schema)

        if result["matched_count"] == 0:
            raise NotFoundError(code="not_found", message="")
        elif result["modified_count"] == 0:
            raise ServiceError(code="there_is_no_change", message="")

        result = self.__title_repository.get_single_by_id(_id)
        return self.title_dict(result)

    def delete(self, _id):
        result = self.__title_repository.remove(predicate={"_id": ObjectId(_id)})
        if result == 0:
            raise NotFoundError(code="not_found", message="")
        return True
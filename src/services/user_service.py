from src.services.base_service import BaseService
from src.schemas.user_schema import UserCollectionSearchSchema
from src.repositories.user_repository import UserRepository
from src.repositories.role_repository import RoleRepository

from src.commons.exceptions import NotFoundError, ServiceError, BusinessRuleError
from src.utils.hash_util import generate_password, hash_bcrypt
from src.utils.datetime_util import get_utc_datetime
from bson import ObjectId

class UserService(BaseService):

    def __init__(self):
        super().__init__()
        self.__user_repository = UserRepository()
        self.__role_repository = RoleRepository()

    def get_all(self, predicate=None, pagination=None):
        skip = (pagination["page"] - 1) * pagination["items_per_page"]
        limit = pagination["items_per_page"]
        sort = pagination["sort"]
        users = self.__user_repository.get_all(predicate={"status": True}, skip=skip, limit=limit, sort=sort)
        if not users:
            raise NotFoundError(code="not_found", message="")

        user_list = []


        for user in users:
            user_list.append(self.user_dict(user))

        return user_list


    def user_dict(self, user):
        user = UserCollectionSearchSchema().dump(user)

        return user

    def add(self, schema):
        password = generate_password()
        print(password)

        schema["password"] = hash_bcrypt(password)
        schema["role_id"] = RoleRepository().get_single({"title": "user"})["_id"]
        schema["status"] = True
        schema["created_at"] = get_utc_datetime()
        schema["first_login"] = True


        result = self.__user_repository.add(schema)
        if not result["acknowledged"]:
            raise ServiceError(code="internal_error", message="User can not be created")
        # TODO send password with email using celery tasks
        # self.send_email(schema["email"], password)
        schema["_id"] = result["inserted_id"]
        return self.user_dict(schema)


    def get(self, _id):
        user = self.__user_repository.get_single_by_id(_id)
        if not user:
            raise NotFoundError(code="not_found", message="")

        return self.user_dict(user)

    def edit(self, _id, schema):
        result = self.__user_repository.edit({"_id": ObjectId(_id)}, schema)
        if result["matched_count"] == 0:
            raise NotFoundError(code="not_found", message="User not found")
        elif result["modified_count"] == 0:
            raise BusinessRuleError(code="there_is_no_change", message="")

        user = self.__user_repository.get_single_by_id(_id)
        return self.user_dict(user)

    def delete(self, _id):
        result = self.__user_repository.remove({"_id": ObjectId(_id)})
        if result == 0:
            raise NotFoundError(code="not_found", message="User not found")
        return True


import time
import datetime
from bson import ObjectId
from flask_injector import inject
from src.services.base_service import BaseService

from src.repositories.user_repository import UserRepository
from src.repositories.organization_repository import OrganizationRepository
from src.repositories.role_repository import RoleRepository
from src.repositories.unit_repository import UnitRepository

from src.commons.exceptions import NotFoundError, BusinessRuleError

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from flask import current_app as app

class AuthService(BaseService):
    @inject
    def __init__(self):
        super().__init__()
        self.__user_repository = UserRepository()
        self.__organization_repository = OrganizationRepository()
        self.__role_repository = RoleRepository()
        self.__unit_repository = UnitRepository()

    def login(self, schema):
        user = self.__get_user(schema=schema)
        organization = self.__get_organization(user['organization_id'])
        unit = self.__get_unit(user['unit_id'])
        role = self.__get_user_role(user['role_id'])

        now_time = int(time.time())
        exp_time = int(organization["support_end_date"].timestamp())
        if now_time > exp_time:
            raise BusinessRuleError(code="organization.demo.end", message="Organization Expired")

        result = self.__create_token(user=user, organization=organization, unit=unit, role=role)
        return result


    def __get_user(self, schema):
        result = self.__user_repository.get_single({"email": schema['email']})
        if not result:
            raise NotFoundError(code="user.not_found", message="User not found")

        # if not check_bcrypt(password=schema["password"], password_hash=result['password']):
        #     raise NotFoundError(code="user.not_found", message="User not found")

        if not result['status']:
            raise BusinessRuleError("module.user.status", "User status is not active")

        return result

    def __get_organization(self, _id: ObjectId):
        result = self.__organization_repository.get_single(predicate={"_id": _id})
        if not result:
            raise BusinessRuleError("module.user.organization", "Organization assignment not found in user")
        return result

    def __get_unit(self, _id: ObjectId):
        result = self.__unit_repository.get_single(predicate={"_id": _id})
        if not result:
            raise BusinessRuleError("module.user.unit", "Unit assignment not found in user")
        return result

    def __get_user_role(self, _id: ObjectId):
        result = self.__role_repository.get_single(predicate={"_id": _id})
        if not result:
            raise BusinessRuleError("module.user.role", "Role assignment not found in user")
        return result

    @staticmethod
    def __token_expires_delta():
        days = app.config["API_EXPIRE_TOKEN"]
        return datetime.timedelta(days=int(days))

    def __create_token(self, user, organization, unit, role):
        expires_delta = self.__token_expires_delta()
        access_token = create_access_token(identity= str(user["_id"]),
                                           additional_claims={
                                                "organization_id": str(organization["_id"]),
                                                "organization_title": organization["title"],

                                                "unit_id": str(unit["_id"]),
                                                "unit_title": str(unit["title"]),

                                                "is_demo" : organization["is_demo"],

                                                "email": user['email'],
                                                "name": user['name'],
                                                "surname": user['surname'],

                                                "role_id": str(role["_id"]),
                                                "role_title": role["title"],
                                                "roles": role['roles'],

                                                "manager_user_id" : str(user["manager_user_id"]),
},
                                           expires_delta=expires_delta)
        refresh_token = create_refresh_token(identity=str(user['_id']),
                                             expires_delta=expires_delta)

        token = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return token

    def refresh_access_token(self):
        user_id = get_jwt_identity()
        user = self.__user_repository.get_single_by_id(user_id)
        organization = self.__get_organization(user['organization_id'])
        unit = self.__get_unit(user['unit_id'])
        role = self.__get_user_role(user['role_id'])

        now_time = int(time.time())
        exp_time = int(organization["support_end_date"].timestamp())
        if now_time > exp_time:
            raise BusinessRuleError(code="organization.demo.end", message="Organization Expired")

        expires_delta = self.__token_expires_delta()
        token = create_access_token(identity= str(user["_id"]),
                                                    additional_claims={
                                                    "organization_id": str(organization["_id"]),
                                                    "organization_title": organization["title"],

                                                    "unit_id": str(unit["_id"]),
                                                    "unit_title": str(unit["title"]),

                                                    "is_demo": organization["is_demo"],

                                                    "email": user['email'],
                                                    "name": user['name'],
                                                    "surname": user['surname'],

                                                    "role_id": str(role["_id"]),
                                                    "role_title": role["title"],
                                                    "roles": role['roles'],

                                                    "manager_user_id": str(user["manager_user_id"]),
                                                },
                                                expires_delta=expires_delta)
        refresh_token = create_refresh_token(identity=str(user['_id']),
                                             expires_delta=expires_delta)
        result = {
            "access_token": token,
            "refresh_token": refresh_token,
        }
        return result

    @staticmethod
    def logout():
        return True
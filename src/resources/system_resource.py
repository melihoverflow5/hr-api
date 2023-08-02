from injector import inject

from src.commons.response import ok_result
from src.resources.base_resource import BaseResource
from src.services.system_service import SystemService


class SystemPingResource(BaseResource):
    @inject
    def __init__(self, __system_service: SystemService):
        super().__init__()
        self.__system_service = __system_service

    def get(self):
        result = self.__system_service.ping()
        return ok_result(data=result)

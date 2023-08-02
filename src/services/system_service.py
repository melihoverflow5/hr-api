import platform

from injector import inject

from src.services.base_service import BaseService



class SystemService(BaseService):
    @inject
    def __init__(self):
        super().__init__()

    def ping(self):
        cache_check = True
        db_check = self.__db_check()
        system_check = self.__system_check()
        check = False
        if cache_check and db_check and system_check:
            check = True

        result = {"cache_check": cache_check,
                  "db_check": db_check,
                  "system_check": system_check,
                  "check": check}
        return result


    @staticmethod
    def __db_check():
        output = True
        try:
            pass
            #db.session.execute('SELECT 1')
        except Exception as e:
            output = str(e)
        return output

    @staticmethod
    def __system_check():
        output = True
        try:
            check = platform.system()
            if check:
                output = True
        except Exception as e:
            output = str(e)
        return output

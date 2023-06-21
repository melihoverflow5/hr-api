import functools

from flask_jwt_extended import get_jwt_identity, get_jwt
from src.commons.response import bad_request_result
from src.commons.exceptions import SystemStatusError
from src.utils.datetime_util import now_timestamp

def authorize(_func=None, *, roles: list, rule: str = "any"):
    def decorator_auth(func):
        @functools.wraps(func)
        def wrapper_auth(*args, **kwargs):
            jwt = get_jwt()

            if rule not in ["all", "any"]:
                return bad_request_result(code="all/any", message="all yada any kullanilmali...")

            auth_roles = sorted(roles)
            for auth_role in auth_roles:
                if auth_role not in jwt["roles"]:
                    return bad_request_result(code="all", message="Kullanicinin rolu uygun degil...")

            # now_datetime = now_timestamp()
            # if jwt["support_end_date"] <= now_datetime:
            #     raise SystemStatusError(code="api_message.auth.support_end_date", message="Support end date")

            return func(*args, **kwargs)

        return wrapper_auth

    if _func is None:
        return decorator_auth
    else:
        return decorator_auth(_func)
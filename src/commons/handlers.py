import ast
import json
import traceback
import jsonschema
import marshmallow
# import redis
# from os import environ
from src.commons.exceptions import ArgumentNullError, ArgumentEmptyError, ArgumentNullOrEmptyError, ExistError, \
    ValidationError, NotFoundError, BusinessRuleError, SystemStatusError, ForbiddenError
from src.commons.response import bad_request_result, conflict_result, not_found_result, internal_server_error_result, \
    unauthorized_result, forbidden_result, validation_result


def jwt_handlers_config(jwt):
    @jwt.expired_token_loader
    def my_expired_token_callback(a,b):
        return unauthorized_result(
            code="handler.jwt.expired_token_loader",
            message="Erişim süresi doldu"
        )

    # Setup our redis connection for storing the blocklisted tokens. You will probably
    # want your redis instance configured to persist data to disk, so that a restart
    # does not cause your application to forget that a JWT was revoked.
    #redis_instance = redis.StrictRedis.from_url(environ.get('REDIS_URL'))

    # Callback function to check if a JWT exists in the redis blocklist
    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        return False
        jti = jwt_payload["jti"]
        token_in_redis = redis_instance.get('token:'+str(jti))
        if token_in_redis:
            return False
        return True

    @jwt.invalid_token_loader
    def my_invalid_token_loader(e):
        return unauthorized_result(
            code="handler.jwt.invalid_token_loader",
            message="Token hatalı",
            description=str(e)
        )

    @jwt.unauthorized_loader
    def my_unauthorized_loader(fp):
        return unauthorized_result(
            code="handler.jwt.unauthorized_loader",
            message="Yetki dışı erişim",
            description=str(fp)
        )

    @jwt.needs_fresh_token_loader
    def my_needs_fresh_token_loader():
        return unauthorized_result(
            code="handler.jwt.needs_fresh_token_loader",
            message="Token yenilenmeli"
        )


# default exception türlerinin handle işlemi
def response_handlers_config(app):
    @app.errorhandler(400)
    def bad_request_error_handler(ex):
        return ex, 400

    @app.errorhandler(404)
    def not_found_error_handler(ex):
        return ex, 404

    @app.errorhandler
    def default_error_handler(ex):
        return ex, 500


# custom exception türlerinin flask ile birleştirilmesi
def exception_handlers_config(app):
    @app.errorhandler(ArgumentNullError)
    def argument_null_error_handler(error):
        return bad_request_result(
            code=error.code,
            message=str(error),
        )

    @app.errorhandler(ArgumentEmptyError)
    def argument_empty_error_handler(error):
        return bad_request_result(
            code=error.code,
            message=str(error),
        )

    @app.errorhandler(ArgumentNullOrEmptyError)
    def argument_null_or_empty_error_handler(error):
        return bad_request_result(
            code=error.code,
            message=str(error),
        )

    @app.errorhandler(ExistError)
    def exist_error_handler(error):
        return conflict_result(
            code=error.code,
            message=str(error),
        )

    @app.errorhandler(ValidationError)
    def validation_error_handler(error):
        return bad_request_result(
            code=error.code,
            message=str(error),
        )

    @app.errorhandler(NotFoundError)
    def not_found_error_handler(error):
        return not_found_result(
            code=error.code,
            message=str(error),
        )

    @app.errorhandler(ForbiddenError)
    def forbidden_handler(error):
        return forbidden_result(
            code=error.code,
            message=str(error),
        )

    @app.errorhandler(SystemStatusError)
    def system_status_error_handler(error):
        return forbidden_result(
            code=error.code,
            message=str(error),
        )

    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_rule_error_handler(error):
        error = json.dumps(ast.literal_eval(str(error)))
        error = json.loads(error)
        return validation_result(
            code="handler.exception.validation_error",
            message=error
        )

    @app.errorhandler(BusinessRuleError)
    def business_rule_error_handler(error):
        return bad_request_result(
            code=error.code,
            message=str(error),
        )

    # handle edilmemiş tüm exception için handle methodu
    @app.errorhandler(Exception)
    def all_exception_handler(error):
        print(traceback.format_exc())
        return internal_server_error_result(
            code="handler.exception.internal_server_error",
            message=str(error),
            description=str('null')
        )


# şema validasyonları için custom handler
def json_schema_handlers_config(app):
    @app.errorhandler(jsonschema.ValidationError)
    def on_validation_error_handler(e):
        return bad_request_result(
            code="VALIDATION_ERROR",
            message=str(e),
        )

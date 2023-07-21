from src.schemas.base_schema import default_error_messages, BaseSchema

from marshmallow import fields, validate, EXCLUDE

class PaginationSchema(BaseSchema):
    page = fields.Int(
        required=False,
        validate=[validate.Range(min=0, max=100000)],
        allow_none=False,
        default=1,
        error_messages=default_error_messages
    )

    items_per_page = fields.Int(
        required=False,
        validate=[validate.Range(min=0, max=100000)],
        allow_none=False,
        default=5,
        error_messages=default_error_messages
    )

    sort = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )
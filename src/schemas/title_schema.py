from src.schemas.base_schema import default_error_messages, BaseSchema
from marshmallow import fields, validate
class TitleCollectionSchema(BaseSchema):
    _id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    title = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    level = fields.Float(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    status = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages,
    )

    created_at = fields.DateTime(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

class TitleCollectionSearchSchema(BaseSchema):
    _id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    title = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    level = fields.Int(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    status = fields.Bool(
        required=False,
        default=True,
        error_messages=default_error_messages,
    )

    created_at = fields.DateTime(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

from src.schemas.base_schema import default_error_messages, BaseSchema
from marshmallow import fields, validate

class OrganizationCollectionSchema(BaseSchema):
    title = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    description = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    status = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages,
    )

    is_demo = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages,
    )

    features = fields.Dict(
        required=False,
        allow_none=False,
        error_messages=default_error_messages,
    )

    support_end_date = fields.Date(
        required=False,
        allow_none=False,
        error_messages=default_error_messages,
    )

    organization_logo = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages,
    )

class OrganizationCollectionSearchSchema(BaseSchema):
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

    description = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    status = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages,
    )

    is_demo = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages,
    )

    features = fields.Dict(
        required=False,
        allow_none=False,
        error_messages=default_error_messages,
    )

    support_end_date = fields.Date(
        required=False,
        allow_none=False,
        error_messages=default_error_messages,
    )

    organization_logo = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages,
    )

    created_at = fields.DateTime(
        required=False,
        allow_none=False,
        error_messages=default_error_messages,
    )
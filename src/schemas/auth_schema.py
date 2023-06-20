from marshmallow import Schema, fields, validate

from src.schemas.base_schema import BaseSchema, default_error_messages

class AuthLoginSchema(BaseSchema):
    email = fields.Str(
        required=True,
        allow_none=True,
        validate=[validate.Length(min=3, max=100)],
        error_messages=default_error_messages
    )

    password = fields.Str(
        required=True,
        validate=[validate.Length(min=6, max=100)],
        allow_none=False,
        error_messages=default_error_messages
    )
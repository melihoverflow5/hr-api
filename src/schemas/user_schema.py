from marshmallow import fields, EXCLUDE

from src.schemas.base_schema import default_error_messages, BaseSchema

class UserCollectionSchema(BaseSchema):
    _id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    jira_id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    email = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    password = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    name = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    surname = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    organization_id = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    role_id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    address = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    birth_date = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    gender = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    manager_user_id = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    title_id = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    unit_id = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    phone_number = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

    profile_pic = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    first_login = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages
    )

    status = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages,
    )


class UserCollectionSearchSchema(BaseSchema):
    _id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    jira_id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )
    
    email = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    password = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    name = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    surname = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    organization_id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    role_id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    address = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    birth_date = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    gender = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    manager_user_id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    title_id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    unit_id = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    phone_number = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    profile_pic = fields.Str(
        required=False,
        allow_none=False,
        error_messages=default_error_messages
    )

    first_login = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages
    )

    status = fields.Bool(
        required=False,
        allow_none=False,
        default=True,
        error_messages=default_error_messages,
    )
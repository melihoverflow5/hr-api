from src.schemas.base_schema import BaseSchema, default_error_messages
from marshmallow import fields, validate

class JiraSchema(BaseSchema):
    jira_username = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )
    jira_api_key = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )
    jira_cloud = fields.Bool(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )
    jira_url = fields.Str(
        required=True,
        allow_none=False,
        error_messages=default_error_messages
    )

class JiraUpdateSchema(BaseSchema):
    jira_username = fields.Str(
        required=False,
        allow_none=True,
        error_messages=default_error_messages
    )
    jira_api_key = fields.Str(
        required=False,
        allow_none=True,
        error_messages=default_error_messages
    )
    jira_cloud = fields.Str(
        required=False,
        allow_none=True,
        error_messages=default_error_messages
    )
    jira_url = fields.Str(
        required=False,
        allow_none=True,
        error_messages=default_error_messages
    )
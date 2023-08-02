from src.resources.auth_resource import AuthLoginResource, AuthLoginUserResource, SSOResource
from src.resources.organization_resource import OrganizationCollectionResource, OrganizationItemColletionResource
from src.resources.user_resource import UserCollectionResource, UserCollectionItemResource
from src.resources.title_resource import TitleCollectionResource, TitleCollectionItemResource
from src.resources.jira_resource import JiraCollectionResource, JiraItemCollectionResource, JiraUserCollectionResource

def routes_config(api):
    api.add_resource(AuthLoginResource, '/auth/login')
    api.add_resource(AuthLoginUserResource, '/auth/get-user')
    api.add_resource(SSOResource, '/auth/sso')

    api.add_resource(OrganizationCollectionResource, '/organizations')
    api.add_resource(OrganizationItemColletionResource, '/organizations/<string:_id>')

    api.add_resource(UserCollectionResource, '/users')
    api.add_resource(UserCollectionItemResource, '/users/<string:_id>')

    api.add_resource(TitleCollectionResource, '/titles')
    api.add_resource(TitleCollectionItemResource, '/titles/<string:_id>')

    api.add_resource(JiraCollectionResource, '/jira')
    api.add_resource(JiraItemCollectionResource, '/jira/<string:jira_id>')
    api.add_resource(JiraUserCollectionResource, '/jira/users')

    api.add_resource(SystemPingResource, "/system/ping")
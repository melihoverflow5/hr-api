from src.resources.auth_resource import AuthLoginResource, AuthLoginUserResource
from src.resources.organization_resource import OrganizationCollectionResource
from src.resources.organization_resource import OrganizationItemColletionResource

def routes_config(api):
    api.add_resource(AuthLoginResource, '/auth/login')
    api.add_resource(AuthLoginUserResource, '/auth/get-user')

    api.add_resource(OrganizationCollectionResource, '/organizations')
    api.add_resource(OrganizationItemColletionResource, '/organizations/<string:_id>')

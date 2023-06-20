from src.resources.auth_resource import AuthLoginResource
def routes_config(api):
    api.add_resource(AuthLoginResource, '/auth/login')
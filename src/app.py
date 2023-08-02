from flask import Flask, request, g
from flask_restful import Api
from src.routes import routes_config
from src.injects import injects_config
from src.commons.handlers import jwt_handlers_config, response_handlers_config, exception_handlers_config, json_schema_handlers_config
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    jwt = JWTManager(app)
    jwt_handlers_config(jwt)

    api = Api(app)
    routes_config(api)
    injects_config(app)
    exception_handlers_config(app)
    response_handlers_config(app)
    exception_handlers_config(app)
    json_schema_handlers_config(app)


    @app.before_request
    def db_provider():
        db = request.headers['Host'].split('.')[0]
        # test connection
        if db == "127" or db == "localhost":
            db = "test"
        g.database = db
        # print(g.database)

    return app


app = create_app()



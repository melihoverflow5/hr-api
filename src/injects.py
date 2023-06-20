from flask_injector import FlaskInjector

def injects_config(app):
    def configure(binder):
        pass

    FlaskInjector(app=app, modules=[configure])
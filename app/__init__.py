from flask import Flask
from .context_injectors import inject_globals, inject_dummy_products


def create_app():
    app = Flask(
        __name__,
        static_folder='../static',  # make sure path points to your project static/
        template_folder='../templates'
    )
    app.config.from_object("config.Config")

    from app.routes.home import home_bp

    app.register_blueprint(home_bp)

    app.context_processor(inject_dummy_products)

    return app
from flask import Flask
from .extensions import db, login_manager
from .context_injectors import inject_globals, inject_dummy_products
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

csrf = CSRFProtect()  # just create it here
migrate = Migrate()
def create_app():
    app = Flask(
        __name__,
        static_folder='../static',  # make sure path points to your project static/
        template_folder='../templates'
    )
    app.config.from_object("config.Config")

    # 3. Import models so SQLAlchemy/Alembic knows they exist
    from . import models

    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)  # Connects Migrate to App and DB

    from app.routes.home import home_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    app.context_processor(inject_dummy_products)

    return app
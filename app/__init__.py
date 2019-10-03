from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from app.core import bp as core_bp

    app.register_blueprint(core_bp)

    return app


from app import models

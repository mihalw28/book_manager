from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.core import bp as core_bp

    app.register_blueprint(core_bp)

    return app


from app import models

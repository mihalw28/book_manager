import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "very-difficult-random-bstring"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = to be detailed
    DEBUG = False
    Testing = False

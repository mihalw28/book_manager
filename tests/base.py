from flask_testing import TestCase
from config import TestingConfig
from flask import current_app
from app import create_app, db


class TestBase(TestCase):
    def create_app(self):
        app = create_app(TestingConfig)
        with app.app_context():
            current_app.test_client()
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

import os
import unittest

from flask import current_app
from flask_testing import TestCase
from tests.base import TestBase

from app import create_app

basedir = os.path.abspath(os.path.dirname(__file__))


class TestTestingConfig(TestBase):
    def test_app_is_testing(self):
        """
        Test that app is running in testing config.
        """
        app = create_app()
        app.config.from_object("config.TestingConfig")
        self.assertTrue(app.config["TESTING"])
        self.assertTrue(app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite://")


class TestDevelopmentConfig(TestBase):
    def test_app_is_development(self):
        """
        Test that app is in development config.
        """
        app = create_app()
        app.config.from_object("config.DevelopmentConfig")
        self.assertFalse(app.config["TESTING"])
        self.assertTrue(app.config["DEBUG"])
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
            or "sqlite:///" + os.path.join(basedir, "app.db")
        )


if __name__ == "__main__":
    unittest.main()

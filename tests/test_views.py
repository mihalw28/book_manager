import unittest

from flask import url_for

from tests.base import TestBase
from tests.helper import add_book


class TestViews(TestBase):
    def test_home_page(self):
        """
        Test home page behavior.
        """
        response = self.client.get(url_for("core.index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    def test_add_book_page(self):
        """
        Test add_book page behavior.
        """
        response = self.client.get(url_for("core.add_book"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Number of pages", response.data)
        self.assertIn(b"Add book", response.data)
        self.assertIn(b"Add to library", response.data)

    def test_all_book_page(self):
        """
        Test all_books page behavior.
        """
        add_book("Epic Book", "Famous Writer", "Amazing book...", 5)
        response = self.client.get(url_for("core.all_books"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"List of all books", response.data)
        self.assertIn(b"Epic Book", response.data)
        self.assertIn(b"Amazing book", response.data)


if __name__ == "__main__":
    unittest.main()

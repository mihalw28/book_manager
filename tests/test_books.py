import datetime
import unittest

from app import db
from app.models import Book
from tests.base import TestBase

book = Book(
    title="For whom the bell tolls",
    author="Ernest Hemingway",
    description="A novel by Ernest...",
    pages_no=357,
)
book1 = Book(
    title="The almost nearly perfect people",
    author="Michael Booth",
    description="A witty, informative, and popular travelogue about the Scandinavian countries...",
    pages_no=400,
)
book2 = Book(
    title="A short history of nearly everything",
    author="Bill Bryson",
    description="One of the world’s most beloved...",
    pages_no=544,
)
book3 = Book(
    title="Pan Tadeusz",
    author="Adam Mickiewicz",
    description="The polish national epic opus...",
    pages_no=234,
)


class TestBookModel(TestBase):
    def test_books(self):
        """
        Test book model.
        """
        self.assertEqual(book.title, "For whom the bell tolls")
        self.assertEqual(book.author, "Ernest Hemingway")
        self.assertEqual(book.description, "A novel by Ernest...")
        self.assertEqual(book.pages_no, 357)

    def test_date(self):
        """
        Test that added_date returned by add_date() method is today's date.
        """
        book.add_date()
        self.assertEqual(book.added_date, datetime.date.today())

    def test_number_of_records(self):
        """
        Test number of records in database.
        """
        db.session.add_all([book1, book2, book3])
        db.session.commit()
        self.assertEqual(Book.query.count(), 3)


if __name__ == "__main__":
    unittest.main()

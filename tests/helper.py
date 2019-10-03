from app import db
from app.models import Book


def add_book(title, author, description, pages_no):
    """Helper function for adding example book to db."""
    book = Book(title=title, author=author, description=description, pages_no=pages_no)
    book.add_date()
    db.session.add(book)
    db.session.commit()
    return book

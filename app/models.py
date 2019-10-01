from app import db
import datetime


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    pages_no = db.Column(db.Integer, nullable=False)
    added_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.title})>"

    def __str__(self):
        return f"{self.title}"

    def add_date(self):
        self.added_date = datetime.date.today()

import datetime

from app import db


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    pages_no = db.Column(db.String(5), nullable=False)
    added_date = db.Column(db.DateTime)
    link_generation_time = db.Column(db.DateTime, nullable=True)
    link_token = db.Column(db.String(20), unique=True, nullable=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.title})>"

    def __str__(self):
        return f"{self.title}"

    def add_date(self):
        self.added_date = datetime.date.today()

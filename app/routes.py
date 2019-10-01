from flask import flash, redirect, render_template, url_for

from app import app, db
from app.forms import AddBookForm
from app.models import Book


@app.route("/")
@app.route("/index")
def index():
    """Function for rendering template on 2 priary routes."""
    return render_template("index.html", title="Home")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    """Function adds book to database."""
    form = AddBookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            description=form.description.data,
            pages_no=form.pages_no.data,
        )
        book.add_date()
        db.session.add(book)
        db.session.commit()
        flash(f"The book {form.title.data} has been added to the library.")
        return redirect(url_for("index"))
    return render_template("add_book.html", title="Add Book", form=form)

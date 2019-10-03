import datetime
import uuid

from flask import flash, redirect, render_template, request, session, url_for

from app import db
from app.core import bp
from app.core.forms import AddBookForm, UpdateBookForm
from app.models import Book


@bp.route("/")
@bp.route("/index")
def index():
    """Function for rendering template on 2 priary routes."""
    return render_template("index.html", title="Home")


@bp.route("/add_book", methods=["GET", "POST"])
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
        return redirect(url_for("core.all_books"))
    return render_template("add_book.html", title="Add Book", form=form)


@bp.route("/all_books", methods=["GET", "POST"])
def all_books():
    """Function returns all books from database."""
    books = Book.query.all()
    return render_template("all_books.html", title="All books", books=books)


@bp.route("/delete_book", methods=["POST"])
def delete_book():
    """After click on button function deletes book from db"""
    if request.method == "POST":
        bk_id = request.form.get("id", type=int)
        book_to_del = Book.query.filter_by(id=bk_id).first()
        db.session.delete(book_to_del)
        db.session.commit()
    flash(f"The book {book_to_del.title} has been deleted.")
    return redirect(url_for("core.all_books"))


@bp.route("/update_book", methods=["GET", "POST"])
def update_book():
    """After click on button function renders form to update book."""
    id_from_session = session["book_id"]
    book = Book.query.filter_by(id=id_from_session).first()
    form = UpdateBookForm()
    if form.validate_on_submit():
        form.populate_obj(book)  # from WTForms docs
        db.session.commit()
        flash(f"The book {book.title} has been updated.")
        return redirect(url_for("core.all_books"))
    form.title.data = book.title
    form.author.data = book.author
    form.description.data = book.description
    form.pages_no.data = book.pages_no
    return render_template("update_book.html", title="Update Book", form=form)


@bp.route("/view_book", methods=["GET", "POST"])
def view_book():
    """On click button function renders particular book view."""
    if request.method == "POST":
        bk_id = request.form.get("id", type=int)
        book = Book.query.filter_by(id=bk_id).first()
        session["book_id"] = book.id
    return render_template("view_book.html", title="View", book=book)


@bp.route("/book/<int:id>/<string:token>", methods=["GET"])
def render_book_preview(id, token):
    """Renders preview of book from link."""
    book = Book.query.filter_by(id=id).first()
    if (
        book.link_generation_time + datetime.timedelta(days=0, seconds=300)
        < datetime.datetime.utcnow()
    ) or token != book.link_token:
        return redirect(url_for("core.error"))
    return render_template("link_book.html", title="Link book", book=book)


@bp.route("/generate_link", methods=["GET", "POST"])
def generate_link():
    """On click button function generates link for single entry."""
    if request.method == "POST":
        bk_id = request.form.get("id", type=int)
        book = Book.query.filter_by(id=bk_id).first()
        book.link_generation_time = datetime.datetime.utcnow()
        # Not necessary to create UUID object, string is enough
        token = str(uuid.uuid4())[-12:]  # dozen-sign token
        book.link_token = token
        db.session.commit()
        link = f"{request.host_url}book/{book.id}/{book.link_token}"
    return render_template("view_book.html", title="View", book=book, link=link)


@bp.route("/error")
def error():
    """Renders timeout_error template."""
    return render_template("timeout_error.html", title="Error")

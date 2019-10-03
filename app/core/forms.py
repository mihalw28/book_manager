from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Regexp


class AddBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    pages_no = StringField(
        "Number of pages",
        validators=[
            InputRequired(),
            Regexp(
                regex=r"^[1-9]+$",
                message="Digits only. Number of pages must be a number greater than zero.",
            ),
        ],
    )
    submit = SubmitField("Add to library")


class UpdateBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    pages_no = StringField(
        "Number of pages",
        validators=[
            InputRequired(),
            Regexp(
                regex=r"^[1-9]+$",
                message="Digits only. Number of pages must be a number greater than zero.",
            ),
        ],
    )
    submit = SubmitField("Update book")

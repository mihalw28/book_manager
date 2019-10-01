from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class AddBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    pages_no = IntegerField("Number of pages")
    submit = SubmitField("Add to library")

    def validate_pages_no(self, pages_no):
        """Method validates if number of pages is a positive one."""
        if pages_no.data < 1:
            raise ValidationError("A book cannot have less than 1 page.")

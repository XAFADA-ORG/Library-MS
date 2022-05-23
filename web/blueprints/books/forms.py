
# form for creating and updating books
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

from web.blueprints.books.models import Books


class BooksForm(FlaskForm):
    # checks if book already exists
    def validate_title(self, title_to_check):
        book = Books.query.filter_by(title=title_to_check.data).first()
        if book:
            raise ValidationError('Book already exists')

    title = StringField(label='Title', validators=[ DataRequired()])
    isbn = StringField(label='ISBN', validators=[DataRequired()])
    author = StringField(label='Author', validators=[ DataRequired()])
    stock = IntegerField(label='Stock', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
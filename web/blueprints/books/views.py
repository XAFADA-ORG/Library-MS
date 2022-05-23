from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.books.forms import BooksForm
from web.blueprints.books.models import Books
from web.extensions import save_to_db, db

blueprint = ProjectBlueprint('books', __name__)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add():
    form = BooksForm()
    if form.validate_on_submit():
        data = Books()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your Book has been created', 'success')
        return redirect(url_for('books.index'))
    return render_template('books/add.html', title='Books', form=form)


@blueprint.route(blueprint.url)
def index():
    form = BooksForm()
    if form.validate_on_submit():
        book_to_create = Books(title=form.title.data,
                               isbn=form.isbn.data,
                               author=form.author.data,
                               stock=form.stock.data,
                               borrow_stock=form.stock.data)
        db.session.add(book_to_create)
        db.session.commit()
        flash('Successfully create a book', category="success")
    return render_template('books/index.html', title='books')

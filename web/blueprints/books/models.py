from web.extensions import db


class Books(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    isbn = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    stock = db.Column(db.Integer(), default=0)
    borrow_stock = db.Column(db.Integer(), default=0)
    member_count = db.Column(db.Integer(), default=0)
    returned = db.Column(db.Boolean(), default=False)

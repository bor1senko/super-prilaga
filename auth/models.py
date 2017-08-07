from ext import db
from util import CRUDMixin


class User(CRUDMixin, db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(32))
    username = db.Column(db.String(32), unique=True, index=True)
    password = db.Column(db.String(64))
    level = db.Column(db.Integer)
    progress = db.Column(db.Integer)

    def __init__(self, name, color, note):
        self.color = color
        self.note = note
        self.name = name

    def __repr__(self):
        return u'<Spiner> {}'.format(self.name)

    def __str__(self):
        return self.name

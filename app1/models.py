from ext import  db
from util import CRUDMixin

class Spiner(CRUDMixin, db.Model):
    name = db.Column(db.String(32))
    color = db.Column(db.String(50))
    note = db.Column(db.Text)

    def __init__(self, name, color, note):
        self.color = color
        self.note = note
        self.name = name

    def __repr__(self):
        return u'<Spiner> {}'.format(self.name)

    def __str__(self):
        return self.name
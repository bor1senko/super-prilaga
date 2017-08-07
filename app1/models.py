from ext import db
from util import CRUDMixin


class Spiner(CRUDMixin, db.Model):
    name = db.Column(db.String(32))
    color = db.Column(db.String(50))
    note = db.Column(db.Text)
    image = db.Column(db.String(300))
    css = db.Column(db.Text)
    rotation_time = db.Column(db.DateTime)

    def __init__(self, name, color, note, image, css=None, rotation_time=None):
        self.color = color
        self.note = note
        self.name = name
        self.css = css
        self.image = image
        self.rotation_time = rotation_time

    def __repr__(self):
        return u'<Spiner> {}'.format(self.name)

    def __str__(self):
        return self.name

from ext import db


class CRUDMixin(object):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

    def update(self, commit=True, **kw):
        for key, value in kw.iteritems():
            setattr(self, key, value)
        return self.save() if commit else self

    @classmethod
    def create(cls, **kw):
        instance = cls(**kw)
        return instance.save()

from app import db


class Dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64), index=True)
    definition = db.Column(db.String(512))
    example1 = db.Column(db.String(256))
    example2 = db.Column(db.String(256))
    synonyms = db.Column(db.String(256))

    def __repr__(self):
        return '<Dictionary {}>.format(self.username)'

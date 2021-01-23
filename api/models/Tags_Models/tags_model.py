from api.models.model import db


class Tag(db.Model):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(25))

    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __repr__(self):
        return '<Tag %r>' % (self.id)

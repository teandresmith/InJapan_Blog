from api.models.model import db

db = db


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    message = db.Column(db.Text())

    def __init__(self, email, message):
        self.email = email
        self.message = message

    def __repr__(self):
        return '<Feedback %r>' % (self.id)

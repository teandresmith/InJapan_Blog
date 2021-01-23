from api.models.model import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'adminlist'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, username, password):
        self.username = username
        self.password = password

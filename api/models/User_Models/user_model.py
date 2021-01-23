from api.models.model import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'admintable'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, name, password):
        self.name = name
        self.password = password

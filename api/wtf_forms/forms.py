from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=4, max=200)])

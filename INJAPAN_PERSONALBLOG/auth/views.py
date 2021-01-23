from api.models.User_Models.user_model import User
from api.wtf_forms.forms import LoginForm
from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_user, logout_user
from api.models.Anime_model.anime_model import AnimeTable

auth_bp = Blueprint(
    'auth', __name__, template_folder='templates', static_folder='static')


# Any function with anime_list = AnimeTable.query.all()
# is to fufill layout template
# It is to automate the updating of a new feature of InJapanBlog
# Where it seeks the database for anime titles and
# using a for title to develop blocks


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for('auth.login_success'))

        else:
            error = 'Incorrect Credentials'

    return render_template('login.html', form=form, error=error)


@auth_bp.route('/success')
def login_success():
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    return render_template('success.html', anime_list=anime_list)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.home_page'))

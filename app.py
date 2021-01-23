from flask import Flask

from api.admin.admin_user.admin import admin
from api.admin.admin_user.admin_modelview import MyModelView, MyAdminIndexView
from api.admin.login.login import login
from api.mail.mail import mail
from api.models.model import db
from api.bootstrap.bootstrap import bootstrap
from INJAPAN_PERSONALBLOG.about.views import about_bp
from INJAPAN_PERSONALBLOG.anime.views import anime_bp
from INJAPAN_PERSONALBLOG.auth.views import auth_bp
from INJAPAN_PERSONALBLOG.blog.views import blog_bp
from INJAPAN_PERSONALBLOG.contact.views import contact_bp
from INJAPAN_PERSONALBLOG.home.views import home_bp
from INJAPAN_PERSONALBLOG.learn.views import learn_bp
from INJAPAN_PERSONALBLOG.travel.views import travel_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    bootstrap.init_app(app)

    ENV = 'prod'
    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2706@localhost/injapanblog'
    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pzcxxcnlqghjbh:489936ada34ffc352c7021983225a4f10c4296b00f617e00042dc4104d07a6e8@ec2-52-0-65-165.compute-1.amazonaws.com:5432/d8pmugs1aoqi0o'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    '#Creating mailing capabilities'
    app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '2ae67d66d3415d'
    app.config['MAIL_PASSWORD'] = '9f39fe71c5aa46'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    mail.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(learn_bp, url_prefix=('/learn'))
    app.register_blueprint(blog_bp, url_prefix='/blog')
    app.register_blueprint(about_bp, url_prefix='/about')
    app.register_blueprint(travel_bp, url_prefix='/travel')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(anime_bp, url_prefix='/anime')

    login.login_view = 'auth.login'
    login.init_app(app)

    from api.models.Blog_Model.blog_model import Blogs
    from api.models.Contact_Models.contact_model import Feedback
    from api.models.Tags_Models.tags_model import Tag
    from api.models.User_Models.user_model import User
    from api.models.Anime_model.anime_model import AnimeTable

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    admin.init_app(app, index_view=MyAdminIndexView())

    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Blogs, db.session))
    admin.add_view(MyModelView(Feedback, db.session))
    admin.add_view(MyModelView(Tag, db.session))
    admin.add_view(MyModelView(AnimeTable, db.session))

    return app

from flask import Flask
from api.model import db
from api.mail import mail
from INJAPAN_PERSONALBLOG.home.views import home_bp
from INJAPAN_PERSONALBLOG.learn.views import learn_bp
from INJAPAN_PERSONALBLOG.blog.views import blog_bp
from INJAPAN_PERSONALBLOG.about.views import about_bp
from INJAPAN_PERSONALBLOG.travel.views import travel_bp
from INJAPAN_PERSONALBLOG.contact.views import contact_bp


def create_app():
    app = Flask(__name__)

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

    return app




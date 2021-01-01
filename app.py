'This Python File uses Flask to render web pages'

from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2706@localhost/feedback'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pzcxxcnlqghjbh:489936ada34ffc352c7021983225a4f10c4296b00f617e00042dc4104d07a6e8@ec2-52-0-65-165.compute-1.amazonaws.com:5432/d8pmugs1aoqi0o'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'blogreport'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    message = db.Column(db.Text())

    def __init__(self, email, message):
        self.email = email
        self.message = message


@app.route('/')
def home():
    '''This function renders the home web page'''
    return render_template('home.html')


@app.route('/about')
def about():
    '''This function renders the about me web page'''
    return render_template('about.html')


@app.route('/resources/web_resources')
def web_resources():
    '''This function renderes the Resources web page'''
    return render_template('web_resources.html')


@app.route('/resources/common_phrases')
def common_phrases():
    '''This function renders the common phrases web page'''
    return render_template('common_phrases.html')


@app.route('/blog')
def blog():
    '''This function renders the blog web page'''
    return render_template('blog.html')


@app.route('/blog/first_post')
def first_blog():
    '''This function renders the first blog post web page'''
    return render_template('first_blog.html')


@app.route('/contact')
def contact():
    '''This function renders the contact web page'''
    return render_template('contact_us.html')


@app.route('/contact/submit', methods=['Get', 'POST'])
def contact_submit():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        if email == '' or message == '':
            return render_template('contact_us.html', error='Please fill in all fields')
        data = Feedback(email, message)
        db.session.add(data)
        db.session.commit()
        send_mail(email, message)
        return render_template('success.html')


if __name__ == '__main__':
    app.run()

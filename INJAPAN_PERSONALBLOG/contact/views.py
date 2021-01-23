from flask import Blueprint, render_template, request
from api.models.model import db
from api.models.Contact_Models.contact_model import Feedback
from api.mail.send_feedback import sendmail
from api.models.Anime_model.anime_model import AnimeTable

contact_bp = Blueprint('contact', __name__,
                       template_folder='templates', static_folder='static')

# Any function with anime_list = AnimeTable.query.all()
# is to fufill layout template
# It is to automate the updating of a new feature of InJapanBlog
# Where it seeks the database for anime titles and
# using a for title to develop blocks


@contact_bp.route('/')
def contact_page():
    '''This function renders the contact web page'''
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    return render_template('contact_us.html', anime_list=anime_list)


@contact_bp.route('/submit', methods=['POST'])
def contact_submit():
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        if email == '' or message == '':
            return render_template('contact_us.html', error='Please fill in all fields', anime_list=anime_list)
        data = Feedback(email, message)
        db.session.add(data)
        db.session.commit()
        sendmail(email, message)
        return render_template('successful_submission.html', anime_list=anime_list)

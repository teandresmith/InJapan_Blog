from flask import Blueprint, render_template, request
from api.model import db
from .contact_model import Feedback
from .send_feedback import sendmail

contact_bp = Blueprint('contact', __name__,
                       template_folder='templates', static_folder='static')


@contact_bp.route('/')
def contact_page():
    '''This function renders the contact web page'''
    return render_template('contact_us.html')


@contact_bp.route('/submit', methods=['POST'])
def contact_submit():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        if email == '' or message == '':
            return render_template('contact_us.html', error='Please fill in all fields')
        data = Feedback(email, message)
        db.session.add(data)
        db.session.commit()
        sendmail(email, message)
        return render_template('successful_submission.html')

from flask import render_template
from flask_mail import Message
from api.mail import mail


def sendmail(email, feedback):
    msg = Message(subject='Website Feedback', sender=email,
                  recipients=['InJapan@blog.com'])
    msg.html = render_template(
        'feedback_email.html', email=email, feedback=feedback)
    mail.send(msg)

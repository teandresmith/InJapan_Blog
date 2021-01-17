from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__,
                     template_folder='templates', static_folder='static')


@about_bp.route('/')
def about_page():
    '''This function renders the about me web page'''
    return render_template('about.html')

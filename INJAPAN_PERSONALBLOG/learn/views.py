from flask import Blueprint, render_template

learn_bp = Blueprint('learn', __name__,
                     template_folder='templates', static_folder='static')


@learn_bp.route('/resources/web_resources')
def web_resources():
    '''This function renderes the Resources web page'''
    return render_template('web_resources.html')


@learn_bp.route('/resources/common_phrases')
def common_phrases():
    '''This function renders the common phrases web page'''
    return render_template('common_phrases.html')

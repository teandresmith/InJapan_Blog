from flask import Blueprint, render_template

travel_bp = Blueprint('travel', __name__, url_prefix='/travel',
                      template_folder='templates', static_folder='static')

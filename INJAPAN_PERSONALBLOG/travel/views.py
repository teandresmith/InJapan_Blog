from flask import Blueprint, render_template

travel_bp = Blueprint('travel', __name__, url_prefix='/travel',
                      template_folder='templates', static_folder='static')

# Any function with anime_list = AnimeTable.query.all()
# is to fufill layout template
# It is to automate the updating of a new feature of InJapanBlog
# Where it seeks the database for anime titles and
# using a for title to develop blocks

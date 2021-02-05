from flask import Blueprint, render_template
from api.models.Anime_model.anime_model import AnimeTable
from api.models.Tags_Models.tags_model import Tag

about_bp = Blueprint('about', __name__,
                     template_folder='templates', static_folder='static')


@about_bp.route('/')
def about_page():
    '''This function renders the about me web page'''
    tag_list = Tag.query.all()
    anime_list = AnimeTable.query.order_by(AnimeTable.date.desc()).limit(1).all()
    return render_template('about.html', anime_list=anime_list, tag_list=tag_list)

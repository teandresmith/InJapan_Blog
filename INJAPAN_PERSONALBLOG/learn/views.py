from flask import Blueprint, render_template
from api.models.Anime_model.anime_model import AnimeTable
from api.models.Tags_Models.tags_model import Tag

learn_bp = Blueprint('learn', __name__,
                     template_folder='templates', static_folder='static')


# Any function with anime_list = AnimeTable.query.all()
# is to fufill layout template
# It is to automate the updating of a new feature of InJapanBlog
# Where it seeks the database for anime titles and
# using a for title to develop blocks

@learn_bp.route('/')
def japanese():
    tag_list = Tag.query.all()
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    return render_template('learn.html', anime_list=anime_list, tag_list=tag_list)


@learn_bp.route('/resources/web_resources')
def web_resources():
    tag_list = Tag.query.all()
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    '''This function renderes the Resources web page'''
    return render_template('web_resources.html', anime_list=anime_list, tag_list=tag_list)


@learn_bp.route('/resources/common_phrases')
def common_phrases():
    tag_list = Tag.query.all()
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    '''This function renders the common phrases web page'''
    return render_template('common_phrases.html', anime_list=anime_list, tag_list=tag_list)

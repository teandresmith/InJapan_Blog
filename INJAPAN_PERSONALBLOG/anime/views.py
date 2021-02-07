from flask import Blueprint, render_template
from api.models.Anime_model.anime_model import AnimeTable
from api.models.Tags_Models.tags_model import Tag

anime_bp = Blueprint(
    'anime', __name__, template_folder='templates', static_folder='static')


@anime_bp.route('/')
def anime_page():
    tag_list = Tag.query.all()
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    anime_descend_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).all()
    return render_template('anime.html', anime_descend_list=anime_descend_list, anime_list=anime_list, tag_list=tag_list)


@anime_bp.route('/<slug>')
def anime_recommendation(slug):
    tag_list = Tag.query.all()
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    post = AnimeTable.query.filter_by(slug=slug).one()
    return render_template('anime_template.html', post=post, anime_list=anime_list, tag_list=tag_list)

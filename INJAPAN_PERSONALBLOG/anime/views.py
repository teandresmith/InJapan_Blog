from flask import Blueprint, render_template
from api.models.Anime_model.anime_model import AnimeTable

anime_bp = Blueprint(
    'anime', __name__, template_folder='templates', static_folder='static')


@anime_bp.route('/')
def anime_page():
    anime_list = AnimeTable.query.all()
    anime_descend_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).all()
    return render_template('anime.html', anime_descend_list=anime_descend_list, anime_list=anime_list)


@anime_bp.route('/<slug>')
def anime_recommendation(slug):
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    post = AnimeTable.query.filter_by(slug=slug).one()
    return render_template('anime_template.html', post=post, anime_list=anime_list)

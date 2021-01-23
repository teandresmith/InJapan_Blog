from flask import Blueprint, render_template
from api.models.Anime_model.anime_model import AnimeTable
from api.models.Blog_Model.blog_model import Blogs

home_bp = Blueprint('home', __name__,
                    template_folder='templates', static_folder='static')


@home_bp.route('/')
def home_page():
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    blog_list = Blogs.query.order_by(Blogs.date.desc()).limit(1).all()
    return render_template('home.html', blog_list=blog_list, anime_list=anime_list)

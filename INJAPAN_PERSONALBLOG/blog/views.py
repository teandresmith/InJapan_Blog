from flask import Blueprint, render_template
from api.models.Anime_model.anime_model import AnimeTable
from api.models.Blog_Model.blog_model import Blogs

blog_bp = Blueprint('blog', __name__,
                    template_folder='templates', static_folder='static')


# Any function with anime_list = AnimeTable.query.all()
# is to fufill layout template
# It is to automate the updating of a new feature of InJapanBlog
# Where it seeks the database for anime titles and
# using a for title to develop blocks


@blog_bp.route('/')
def blog():
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    blog_list = Blogs.query.order_by(Blogs.date.desc()).all()
    return render_template('blog_page.html', blog_list=blog_list, anime_list=anime_list)


@blog_bp.route('/blogs/<slug>')
def blog_post(slug):
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    post = Blogs.query.filter_by(slug=slug).one()
    return render_template('blogs.html', post=post, anime_list=anime_list)


@blog_bp.route('/blog/first_post')
def first_blog():
    anime_list = AnimeTable.query.order_by(
        AnimeTable.date.desc()).limit(1).all()
    '''This function renders the first blog post web page'''
    return render_template('first_blog.html', anime_list=anime_list)

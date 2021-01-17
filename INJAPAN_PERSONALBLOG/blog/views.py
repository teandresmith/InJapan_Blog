from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__,
                    template_folder='templates', static_folder='static')


@blog_bp.route('/')
def blog():
    return render_template('blog.html')


@blog_bp.route('/blog/first_post')
def first_blog():
    '''This function renders the first blog post web page'''
    return render_template('first_blog.html')

from api.models.model import db
from api.models.Blog_Model.tags_blog_table import tags_blogs


class Blogs(db.Model):
    __tablename__ = 'blogs'
    blog_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    subtitle = db.Column(db.Text())
    content = db.Column(db.Text())
    image = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    slug = db.Column(db.String(255))
    tags = db.relationship('Tag', secondary=tags_blogs,
                           backref=db.backref('taglist', lazy='dynamic'))

    def __init__(self, title, subtitle, content, image, date, slug):
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.image = image
        self.date = date
        self.slug = slug

    def __repr__(self):
        return '<Blog %r>' % (self.blog_id)

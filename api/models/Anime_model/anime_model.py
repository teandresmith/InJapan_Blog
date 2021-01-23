from api.models.model import db


class AnimeTable(db.Model):
    __tablename__ = 'anime_table'
    anime_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    subtitle = db.Column(db.Text())
    content = db.Column(db.Text())
    image = db.Column(db.String(250))
    video = db.Column(db.String(250))
    date = db.Column(db.DateTime)
    slug = db.Column(db.String(255))

    def __init__(self, title, subtitle, content, image, video,  date, slug):
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.image = image
        self.video = video
        self.date = date
        self.slug = slug

    def __repr__(self):
        return '<Title %r>' % (self.anime_id)

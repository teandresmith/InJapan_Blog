from api.models.model import db

tags_blogs = db.Table('tags_blogs',
                      db.Column('blog_id', db.Integer,
                                db.ForeignKey('blogs.blog_id')),
                      db.Column('tag_id', db.Integer,
                                db.ForeignKey('tag.tag_id'))
                      )

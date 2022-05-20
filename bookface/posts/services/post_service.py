from flask import session
from bookface.misc import singleton
from bookface import db
from bookface.posts.models.post import Post
from sqlalchemy import desc


class PostService(metaclass=singleton.Singleton):
    def __init__(self):
        self.session = db.session

    def create(self, post):
        self.session.add(post)

    def update(self, user):
        self.session.merge(user)    

    def delete(self, post):
        self.session.delete(post)

    def get_by_id(self, post_id):
        return self.session.query(Post).filter_by(id=post_id).first()

    def get_all(self):
        return self.session.query(Post).all()

    def get_all_by_created_at(self):
        return self.session.query(Post).order_by(Post.created_at.desc()).all()

    def flush(self):
        self.session.commit()
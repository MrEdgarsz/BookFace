from flask_login import UserMixin
from sqlalchemy.orm import backref

from bookface import db, bcrypt
from bookface.roles.models.role import Role
from bookface.roles.services.roles_services import RolesService
from bookface.posts.models.postlike import PostLike


class User(db.Model, UserMixin):
    def __init__(self, username, password, role_id):
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self.role_id = role_id

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    role = db.relationship('Role', uselist=False, backref=backref('users'))

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def has_liked_post(self, post):
        return PostLike.query.filter(PostLike.user_id==self.id, PostLike.post_id==post.id).count() > 0

    def like_post(self, post):
        if not self.has_liked_post(post):
            like = PostLike(post_id=post.id, user_id=self.id)
            db.session.add(like)

    def unlike_post(self, post):
        if self.has_liked_post(post):
            PostLike.query.filter_by(user_id=self.id, post_id=post.id).delete()

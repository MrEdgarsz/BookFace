from bookface import db
from sqlalchemy.orm import backref
from datetime import datetime
from sqlalchemy import ForeignKey
from bookface.auth.models.user import User

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship('User', uselist=False, backref=backref('posts'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
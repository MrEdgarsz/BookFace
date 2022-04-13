from bookface import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Post(db.Model):
    __tablename__ = "posts"
    post_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, default=datetime.now())
    #user_id = db.Column(db.Integer, ForeignKey('user.user_id'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
from bookface import db

class PostLike(db.Model):
    __tablename__ = "postslikes"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

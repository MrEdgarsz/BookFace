from bookface import db
from sqlalchemy import Table, Column, Integer, Boolean, String, ForeignKey, MetaData


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    can_add_post = db.Column(db.Boolean, nullable=False)
    can_block_user = db.Column(db.Boolean, nullable=False)
    can_remove_post = db.Column(db.Boolean, nullable=False)

    def __init__(self, *args, **kwargs):
        super(Role, self).__init__(*args, **kwargs)


# define relationships with user model: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application

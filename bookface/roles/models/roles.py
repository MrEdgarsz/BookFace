from bookface import db
from sqlalchemy import Table, Column, Integer, Boolean, String, ForeignKey, MetaData


class Roles(db.Model):
    __tablename__ = "Roles"
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    can_add_post = db.Column(db.Boolean, nullable=False)
    can_block_user = db.Column(db.Boolean, nullable=False)
    can_remove_post = db.Column(db.Boolean, nullable=False)

    def __init__(self, *args, **kwargs):
        super(Roles, self).__init__(*args, **kwargs)

    def addRole(self, role):
        self._engine.session.add(role)


# define relationships with user model: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application

from flask_login import UserMixin
from sqlalchemy.orm import backref

from bookface import db, bcrypt


class User(db.Model, UserMixin):
    # noinspection SpellCheckingInspection
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
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

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

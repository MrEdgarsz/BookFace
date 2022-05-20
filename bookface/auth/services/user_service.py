import flask
from flask_login import login_user

from bookface import db
from bookface.auth.models.user import User
from bookface.misc import singleton
from bookface.roles.services.roles_services import RolesService


class UserService(metaclass=singleton.Singleton):
    def __init__(self):
        self.session = db.session

    def create(self, user):
        role = RolesService().getRoleByName("user")
        user.role_id = role.id
        self.session.add(user)
        self.session.commit()

    def update(self, user):
        self.session.merge(user)
        self.session.flush()

    def delete(self, user):
        self.session.delete(user)
        self.session.flush()

    def get_by_id(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

    def get_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def get_all(self):
        return self.session.query(User).all()

    def authenticate(self, username, password):
        user = self.get_by_username(username=username)
        if user and user.check_password(password):
            return user
        else:
            return None

    def flush(self):
        self.session.commit()


from flask import session
from bookface.misc import singleton
from bookface import db
from bookface.roles.models.role import Role


class RolesService(metaclass=singleton.Singleton):
    def __init__(self):
        self._engine = db
        self.session = self._engine.session

    def getRoleByName(self, name):
        return self.session.query(Role).filter_by(name=name).first()

    def addRole(self, role):
        self._engine.session.add(role)

    def removeRole(self, id):
        self._engine.session.remove(id)

    # def get_by_id(self, role_id):
    #     return self.session.query(Role).filter_by(id=role_id).first()

    def flush(self):
        self.session.commit()

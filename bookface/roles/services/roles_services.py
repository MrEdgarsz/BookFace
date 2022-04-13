
from flask import session
from bookface.misc import singleton
from bookface import db


class RolesService(metaclass=singleton.Singleton):
    def __init__(self):
        self._engine = db
        self.session = self._engine.session

    def addRole(self, role):
        self._engine.session.add(role)

    def removeRole(self, id):
        self._engine.session.remove(id)

    def flush(self):
        self.session.commit()

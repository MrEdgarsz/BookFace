from os import name
from bookface.roles.models import *
from bookface.roles.models.role import Roles
from bookface.roles.services.roles_services import RolesService


class DBGenerator():
    def __init__(self):
        self.roleService = RolesService()
        self.roles = []

    def cleanDB(self):
        self.roleService._engine.drop_all()
        self.roleService._engine.create_all()

    def genData(self):
        self.genRoles()

    def genRoles(self):
        admin = Roles(name="admin", can_add_post=True,
                      can_block_user=True, can_remove_post=True)
        moderator = Roles(name="moderator", can_add_post=True,
                          can_block_user=False, can_remove_post=True)
        user = Roles(name="user", can_add_post=True,
                     can_block_user=False, can_remove_post=False)
        blockedUser = Roles(name="blocked_user", can_add_post=False,
                            can_block_user=False, can_remove_post=False)
        roles = [admin, moderator, user, blockedUser]
        for role in roles:
            self.roles.append(role)
            self.roleService.addRole(role)
        self.roleService.flush()


if __name__ == "__main__":
    generator = DBGenerator()
    generator.cleanDB()
    generator.genData()

from bookface import db
from bookface.auth.models.user import User
from bookface.auth.services.user_service import UserService
from bookface.roles.models.role import Role
from bookface.roles.services.roles_services import RolesService


class DBGenerator:
    def __init__(self):
        self.roleService = RolesService()
        self.userService = UserService()
        self._engine = db

    def cleanDB(self):
        self._engine.drop_all()
        self._engine.create_all()

    def genData(self):
        self.genRoles()
        self.genUsers()

    def genUsers(self):
        kitkuLover = User( username="Kitku_Lover", password_hash= "$2b$12$exW9JpDkAwjmMV6AMrHwNu6J2zVohEoj.donah7kYpSVMjJQUB47i",role_id=1)
        dogoLover = User( username="Dogo_Lover",
                          password_hash="$2b$12$exW9JpDkAwjmMV6AMrHwNu6J2zVohEoj.donah7kYpSVMjJQUB47i", role_id=3)
        szopLover = User( username="Szop_Lover",
                          password_hash="$2b$12$exW9JpDkAwjmMV6AMrHwNu6J2zVohEoj.donah7kYpSVMjJQUB47i", role_id=2)

        stopkarz = User(username="Stopkarz",
                         password_hash="$2b$12$exW9JpDkAwjmMV6AMrHwNu6J2zVohEoj.donah7kYpSVMjJQUB47i", role_id=4)
                    
        users = [kitkuLover, dogoLover, szopLover, stopkarz]
        for user in users:
            self.userService.create(user)
        self.userService.flush()

    def genRoles(self):
        admin = Role(name="admin",
                     can_add_post=True,
                     can_block_user=True,
                     can_remove_post=True,
                     )
        moderator = Role(name="moderator",
                         can_add_post=True,
                         can_block_user=False,
                         can_remove_post=True,
                         )
        user = Role(name="user",
                    can_add_post=True,
                    can_block_user=False,
                    can_remove_post=False,
                    )
        blockedUser = Role(name="blocked_user",
                           can_add_post=False,
                           can_block_user=False,
                           can_remove_post=False,
                           )
        roles = [admin, moderator, user, blockedUser]
        for role in roles:
            self.roleService.addRole(role)
        self.roleService.flush()


if __name__ == "__main__":
    generator = DBGenerator()
    generator.cleanDB()
    generator.genData()

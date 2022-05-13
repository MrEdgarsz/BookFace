from random import randint
from bookface import db
from bookface.auth.models.user import User
from bookface.auth.services.user_service import UserService
from bookface.roles.models.role import Role
from bookface.roles.services.roles_services import RolesService
from bookface.posts.models.post import Post
from bookface.posts.services.post_service import PostService


class DBGenerator:
    def __init__(self):
        self.roleService = RolesService()
        self.userService = UserService()
        self.postService = PostService()
        self._engine = db

    def cleanDB(self):
        self._engine.drop_all()
        self._engine.create_all()

    def genData(self):
        self.genRoles()
        self.genUsers()
        self.genPosts()

    def genUsers(self):
        kitkuLover = User( username="Kitku_Lover", password_hash= "$2b$12$exW9JpDkAwjmMV6AMrHwNu6J2zVohEoj.donah7kYpSVMjJQUB47i",role_id=1)
        dogoLover = User( username="Dogo_Lover",
                          password_hash="$2b$12$exW9JpDkAwjmMV6AMrHwNu6J2zVohEoj.donah7kYpSVMjJQUB47i", role_id=3)
        szopLover = User( username="Szop_Lover",
                          password_hash="$2b$12$exW9JpDkAwjmMV6AMrHwNu6J2zVohEoj.donah7kYpSVMjJQUB47i", role_id=2)
                    
        users = [kitkuLover, dogoLover,szopLover]
        for user in users:
            self.userService.create(user)
        self.userService.flush()

    def genRoles(self):
        admin = Role(name="administrator",
                     can_add_post=True,
                     can_block_user=True,
                     can_remove_post=True,
                     )
        moderator = Role(name="moderator",
                         can_add_post=True,
                         can_block_user=False,
                         can_remove_post=True,
                         )
        user = Role(name="użytkownik",
                    can_add_post=True,
                    can_block_user=False,
                    can_remove_post=False,
                    )
        blockedUser = Role(name="zablokowany",
                           can_add_post=False,
                           can_block_user=False,
                           can_remove_post=False,
                           )
        roles = [admin, moderator, user, blockedUser]
        for role in roles:
            self.roleService.addRole(role)
        self.roleService.flush()

    def genPosts(self):
        post1 = Post(description="<img src='https://twojememy.pl/wp-content/uploads/2020/12/Kitku-w-szoku.jpg' width='297' height='294' alt="" data-mce-src='https://twojememy.pl/wp-content/uploads/2020/12/Kitku-w-szoku.jpg' style='display: block; margin-left: auto; margin-right: auto;' data-mce-style='display: block; margin-left: auto; margin-right: auto;'><br>Nie wiem, jak wy, ale ja śmiechłem😄", likes = randint(3,21), user_id=1)
        post2 = Post(description="<h2>Czym jest Szop?</h2><b>Szop</b> to rodzaj ssaka z rodziny szopowatych (po łacinie <i>Procyonidae</i>).<br>Rodzaj obejmuje gatunki występujące w Ameryce. W Polsce stwierdzono od 1927 r. obecność szopa pracza żyjącego w warunkach naturalnych. Jest to populacja uciekinierów z hodowli. Przewidywane jest rozprzestrzenianie się tego gatunku na terenie całej Polski.<br>Źródło: <a href='https://pl.wikipedia.org/wiki/Szop' data-mce-href='https://pl.wikipedia.org/wiki/Szop'>https://pl.wikipedia.org/wiki/Szop</a>", likes = randint(3,21), user_id=3)
        post3 = Post(description="Psy są najlepsze. Koniec kropka. <b>Don't change my mind!</b>", likes = 0, user_id=2)
                    
        posts = [post1, post2, post3]
        for post in posts:
            self.postService.create(post)
        self.postService.flush()


if __name__ == "__main__":
    generator = DBGenerator()
    generator.cleanDB()
    generator.genData()

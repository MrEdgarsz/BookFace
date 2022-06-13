from datetime import datetime
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
        kitkuLover = User(username="Kitku_Lover", password="test1234", role_id=1)
        dogoLover = User(username="Dogo_Lover",
                         password="test1234", role_id=2)
        szopLover = User(username="Szop_Lover",
                         password="test1234", role_id=3)
        stopkarz = User(username="Stopkarz",
                        password="test1234", role_id=4)
        gameLover = User(username="Game_Lover",
                        password="test1234", role_id=3)

        users = [kitkuLover, dogoLover, szopLover, stopkarz, gameLover]
        for user in users:
            self.userService.create(user)
        self.userService.flush()

    def genRoles(self):
        admin = Role(name="Administrator",
                     can_add_post=True,
                     can_block_user=True,
                     can_remove_post=True,
                     )
        moderator = Role(name="Moderator",
                         can_add_post=True,
                         can_block_user=False,
                         can_remove_post=True,
                         )
        user = Role(name="Użytkownik",
                    can_add_post=True,
                    can_block_user=False,
                    can_remove_post=False,
                    )
        blockedUser = Role(name="Zablokowany",
                           can_add_post=False,
                           can_block_user=False,
                           can_remove_post=False,
                           )
        roles = [admin, moderator, user, blockedUser]
        for role in roles:
            self.roleService.addRole(role)
        self.roleService.flush()

    def genPosts(self):
        post0 = Post(
            description="<h1 style='text-align: center;'>Witajcie na BookFace!</h1><p style='text-align: center;'>Zarówno całej administracji jak i moderacji jest niezmiernie miło gościć was na naszej nowopowstałej platformie. Mamy nadzieję, że będziecie się tu świetnie bawić.</p>",
            created_at=datetime(2022, 4, 6, 19, 2), updated_at=datetime(2022, 4, 6, 19, 2),
            user_id=1)
        post1 = Post(
            description="<p><img src='https://twojememy.pl/wp-content/uploads/2020/12/Kitku-w-szoku.jpg' data-mce-src='https://twojememy.pl/wp-content/uploads/2020/12/Kitku-w-szoku.jpg' class='card-img-top'><br>Nie wiem, jak wy, ale ja śmiechłem😄</p>",
            created_at=datetime(2022, 5, 14, 16, 49), updated_at=datetime(2022, 5, 14, 16, 49),
            user_id=1)
        post2 = Post(
            description="<h2>Czym jest Szop?</h2><p><strong>Szop</strong> to rodzaj ssaka z rodziny szopowatych (po łacinie <em>Procyonidae</em>).<br>Rodzaj obejmuje gatunki występujące w Ameryce. W Polsce stwierdzono od 1927 r. obecność szopa pracza żyjącego w warunkach naturalnych. Jest to populacja uciekinierów z hodowli. Przewidywane jest rozprzestrzenianie się tego gatunku na terenie całej Polski.<br>Źródło: <a href='https://pl.wikipedia.org/wiki/Szop' data-mce-href='https://pl.wikipedia.org/wiki/Szop'>https://pl.wikipedia.org/wiki/Szop</a></p>",
            user_id=3)
        post3 = Post(description="<p>Psy są najlepsze. Koniec kropka. <strong>Don't change my mind!</strong></p>",
                     user_id=2)
        post4 = Post(description="<p>Biegnie zziajany pies przez pustynię i myśli: 'Jak zaraz nie znajdę jakiegoś drzewa, to się posikam'.</p>",
                     user_id=2)
        post5 = Post(description="<p>Chciałbym mieć szopa w domu. Nazwałbym go Rocket.<br><img src='https://i.pinimg.com/originals/07/e1/48/07e148a690701ba6c909cfb372aabe9d.gif' class='card-img-top'></p>",
                     created_at=datetime(2022, 6, 11, 13, 43), updated_at=datetime(2022, 6, 11, 13, 43), user_id=3)
        post6 = Post(description="<p>Patrzcie na to xD<br><img src='https://scontent.flcj1-1.fna.fbcdn.net/v/t39.30808-6/287162814_10160452298296042_2541147672778630526_n.png?_nc_cat=109&ccb=1-7&_nc_sid=730e14&_nc_ohc=uD1G6yUEQ88AX8Rvuzx&_nc_ht=scontent.flcj1-1.fna&oh=00_AT9DZ1b0Rf_sstj1LouY_11mL2jr2aTenRftq4ETUTXS5A&oe=62AB2CC1' class='card-img-top'></p>",
                    user_id=5)             

        posts = [post0, post1, post2, post3, post4, post5, post6]
        for post in posts:
            self.postService.create(post)
        self.postService.flush()


if __name__ == "__main__":
    generator = DBGenerator()
    generator.cleanDB()
    generator.genData()

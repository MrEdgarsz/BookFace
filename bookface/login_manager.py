from flask_login import LoginManager

from bookface.bookface import app
from bookface.auth.services.user_service import UserService

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return UserService().get_by_id(user_id=user_id)


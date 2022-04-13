from flask_login import LoginManager

from bookface import app
from bookface.auth.models.user import User

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

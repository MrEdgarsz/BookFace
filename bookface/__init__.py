from flask import Flask, render_template, Blueprint
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="pages")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookface.db"
app.config["SECRET_KEY"] = "97fdf98cb2f69976dc8c7c17"
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from bookface.auth.services.user_service import UserService
from bookface.auth.routes import auth as auth_module
app.register_blueprint(auth_module)


@app.route("/")
def index():
    return render_template("home.html")


login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return UserService(db=db).get_by_id(user_id=user_id)

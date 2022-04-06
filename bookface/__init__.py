from pydoc import render_doc
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from bookface.auth import auth

app = Flask(__name__, template_folder="pages")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///condition_monitor.db"
app.config["SECRET_KEY"] = "97fdf98cb2f69976dc8c7c17"
app.register_blueprint(auth)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return None;

@app.route("/")
def home_page():
    return render_template("home.html")
from pydoc import render_doc
from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from bookface.auth import auth
from bookface.auth import routes
from bookface.auth.forms.login_form import LoginForm

app = Flask(__name__, template_folder="pages")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookface.db"
app.config["SECRET_KEY"] = "97fdf98cb2f69976dc8c7c17"
app.register_blueprint(auth)
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


@app.route("/")
@app.route("/sign_in_page")
def sign_in_page():
    form = LoginForm()
    return render_template("sign_in_page.html", form=form)

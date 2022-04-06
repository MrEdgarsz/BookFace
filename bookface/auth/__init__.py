from flask import Blueprint, render_template

from bookface.auth.controllers.login_controller import sign_in

auth_module = Blueprint('auth', __name__, url_prefix='/auth', template_folder="pages")

@auth_module.route('/')
def home():
    return render_template("index.html")

@auth_module.route("/sign_in")
def route_to_singIn():
    return sign_in();
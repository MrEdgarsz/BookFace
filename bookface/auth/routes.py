from flask import render_template, url_for
from flask_login import current_user, login_required, logout_user
from werkzeug.utils import redirect

from bookface import bcrypt
from bookface.auth import auth
from bookface.auth.controllers.login_controller import handle_sign_in
from flask import Blueprint

from bookface.auth.controllers.register_controller import handle_sign_up


# @auth.route('/')
# def home():
#     return render_template("sign_in_page.html")

@auth.route('/',methods=['POST', 'GET'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('postboard.postboard_page'))
    return handle_sign_in()



@auth.route("/register", methods=['POST', 'GET'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('postboard.postboard_page'))
    return handle_sign_up()


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.sign_in'))



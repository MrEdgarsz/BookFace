from flask import render_template

from bookface.auth import auth
from bookface.auth.controllers.login_controller import handle_sign_in
from flask import Blueprint


@auth.route('/')
def home():
    return render_template("index.html")


@auth.route("/login", methods=['POST', 'GET'])
def sign_in():
    return handle_sign_in()


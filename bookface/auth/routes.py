from flask import render_template

from bookface import auth
from bookface.auth.controllers.login_controller import sign_in
from bookface.auth.forms.login_form import LoginForm


@auth.route('/')
def home():
    return render_template("index.html")


@auth.route("/login", methods=['GET'])
def sign_in_without_form():
    form = LoginForm()
    return sign_in(form)


@auth.route("/login", methods=['POST'])
def sign_up_with_form():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.data.get('username'))
        print(form.data.get('password'))
        #TODO: Handle login
    form.data.update({'password': ''})
    return sign_in(form)


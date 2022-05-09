from flask import render_template
from flask_login import login_user
from flask_wtf import FlaskForm

from bookface.auth.forms.login_form import LoginForm
from bookface.auth.services.user_service import UserService


def handle_sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        result = UserService().authenticate(username=form.username.data, password=form.password.data)
        if result is not None:
            login_user(result)
        else:
            form.errors.append("Invalid username or password")
    form.data.update({'password': ''})
    return render_template("sign_in_page.html", form=form)


def sign_in_with_form():
    return render_template("index.html")

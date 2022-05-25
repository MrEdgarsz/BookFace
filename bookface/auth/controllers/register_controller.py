import flask
from flask import render_template, url_for
from werkzeug.utils import redirect

from bookface.auth.forms.register_form import RegisterForm
from bookface.auth.models.user import User
from bookface.auth.services.user_service import UserService


def handle_sign_up():
    form = RegisterForm()
    if form.validate_on_submit():
        UserService().create(user=User(username=form.username.data, password=form.password.data,role_id=3))
        form.data.clear()
        flask.flash("You have successfully registered! you can now sign in.", "success")
        return redirect(url_for("auth.sign_in"))
    return render_template("sign_up_page.html", form=form)

from flask import render_template, flash, request, url_for
from flask_login import login_user
from flask_wtf import FlaskForm
from werkzeug.utils import redirect

from bookface.auth.forms.login_form import LoginForm
from bookface.auth.services.user_service import UserService


def handle_sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        result = UserService().authenticate(username=form.username.data, password=form.password.data)
        if result is not None:
            login_user(result)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('postboard.postboard_page')
            print(next)
            return redirect(next)
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('auth.sign_in'))
    form.data.update({'password': ''})
    return render_template("sign_in_page.html", form=form)



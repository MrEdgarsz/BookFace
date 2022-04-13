from flask import render_template
from flask_wtf import FlaskForm


def sign_in(login_form: FlaskForm):
    return render_template("sign_in_page.html", form=login_form)


def sign_in_with_form():
    return render_template("index.html")

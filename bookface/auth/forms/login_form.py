from flask_wtf import FlaskForm
from wtforms import StringField, Form, SubmitField, HiddenField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("", validators=[DataRequired()],render_kw={"placeholder":"Nazwa użytkownika"} )
    password = PasswordField("", validators=[DataRequired()],  render_kw={"placeholder": "Hasło"})
    submit = SubmitField('Zaloguj się')

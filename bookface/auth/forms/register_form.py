from flask_wtf import FlaskForm
from wtforms import StringField, Form, SubmitField, HiddenField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    username = StringField("",validators=[DataRequired()],  render_kw={"placeholder": "Nazwa użytkownika"})
    password = PasswordField( "",validators=[DataRequired()],  render_kw={"placeholder": "Hasło"})
    password_confirm = PasswordField("",validators=[DataRequired(),  EqualTo('password', message='Hasła muszą się zgadzać')],  render_kw={"placeholder": "Potwierdź hasło"})
    submit = SubmitField('Zarejestruj się')

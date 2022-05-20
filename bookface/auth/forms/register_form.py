from flask_wtf import FlaskForm
from wtforms import StringField, Form, SubmitField, HiddenField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()], )
    password = PasswordField('Hasło', validators=[DataRequired()],)
    password_confirm = PasswordField('Potwierdź hasło', validators=[DataRequired(),  EqualTo('password', message='Hasła muszą się zgadzać')],)
    submit = SubmitField('Zarejestruj')

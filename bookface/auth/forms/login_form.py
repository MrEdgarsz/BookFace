from flask_wtf import FlaskForm
from wtforms import StringField, Form, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = StringField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')

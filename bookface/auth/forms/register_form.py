from flask_wtf import FlaskForm
from wtforms import StringField, Form, SubmitField, HiddenField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Regexp


class RegisterForm(FlaskForm):
    username = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Nazwa użytkownika"})
    password = PasswordField('', validators=[DataRequired(), Regexp('^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$', message="Hasło musi posiadać przynajmniej 8 znaków w tym jedną wielką jedną małą literę, jedną cyfrę i jeden znak specjalny.")], render_kw={"placeholder": "Hasło"})
    password_confirm = PasswordField('', validators=[DataRequired(), EqualTo('password', message='Hasła muszą się zgadzać')], render_kw={"placeholder": "Potwierdź hasło"})
    submit = SubmitField('Zarejestruj się')

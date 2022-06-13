from flask_wtf import FlaskForm
from wtforms import StringField, Form, SubmitField, HiddenField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Regexp


class RegisterForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()], )
    password = PasswordField('Hasło', validators=[DataRequired(), Regexp('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$',message="Hasło musi posiadać przynajmniej 8 znaków w tym jedną wielką jedną małą literę, jedną cyfrę i jeden znak specjalny.")],)
    password_confirm = PasswordField('Potwierdź hasło', validators=[DataRequired(),  EqualTo('password', message='Hasła muszą się zgadzać')],)
    submit = SubmitField('Zarejestruj')

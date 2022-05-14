from flask_wtf import FlaskForm
from wtforms import TextAreaField, Form, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    content = TextAreaField('Treść posta', validators=[DataRequired()])
    submit = SubmitField('Dodaj post')
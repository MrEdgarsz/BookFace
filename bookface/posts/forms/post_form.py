from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, Form, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    user_id = IntegerField('Autor', validators=[DataRequired()])
    description = TextAreaField('Treść posta', validators=[DataRequired()])
    submit = SubmitField('Dodaj post')
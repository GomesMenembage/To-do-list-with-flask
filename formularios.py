from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    title = StringField("Título", validators=[DataRequired()])
    content = TextAreaField("Conteúdo", validators=[DataRequired()])
    category = SelectField("Categoria", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Salvar Nota")
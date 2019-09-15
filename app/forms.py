from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import ValidationError, DataRequired
from app.models import Dictionary


class QuizForm(FlaskForm):
    no_of_questions = IntegerField(
        'Number of Questions', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LookupForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddwordForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    definition = StringField('Definition', validators=[DataRequired()])
    example1 = StringField('Example 1', validators=[DataRequired()])
    example2 = StringField('Example 2')
    synonyms = StringField('Synonyms')
    submit = SubmitField('Add Word to Dictionary')

    def validate_word(self, word):
        word_query = Dictionary.query.filter_by(word=word.data).first()
        if word_query is not None:
            raise ValidationError(
                f'The word "{word.data}" already exists in Dictionary.')

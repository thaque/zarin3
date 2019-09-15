from flask import render_template, flash, url_for, redirect
from app import app
from app.forms import QuizForm, LookupForm, AddwordForm
from app.models import Dictionary
from app import db


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Zarin'}
    return render_template('index.html', title='Home', user=user)


@app.route('/quizsetup', methods=['GET', 'POST'])
def quizsetup():
    form = QuizForm()
    if form.validate_on_submit():
        flash(f'Quiz generated with {form.no_of_questions.data} Questions')
        no = form.no_of_questions.data
        # questions = generate_questions(no)
        # definition = get_definition(questions[0])
        # choices = generate_choices(definition)
        return redirect(url_for('quiz'))
        # return f'''
        #     <html>
        #         <body>
        #             <p>{choices}</p>
        #         </body>
        #     </html>
        # '''
    return render_template('quizsetup.html', title='Quiz Setup', form=form)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return redirect(url_for('index'))


@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    form = LookupForm()
    if form.validate_on_submit():
        definition = Dictionary.query.filter_by(
            word=form.word.data).first()
        if definition is None:
            flash(f"Can't find definition of {form.word.data}")
            return redirect(url_for('lookup'))
        render_template('lookup.html', title='Lookup Word',
                        form=form, definition=definition)

    return render_template('lookup.html', title='Lookup Word', form=form)


@app.route('/addword', methods=['GET', 'POST'])
def addword():
    form = AddwordForm()
    if form.validate_on_submit():
        word = Dictionary(word=form.word.data, definition=form.definition.data,
                          example1=form.example1.data, example2=form.example2.data, synonyms=form.synonyms.data)
        db.session.add(word)
        db.session.commit()
        flash(f'"{form.word.data}" has been added to the Dictionary.')
        return redirect(url_for('addword'))
    return render_template('addword.html', title='Add Word', form=form)

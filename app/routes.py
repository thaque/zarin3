from flask import render_template, flash, url_for, redirect
from app import app
from app.forms import QuizForm


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

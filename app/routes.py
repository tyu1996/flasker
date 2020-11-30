from app import app
from flask import render_template, redirect

from .forms import SampleForm


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/articles')
def articles():
    return render_template('articles.html')


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = SampleForm()

    # If form is upon submission and is validated success
    if form.validate_on_submit():
        return redirect('index')

    return render_template('forms.html', form=form)

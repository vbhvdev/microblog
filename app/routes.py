from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vaibhav'}
    posts = [
        {
            'author': {'username': 'Miguel'},
            'body': 'Just keep going.'
        },
        {
            'author': {'username': 'John'},
            'body': 'Its thursday already, wtf!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
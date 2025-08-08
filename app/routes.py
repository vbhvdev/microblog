from flask import render_template
from app import app

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
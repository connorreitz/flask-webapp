from flask import render_template, flash, redirect
from app.forms import LoginForm

from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Connor'}
    posts = [
        {
            'author' : {'username': 'Jon'},
            'body' : 'Chicken sandwiches! Add chicken and sandwich.'

        },
        {
            'author' : {'username': 'Stacy'},
            'body' : 'Cheesecake! add cheese and cake.'

        }

    ]


    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)

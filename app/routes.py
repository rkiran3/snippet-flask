from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Bob'}
	snippets = [
		{
			'title': 'Learning Flask',
			'category': 'Flask',
			'content': 'Learning Flask to write Snippet'
		},
		{
			'title': 'Lists in Python',
			'category': 'Python',
			'content': 'Iterating Lists in Python is one liner'
		}
	]

	return render_template('index.html', title='Home', user=user, snippets=snippets)
 
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}'.format(form.username.data))
		return redirect('/index')

	return render_template('login.html', title='Sign In', form=form)

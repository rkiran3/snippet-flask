## Install python3

    $ python3

## Install Flask

    $ pip install flask

## Create Snippet package

    $ mkdir snippet-flask
    $ cd snippet-flask

### Create virtual environment 

    ~/snippet-flask$ python3 -m venv venv
    ~/snippet-flask$ venv/bin/activate

    (venv) $

## Start project 
    Remain in the same folder

    (venv) $ mkdir app

### Create a new file app/\__init\_\_.py
    # app/__init__.py

    from flask import Flask
    app = Flask(__name__)
    from app import routes

### Create main application module snippet-flask.py

    (venv) $ vi snippet-flask.py
    (venv) $ cat snippet-flask.py 

        from app import app


Also create a templates folder to indicate html to use.

    (venv) kiran@atobs2:~/snippet-flask$ tree -I 'venv|__pycache__'
    .
    ├── app
    │   ├── __init__.py
    │   ├── routes.py
    │   └── templates
    │       └── index.html
    ├── README.md
    └── snippet-flask.py

## Run Flask

    (venv) $ flask run

    View in browser
    
    http://localhost:5000/

## Setting a Secret Key and 'config'

Secret key can be set in a separate configuration file config.py 
and imported in _init_.py 

We will get an error "ModuleNotFoundError: No module named 'config'"

Install the config using pip

(venv) : pip install config

## Create a Form Class and Template to accept user input

### Form Class
We will create a Form now to accept user logins, at the simplest it will have user name and password field.
It will have a submit button that will submit to backend.

The form will import corresponding String, Password fields along with validators that prompt user to enter values.

    app/forms.py

    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField, BooleanField, SubmitField
    from wtforms.validators import DataRequired

    # This Form Class defines the form-fields as class variables.
    class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Sign In')

### Form Template

    app/templates/login.html

    {% extends "base.html" %}
    {% block content %}
        <h1>Sign In</h1>
        <form action="" method="post" novalidate>
            {{ form.hidden_tag() }}
            <p>
                {{ form.username.label }}<br>
                {{ form.username(size=32) }}
            </p>
            <p>
                {{ form.password.label }}<br>
                {{ form.password(size=32) }}
            </p>
            <p>{{ form.submit() }}</p>
        </form>
    {% endblock %}

### Use Login Form in routes.py

    This file will contain a function for 'index', create one for 'login' which will be used for signon

    app/routes.py

    import libraries for printing errors, url_for to specify url

    from flask import render_template, flash, redirect, url_for

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for user {}'.format(form.username.data))
            return redirect(url_for('index'))

        return render_template('login.html', title='Sign In', form=form)

### unexpected keywork argument 'method'
    When testing forms, restarting Flask trying signon links showed error
    TypeError: __init__() got an unexpected keyword argument 'method'

    This error came due to incorrect name of argument to login 

    app/routes.py 

    Incorrect:
    @app.route('/login', method=['GET', 'POST'])

    Correct:
    @app.route('/login', methods=['GET', 'POST'])

## Database

We will be using SQL-Alchemy for which install flask-sqlalchemy and flask-migrate

    (venv) ~/snippet-flask$ pip install flask-sqlalchemy
    Collecting flask-sqlalchemy
    Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl (17 kB)
    Successfully installed SQLAlchemy-1.4.37 flask-sqlalchemy-2.5.1 greenlet-1.1.2

    (venv):~/snippet-flask$ pip install flask-migrate

Credentials in app/config.py

    import os
    basedir = os.path.abspath(os.path.dirname(__file__))

    class Config(object):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False

### Creating User Model

    app/models.py

    from app import db

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), index=True, unique=True)
        email = db.Column(db.String(120), index=True, unique=True)
        password_hash = db.Column(db.String(128))

        def __repr__(self):
            return '<User {}>'.format(self.username)

### Migration

    (venv) $ ~/snippet-flask$ flask db migrate
    INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.autogenerate.compare] Detected added table 'user'
    INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_email' on '['email']'
    INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_username' on '['username']'
    Generating /home../migrations/versions/9f25105d1a34_.py ...  done
    (venv) $ flask db upgrade
    INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade  -> 9f25105d1a34, empty message

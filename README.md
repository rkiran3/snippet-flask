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

## Setting a Secret Key



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



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
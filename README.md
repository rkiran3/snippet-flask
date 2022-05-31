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

Create a new file app/\__init\_\_.py

    from flask import Flask
    app = Flask(__name__)
    from app import routes

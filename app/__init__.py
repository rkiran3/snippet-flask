from flask import Flask
#from config import Config

app = Flask(__name__)

# setting secret
app.config['SECRET_KEY'] = 'my-secret'

from app import routes

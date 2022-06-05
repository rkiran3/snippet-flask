from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# setting secret
app.config.from_object(Config)
#app.config['SECRET_KEY'] = 'my-secret'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models

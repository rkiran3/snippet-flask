from enum import unique
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    snippets = db.relationship('Snippet', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    category = db.Column(db.String(256))
    content = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __ref__(self):
        return '<Snippet {}'.format(self, self.title)

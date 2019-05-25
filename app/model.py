#from database import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro = db.Column(db.String(200))
    escritor = db.Column(db.String(255))

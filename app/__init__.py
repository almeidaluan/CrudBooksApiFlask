from flask import Flask
from flask_migrate import Migrate
from .model import configure
from .serializer import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/luan/Documents/db/crudzao.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure(app)
    config_ma(app)

    Migrate(app, app.db)

    from .books import bp_books
    app.register_blueprint(bp_books)
    return app

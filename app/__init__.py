from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///academia_danzas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "secret_key"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

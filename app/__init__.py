from flask import Flask
from app.config import Config
from app.models import db
from app.routes import register_routes

def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)
    return app

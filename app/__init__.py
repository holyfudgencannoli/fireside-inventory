from flask import Flask
from flask_cors import CORS
from config import Config
from db import Base, engine

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8081", "http://localhost"]}}, supports_credentials=True)

    import models

    Base.metadata.create_all(bind=engine)



    return app

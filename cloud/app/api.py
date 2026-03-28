from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
api = Api(app)


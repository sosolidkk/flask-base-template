from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)
app.config.from_object(Config)

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)

login = LoginManager(app=app)
login.login_view = "/sign-in"

from app import routes

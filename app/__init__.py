from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from pathlib import Path

app = Flask(__name__)
Path(app.instance_path).mkdir(parents=True, exist_ok=True)
app.config.from_object(Config)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
	from app.models.usuario import Usuario
	return db.session.get(Usuario, int(user_id))

from app import routes, models

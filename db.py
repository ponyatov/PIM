from httpd import app

from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)

from project.extensions import db, bcrypt
from datetime import datetime
from flask_login import UserMixin

class Post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

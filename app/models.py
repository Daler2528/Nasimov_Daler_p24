from app import db
from datetime import datetime
from app import db

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    confirm_password = db.Column(db.String(512), nullable=False)
    create_at = db.Column(db.Date, default=datetime.now)

class Books(db.Model):
    __tablename__ = 'Books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128),  nullable=False)
    author = db.Column(db.String(128), nullable=False)
    page_count = db.Column(db.Integer, nullable=False)


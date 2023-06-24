from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

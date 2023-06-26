from sqlalchemy.orm.session import Session
from database.models import DbPost
import datetime
from flask_restx import abort

def create_post(db: Session, request: dict):
    new_post = DbPost(
        image_url=request.get('image_url'),
        title=request.get('title'),
        content=request.get('content'),
        creator=request.get('creator'),
        timestamp=datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db: Session):
    return db.query(DbPost).all()

def get_post_by_id(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise abort(404, 'Post not found')
    return post

def delete_post(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise abort(404, 'Post not found')
    db.delete(post)
    db.commit()
    return post



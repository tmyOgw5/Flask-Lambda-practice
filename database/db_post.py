from sqlalchemy.orm.session import Session
from database.models import DbPost
import datetime

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



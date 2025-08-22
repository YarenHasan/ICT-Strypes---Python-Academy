from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from . import models, schemas


def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    obj = models.Item(title=item.title, description=item.description, url=str(item.url))
    db.add(obj)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        obj = db.query(models.Item).filter(models.Item.url == str(item.url)).first()
        return obj
    db.refresh(obj)
    return obj


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[models.Item]:
    return db.query(models.Item).order_by(models.Item.created_at.desc()).offset(skip).limit(limit).all()


def get_item(db: Session, item_id) -> Optional[models.Item]:
    return db.query(models.Item).get(item_id)


def delete_item(db: Session, item_id) -> bool:
    obj = db.query(models.Item).get(item_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True

from sqlalchemy.orm import Session
from . import models, schemas


def get_categories(db: Session):
    return db.query(models.Categories).all()

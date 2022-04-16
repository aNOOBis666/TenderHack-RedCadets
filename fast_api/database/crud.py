from sqlalchemy.orm import Session
from . import models, schemas


def get_deals(db: Session):
    return db.query(models.Deal).all()


def get_deal_by_id(db: Session, deal_id: int):
    return db.query(models.Deal).filter(models.Deal.id_deal == deal_id).first()


def create_deal(category: schemas.DealCreate, db: Session):
    db_user = models.Deal(**category.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(category: schemas.UserCreate, db: Session):
    db_user = models.User(**category.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_last_bet_by_id(db: Session, deal_id: int):
    return db.query(models.Lastbet).filter(models.Lastbet.last_bet_id == deal_id).first()


# def update_last_bet(category: schemas.LastBetsCreate, db: Session, deal_id: int):
#     db_user = models.Notifications(**category.dict(), owner_id=owner_id)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


def get_notifications_by_user_id(db: Session, user_id: int):
    return db.query(models.Notifications).filter(models.Notifications.owner_id == user_id).first()


def create_notification(category: schemas.NotificationsCreate, db: Session, owner_id: int, id_notification: int,
                        user_preference: str, notification_type: str):
    db_user = models.Notifications(**category.dict(), owner_id=owner_id, id_notification=id_notification,
                                   user_preference=user_preference, notification_type=notification_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

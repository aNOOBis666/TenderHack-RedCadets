from sqlalchemy.orm import Session
from . import models, schemas
from .roboLogics.dealGame import bots


def get_deals(db: Session):
    return db.query(models.Deal).all()


def get_deal_by_id(db: Session, deal_id: int):
    return db.query(models.Deal).filter(models.Deal.id_deal == deal_id).first()


def create_deal(category: schemas.DealCreate, db: Session):
    db_user = models.Deal(**category.dict())
    db.add(db_user)
    db_empty_bet = models.Lastbet()
    db.add(db_empty_bet)
    db.commit()
    db.refresh(db_user)
    db.refresh(db_empty_bet)
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


def update_last_bet(category: schemas.LastBetsCreate, db: Session, user_id: int):
    db.query(models.Lastbet).filter(models.Lastbet.last_bet_id == user_id).update(**category.dict()).all()
    db.commit()
    bots(db, get_last_bet_by_id(db, user_id))


def get_notifications_by_user_id(db: Session, user_id: int):
    return db.query(models.Notifications).filter(models.Notifications.owner_id == user_id).first()


def create_notification(category: schemas.NotificationsCreate, db: Session):
    db_user = models.Notifications(**category.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def post_bot_info(category: schemas.RobotCreate, db: Session):
    db_user = models.Robot(**category.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

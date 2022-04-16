from sqlalchemy.orm import Session
from . import models, schemas


def get_deals(db: Session):
    return db.query(models.Deal).all()


def get_deal_by_id(db: Session, deal_id: int):
    return db.query(models.Deal).filter(models.Deal.id_deal == deal_id).first()


def create_deal(category: schemas.DealCreate, db: Session, id_deal: int, name_deal: str, description_deal: str,
                date_deal: str, owner_id: int, first_place_id: int, second_place_id: int, status_deal: str,
                start_price: int):
    db_user = models.Deal(**category.dict(), id_deal=id_deal, name_deal=name_deal, description_deal=description_deal,
                          date_deal=date_deal, owner_id=owner_id, first_place_id=first_place_id,
                          second_place_id=second_place_id, status_deal=status_deal, start_price=start_price)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(category: schemas.UserCreate, db: Session, id: int, email: str, surname: str, name: str,
                date_creation: str, nalog_name: int, password: str, role: str):
    db_user = models.User(**category.dict(), id=id, email=email, surname=surname, name=name,
                          date_creation=date_creation, nalog_name=nalog_name, password=password, role=role)
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

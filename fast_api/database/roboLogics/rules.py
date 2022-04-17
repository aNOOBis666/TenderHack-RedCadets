# In time on create call. Calls once for current deal

from database import models
from sqlalchemy.orm import Session


def on_send_time(db: Session, ownerId: int):
    robot_strategy = db.query(models.Robot).filter(models.Robot.owner_id == ownerId).first()
    if robot_strategy.send_time == 0:
        db.query(models.Robot).filter(models.Robot.owner_id == ownerId).update({'delay': 0})
        db.commit()
    elif robot_strategy.send_time == 1:
        return
        # TODO: impl currentDate
    elif robot_strategy.send_time == 2:
        return
        # TODO: impl leastDate
    else:
        return


def on_selling_type(db: Session, ownerId: int, dealId: int):
    robot_strategy = db.query(models.Robot).filter(models.Robot.owner_id == ownerId).first()
    if robot_strategy.selling_type == 0:
        db.query(models.Robot).filter(models.Robot.owner_id == ownerId).update({'delay': +30})
        db.commit()
    elif robot_strategy.selling_type == 1:
        db.query(models.Robot).filter(models.Robot.owner_id == ownerId).update({'delay': -30})
        db.commit()
    elif robot_strategy.selling_type == 2:
        smart_selling(db, ownerId, dealId)


def smart_selling(db: Session, ownerId: int, dealId: int):
    robots_list = db.query(models.Robot).filter(
        (models.Robot.is_stop == False) and (models.Robot.deal_id != dealId)).all()
    if len(robots_list) >= 3:
        db.query(models.Robot).filter(models.Robot.owner_id == ownerId).update({'delay': 0, 'isHuman': False})
    else:
        db.query(models.Robot).filter(models.Robot.owner_id == ownerId).update({'delay': +30, 'isHuman': True})
    db.commit()


def is_duo(db: Session, ownerId: int):
    robots = db.query(models.Robot).filter(
        (models.Robot.owner_id == ownerId) and (models.Robot.is_smart_duo == True)).all()
    if robots is not None:
        return True
    else:
        return False

import time
from database import models
from sqlalchemy.orm import Session
from . import rules
from . import notificationSender
from . import config

test_emulation = 40


def bots(db: Session, dealId: int):
    robots_list = db.query(models.Robot).filter(
        (models.Robot.deal_id == dealId) and (models.Robot.is_pause == False)).all()
    last_bet = db.query(models.Lastbet).filter(models.Lastbet.last_bet_id == dealId).first()
    deal = db.query(models.Deal).filter(models.Deal.id_deal == dealId).first()
    for robot in robots_list:
        user = db.query(models.User).filter(models.User.id == robot.owner_id).first()
        new_cost = last_bet.cost - deal.step
        if (last_bet.cost > robot.min_limit) and (robot.is_first == True) and (db.query(models.Robot).filter(
                (models.Robot.owner_id == robot.owner_id) and (
                        models.Robot.is_first == False)).first() > robot.last_bet):
            db.query(models.Robot).filter((models.Robot.owner_id == user.id) and (models.Robot.is_first == True)) \
                .update({'last_user_bet': new_cost})
        elif (last_bet.cost > robot.min_limit) and (robot.is_first == False):
            db.query(models.Robot).filter((models.Robot.owner_id == user.id) and (models.Robot.is_first == False)) \
                .update({'last_user_bet': new_cost})
        else:
            notificationSender.say(user.tg_username, config.min_limit_confirmed)


def timer():
    global full_selling_time
    while full_selling_time > 0:
        full_selling_time = full_selling_time - 1
        time.sleep(1)


def set_rules(db: Session, ownerId: int, dealId: int):
    rules.on_send_time(db, ownerId)
    rules.on_selling_type(db, ownerId, dealId)
    if rules.is_duo(db, ownerId):
        pass
    else:
        pass


if __name__ == "__main__":
    pass

import time
from threading import Thread
from database import models
from sqlalchemy.orm import Session
from rules import on_send_time, on_selling_type, is_duo
from notificationSender import say
from config import min_limit_confirmed

full_selling_time = 40
last_step = 1
last_bet_id = 0

robot_1 = 1
robot_2 = 2

player_1 = 4
player_2 = 5


def bots(db: Session, dealId: int):
    robots_list = db.query(models.Robot).filter(
        (models.Robot.deal_id == dealId) and (models.Robot.is_pause == False)).all()
    last_bet = db.query(models.Lastbet).filter(models.Lastbet.last_bet_id == dealId).first()
    deal = db.query(models.Deal).filter(models.Deal.id_deal == dealId).first()
    for robot in robots_list:
        user = db.query(models.User).filter(models.User.id == robot.owner_id).first()
        new_cost = last_bet.cost - deal.step
        if (last_bet.cost > robot.min_limit) and (robot.is_first == True) and (db.query(models.Robot).filter(
        (models.Robot.owner_id == robot.owner_id) and (models.Robot.is_first == False)).first() > robot.last_bet):
            db.query(models.Robot).filter((models.Robot.owner_id == user.id) and (models.Robot.is_first == True)) \
                .update({'last_user_bet': new_cost})
        elif (last_bet.cost > robot.min_limit) and (robot.is_first == False):
            db.query(models.Robot).filter((models.Robot.owner_id == user.id) and (models.Robot.is_first == False))\
                .update({'last_user_bet': new_cost})
        else:
            say(user.tg_username, min_limit_confirmed)


def timer():
    global full_selling_time
    while full_selling_time > 0:
        full_selling_time = full_selling_time - 1
        time.sleep(1)


def game():
    while True:
        if full_selling_time != 0:
            pass
        else:
            print(last_bet_id)


def set_rules(db: Session, ownerId: int, dealId: int):
    on_send_time(db, ownerId)
    on_selling_type(db, ownerId, dealId)
    if is_duo(db, ownerId):
        pass
    else:
        pass



if __name__ == "__main__":
    pass
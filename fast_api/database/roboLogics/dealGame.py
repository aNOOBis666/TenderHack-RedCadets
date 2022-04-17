from threading import Thread
import time
from sqlalchemy.orm import Session
from rules import on_send_time, on_selling_type, is_duo

full_selling_time = 40
last_step = 1
last_bet_id = 0

robot_1 = 1
robot_2 = 2

player_1 = 4
player_2 = 5


def timer():
    global full_selling_time
    while full_selling_time > 0:
        full_selling_time = full_selling_time-1
        time.sleep(1)


def game():
    while True:
        if full_selling_time != 0:

        else:
            print(last_bet_id)




def set_rules(db: Session, ownerId: int, dealId: int):
    on_send_time(db, ownerId)
    on_selling_type(db, ownerId, dealId)
    if is_duo(db, ownerId):

    else:
        second_bot_observer()
#
#
# def second_bot_observer():
#     pass
#
#
# def first_bot_observer():
#     pass


if __name__ == "__main__":
    t = Thread(target=timer)
    g = Thread(target=game)
    t.start(), g.start()

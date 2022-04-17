from sqlalchemy import Column, Integer, String, Boolean, Float

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    email = Column(String)
    surname = Column(String)
    name = Column(String)
    date_creation = Column(String)
    nalog_name = Column(Integer)
    password = Column(String)
    role = Column(String)
    tg_username = Column(String)


class Deal(Base):
    __tablename__ = "deal"

    id_deal = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name_deal = Column(String)
    description_deal = Column(String)
    date_deal = Column(String)
    owner_id = Column(Integer)
    first_place_id = Column(Integer)
    second_place_id = Column(Integer)
    status_deal = Column(String)
    start_price = Column(Integer)
    step = Column(Float)
    finish_time = Column(String)


class Lastbet(Base):
    __tablename__ = "Lastbet"

    id_bet = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    last_bet_id = Column(Integer)
    last_date_time = Column(String)
    last_user_bet = Column(Integer)
    cost = Column(Float)


class Notifications(Base):
    __tablename__ = "notifications"

    id_notification = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_preference = Column(String)
    notification_type = Column(Integer)
    owner_id = Column(Integer)


class Robot(Base):
    __tablename__ = "Robot"

    robot_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    owner_id = Column(Integer)
    deal_id = Column(Integer)
    min_limit = Column(Float)
    send_time = Column(Integer)
    selling_type = Column(Integer)

    last_bet = Column(Float)
    delay = Column(Integer)

    is_first = Column(Boolean)
    is_pause = Column(Boolean)
    is_stop = Column(Boolean)
    is_smart_duo = Column(Boolean)
    is_human = Column(Boolean)


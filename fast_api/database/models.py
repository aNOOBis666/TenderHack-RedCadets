from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String)
    surname = Column(String)
    name = Column(String)
    date_creation = Column(String)
    nalog_name = Column(Integer)
    password = Column(String)
    role = Column(String)


class Deal(Base):
    __tablename__ = "deal"

    id_deal = Column(Integer, primary_key=True, unique=True)
    name_deal = Column(String)
    description_deal = Column(String)
    date_deal = Column(String)
    owner_id = Column(Integer)
    first_place_id = Column(Integer)
    second_place_id = Column(Integer)
    status_deal = Column(String)
    start_price = Column(Integer)


class Lastbet(Base):
    __tablename__ = "Lastbet"

    id_bet = Column(Integer, primary_key=True, unique=True)
    last_bet_id = Column(Integer)
    last_date_time = Column(DateTime)
    last_user_bet = Column(Integer)


class Notifications(Base):
    __tablename__ = "notifications"

    id_notification = Column(Integer, primary_key=True, unique=True)
    user_preference = Column(String)
    notification_type = Column(Integer)
    owner_id = Column(Integer)

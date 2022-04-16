from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    surname = Column(String)
    name = Column(String)
    date_creation = Column(DateTime)
    nalog_name = Column(Integer, ForeignKey(""))
    password = Column(String)
    role = Column(String)

    #items = relationship("Categories", back_populates="owner")
    #profile = relationship("Profile", back_populates="event")


class Deal(Base):
    __tablename__ = "deal"

    id_deal = Column(Integer, primary_key=True, index=True)
    name_deal = Column(String)
    description_deal = Column(String)
    date_deal = Column(DateTime)
    owner_id = Column(Integer)
    first_place_id = Column(Integer)
    second_place_id = Column(Integer)
    status_deal = Column(String)
    start_price = Column(Integer)

    owner = relationship("Events", back_populates="items")


class Lastbet(Base):
    __tablename__ = "lastbet"

    last_bet_id = Column(Integer, ForeignKey("deal.id_deal"))
    
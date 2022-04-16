from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class Events(Base):
    __tablename__ = "events"

    id_event = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    coords = Column(String)
    date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    event_id = Column(Integer, ForeignKey("profile.id_profile"))

    items = relationship("Categories", back_populates="owner")
    profile = relationship("Profile", back_populates="event")


class Categories(Base):
    __tablename__ = "categories"

    id_categories = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("events.id_event"))

    owner = relationship("Events", back_populates="items")


class Profile(Base):
    __tablename__ = "profile"

    id_profile = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    name = Column(String)
    password = Column(String)
    photo = Column(String)
    description = Column(String)
    rating_deals = Column(Integer)
    rating_events = Column(Integer)

    event = relationship("Events", back_populates="profile")
    inspections = relationship("Inspections", back_populates="profile")
    # messages_list = relationship("MessagesList", back_populates="profile")


# Pattern for next versions


class Inspections(Base):
    __tablename__ = "inspections"

    id_inspections = Column(Integer, primary_key=True, index=True)

    profile_banned = Column(Boolean, default=False)
    event_banned = Column(Boolean, default=False)
    profile_id = Column(Integer, ForeignKey("profile.id_profile"))

    profile = relationship("Profile", back_populates="inspections")


from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/dealsList/", response_model=List[schemas.Deals])
def read_deals(db: Session = Depends(get_db)):
    dealsList = crud.get_deals(db)
    return dealsList


@app.get("/deal/", response_model=schemas.Deals)
def read_deal_by_id(deal_id: int, db: Session = Depends(get_db)):
    deal = crud.get_deal_by_id(db, deal_id)
    return deal


@app.post("/deal/", response_model=schemas.Deals)
def post_deal(deal_id: int, category: schemas.DealCreate, db: Session = Depends(get_db)):
    deal_created = crud.create_deal(category, db, deal_id)
    return deal_created


@app.get("/usersList/", response_model=List[schemas.Users])
def read_users(db: Session = Depends(get_db)):
    dealsList = crud.get_users(db)
    return dealsList


@app.get("/user/", response_model=schemas.Users)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    return user


@app.post("/user/", response_model=schemas.Users)
def post_user(user_id: int, category: schemas.UserCreate, db: Session = Depends(get_db)):
    user_created = crud.create_user(category, db, user_id=user_id)
    return user_created


@app.get("/last_bet/", response_model=schemas.LastBets)
def read_last_bet_by_id(deal_id: int, db: Session = Depends(get_db)):
    deal = crud.get_last_bet_by_id(db, deal_id)
    return deal


# @app.post("/last_bet/", response_model=schemas.LastBets)
# def update_last_bet(deal_id: int, category: schemas.LastBetsCreate, db: Session = Depends(get_db)):
#     deal_created = crud.update_last_bet(category, db, deal_id)
#     return deal_created


@app.get("/notifications/", response_model=schemas.Notifications)
def read_notifications_by_user_id(user_id: int, db: Session = Depends(get_db)):
    notification = crud.get_notifications_by_user_id(db, user_id)
    return notification


@app.post("/notifications/", response_model=schemas.Notifications)
def post_user(owner_id: int, category: schemas.NotificationsCreate, db: Session = Depends(get_db)):
    notif_created = crud.create_notification(category, db, owner_id)
    return notif_created

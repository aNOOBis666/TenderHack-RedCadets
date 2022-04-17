from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5500"
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
def post_deal(category: schemas.DealCreate, db: Session = Depends(get_db)):
    deal_created = crud.create_deal(category, db)
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
def post_user(category: schemas.UserCreate, db: Session = Depends(get_db)):
    user_created = crud.create_user(category, db)
    return user_created


@app.get("/last_bet/", response_model=schemas.LastBets)
def read_last_bet_by_id(deal_id: int, db: Session = Depends(get_db)):
    deal = crud.get_last_bet_by_id(db, deal_id)
    return deal


@app.post("/last_bet/", response_model=schemas.LastBets)
def update_last_bet(deal_id: int, category: schemas.LastBetsCreate, db: Session = Depends(get_db)):
    crud.update_last_bet(category, db, deal_id)


@app.get("/notifications/", response_model=schemas.Notifications)
def read_notifications_by_user_id(user_id: int, db: Session = Depends(get_db)):
    notification = crud.get_notifications_by_user_id(db, user_id)
    return notification


@app.post("/notifications/", response_model=schemas.Notifications)
def post_user(category: schemas.NotificationsCreate, db: Session = Depends(get_db)):
    notif_created = crud.create_notification(category, db)
    return notif_created

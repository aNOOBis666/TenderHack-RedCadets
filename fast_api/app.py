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
def post_deal(id_deal: int, name_deal: str, description_deal: str, date_deal: str, owner_id: int, first_place_id: int,
              second_place_id: int, status_deal: str, start_price: int,
              category: schemas.DealCreate, db: Session = Depends(get_db)):
    deal_created = crud.create_deal(category, db, id_deal, name_deal, description_deal, date_deal, owner_id,
                                    first_place_id, second_place_id, status_deal, start_price)
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
def post_user(id: int, email: str, surname: str, name: str, date_creation: str, nalog_name: int, password: str,
              role: str, category: schemas.UserCreate, db: Session = Depends(get_db)):
    user_created = crud.create_user(category, db, id=id, email=email, surname=surname, name=name,
                                    date_creation=date_creation, nalog_name=nalog_name, password=password, role=role)
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
def post_user(owner_id: int, id_notification: int, user_preference: str, notification_type: str,
              category: schemas.NotificationsCreate, db: Session = Depends(get_db)):
    notif_created = crud.create_notification(category, db, owner_id=owner_id, id_notification=id_notification,
                                             user_preference=user_preference, notification_type=notification_type)
    return notif_created

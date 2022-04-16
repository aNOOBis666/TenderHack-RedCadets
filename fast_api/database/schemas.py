from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    role: str
    name: str
    surname: str
    email: str
    password: str
    nalog_name: int
    date_creation: str


class UserCreate(UserBase):
    pass


class Users(UserBase):
    pass

    class Config:
        orm_mode = True


class DealBase(BaseModel):
    id_deal: int
    name_deal: str
    description_deal: str
    date_deal: str
    owner_id: int
    first_place_id: int
    second_place_id: int
    status_deal: str
    start_price: str


class DealCreate(DealBase):
    pass


class Deals(DealBase):
    pass

    class Config:
        orm_mode = True


class LastBetBase(BaseModel):
    id_bet: int
    last_bet_id: int
    last_date_time: str
    last_user_bet: int


class LastBetsCreate(LastBetBase):
    pass


class LastBets(LastBetBase):
    pass

    class Config:
        orm_mode = True


class NotificationsBase(BaseModel):
    id_notification: int
    user_preference: str
    notification_type: int
    owner_id: int


class NotificationsCreate(NotificationsBase):
    pass


class Notifications(NotificationsBase):
    pass

    class Config:
        orm_mode = True
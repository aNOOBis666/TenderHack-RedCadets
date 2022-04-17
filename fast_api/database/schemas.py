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
    tg_username: str


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
    start_price: int
    step: float
    finish_time: str


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
    cost: float


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


class RobotBase(BaseModel):
    robot_id: int
    owner_id: int
    deal_id: int
    min_limit: float
    send_time: int
    selling_type: int
    last_bet: float
    delay: int
    is_first: bool
    is_pause: bool
    is_stop: bool
    is_smart_duo: bool
    is_human: bool


class RobotCreate(RobotBase):
    pass


class RobotSwap(RobotBase):
    pass


class Robot(RobotBase):
    pass

    class Config:
        orm_mode = True
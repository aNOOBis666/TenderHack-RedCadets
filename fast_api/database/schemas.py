from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    pass


class Users(UserBase):
    pass

    class Config:
        orm_mode = True


class DealBase(BaseModel):
    pass


class DealCreate(DealBase):
    pass


class Deals(DealBase):
    pass

    class Config:
        orm_mode = True


class LastBetBase(BaseModel):
    pass


class LastBetsCreate(LastBetBase):
    pass


class LastBets(LastBetBase):
    pass

    class Config:
        orm_mode = True


class NotificationsBase(BaseModel):
    pass


class NotificationsCreate(NotificationsBase):
    pass


class Notifications(NotificationsBase):
    pass

    class Config:
        orm_mode = True
from datetime import datetime
from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    # password: str
    created_at: datetime

    class Config:
        orm_mode: bool = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode: bool = True

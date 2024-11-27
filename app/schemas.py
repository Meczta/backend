from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str 


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_deleted: bool

    class Config:
        orm_mode = True


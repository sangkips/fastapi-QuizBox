from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_active: bool | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

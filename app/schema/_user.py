from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserEdit(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

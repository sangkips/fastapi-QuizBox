from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(UserSchema):
    password: str = Field(..., min_length=6)


class UserUpdate(UserSchema):
    email: EmailStr
    first_name: str
    last_name: str


class UserDB(UserSchema):
    id: int

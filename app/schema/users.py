from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str | None = None
    is_active: bool | None = None

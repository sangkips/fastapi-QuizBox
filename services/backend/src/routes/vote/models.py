import enum
from pydantic import BaseModel
from sqlalchemy import Enum


class VoteSchema(BaseModel):
    question_id: int | None = None
    answer_id: int | None = None
    user_id: int
    like: int


class VoteCreate(VoteSchema):
    ...


class Like(enum.IntEnum):
    down = 1
    up = 2


class VoteDB(VoteSchema):
    id: int

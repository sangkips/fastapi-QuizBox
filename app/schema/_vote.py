from pydantic import BaseModel


class VoteBase(BaseModel):
    question_id: int | None = None
    answer_id: int | None = None
    user_id: int
    like: int


class VoteCreate(VoteBase):
    ...


class Vote(VoteBase):
    id: int

    class Config:
        orm_mode = True

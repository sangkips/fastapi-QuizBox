from pydantic import BaseModel


class VoteBase(BaseModel):
    question_id: int
    answer_id: int
    user_id: int
    like: int


class VoteCreate(VoteBase):
    ...


class Vote(VoteBase):
    id: int

    class Config:
        orm_mode = True

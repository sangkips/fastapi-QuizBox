from pydantic import BaseModel


class AnswerBase(BaseModel):
    body: str
    user_id: int
    vote_id: int
    question_id: int


class AnswerCreate(AnswerBase):
    ...


class Answer(AnswerBase):
    id: int

    class Config:
        orm_mode = True

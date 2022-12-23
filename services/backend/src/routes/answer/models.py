from pydantic import BaseModel


class AnswerSchema(BaseModel):
    body: str
    user_id: int
    question_id: int


class AnswerCreate(AnswerSchema):
    ...


class AnswerEdit(AnswerSchema):
    body: str


class AnswerDB(AnswerSchema):
    id: int

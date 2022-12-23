from pydantic import BaseModel


class QuestionSchema(BaseModel):
    title: str
    body: str
    user_id: int
    tag_id: int


class QuestionCreate(QuestionSchema):
    ...


class QuestionEdit(QuestionSchema):
    title: str
    body: str


class QuestionDB(QuestionSchema):
    id: int

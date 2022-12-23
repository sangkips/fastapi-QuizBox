from pydantic import BaseModel


class TagSchema(BaseModel):
    name: str


class TagDB(TagSchema):
    id: int

from src.routes.question.models import QuestionSchema, QuestionCreate, QuestionEdit
from src.db_connect import database, questions


async def get_all():
    query = questions.select()
    return await database.fetch_all(query=query)


async def get(id: int):
    query = questions.select().where(id == questions.c.id)
    return await database.fetch_one(query=query)


async def post(payload: QuestionCreate):
    query = questions.insert().values(title=payload.title, body=payload.body)

    return await database.execute(query=query)


async def put(id: int, payload: QuestionEdit):
    query = questions.update().where(id == questions.c.id).values(
        title=payload.title, body=payload.body).returning(questions.c.id)

    return await database.execute(query=query)


async def delete(id: int):
    query = questions.delete().where(id == questions.c.id)
    return await database.execute(query=query)

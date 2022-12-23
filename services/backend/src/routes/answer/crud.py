from src.routes.answer.models import AnswerCreate, AnswerEdit, AnswerDB
from src.db_connect import database, answers


async def get_all():
    query = answers.select()
    return await database.fetch_all(query=query)


async def get(id: int):
    query = answers.select().where(id == answers.c.id)
    return await database.fetch_one(query=query)


async def post(payload: AnswerCreate):
    query = answers.insert().values(body=payload.body)

    return await database.execute(query=query)


async def put(id: int, payload: AnswerEdit):
    query = answers.update().where(id == answers.c.id).values(
        body=payload.body).returning(answers.c.id)

    return await database.execute(query=query)


async def delete(id: int):
    query = answers.delete().where(id == answers.c.id)
    return await database.execute(query=query)

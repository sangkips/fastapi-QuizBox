from src.routes.vote.models import VoteSchema, VoteDB
from src.db_connect import database, votes


async def get_all():
    query = votes.select()
    return await database.fetch_all(query=query)


async def get(id: int):
    query = votes.select().where(id == votes.c.id)
    return await database.fetch_one(query=query)


async def post(payload: VoteSchema):
    query = votes.insert().values(email=payload.email, first_name=payload.first_name,
                                  last_name=payload.last_name, password=payload.password)
    return await database.execute(query=query)


async def put(id: int, payload: VoteDB):
    query = votes.update().where(id == votes.c.id).values(
        email=payload.email,
        first_name=payload.first_name,
        last_name=payload.last_name).returning(votes.c.id)

    return await database.execute(query=query)


async def delete(id: int):
    query = votes.delete().where(id == votes.c.id)
    return await database.execute(query=query)

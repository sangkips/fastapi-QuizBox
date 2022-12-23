from src.routes.tag.models import TagSchema
from src.db_connect import database, tags


async def get_all():
    query = tags.select()
    return await database.fetch_all(query=query)


async def get(id: int):
    query = tags.select().where(id == tags.c.id)
    return await database.fetch_one(query=query)


async def post(payload: TagSchema):
    query = tags.insert().values(name=payload.name)

    return await database.execute(query=query)


async def put(id: int, payload: TagSchema):
    query = tags.update().where(id == tags.c.id).values(
        name=payload.name).returning(tags.c.id)

    return await database.execute(query=query)


async def delete(id: int):
    query = tags.delete().where(id == tags.c.id)
    return await database.execute(query=query)

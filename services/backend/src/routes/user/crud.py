from src.routes.user.models import UserSchema, UserUpdate, UserCreate
from src.db_connect import database, users


async def get_all():
    query = users.select()
    return await database.fetch_all(query=query)


async def get(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query=query)


async def post(payload: UserSchema):
    query = users.insert().values(email=payload.email, first_name=payload.first_name,
                                  last_name=payload.last_name, password=payload.password)
    return await database.execute(query=query)


async def put(id: int, payload: UserUpdate):
    query = users.update().where(id == users.c.id).values(
        email=payload.email,
        first_name=payload.first_name,
        last_name=payload.last_name).returning(users.c.id)

    return await database.execute(query=query)


async def delete(id: int):
    query = users.delete().where(id == users.c.id)
    return await database.execute(query=query)

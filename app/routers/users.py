import fastapi
from app.schema.users import User

router = fastapi.APIRouter()


@router.get("/users", tags=["Users"])
async def get_all_users():
    pass


@router.get("/users, {user_id}", tags=["Users"])
async def get_single_user():
    pass


@router.post("/users", tags=["Users"])
async def create_user(user: User):
    pass


@router.put("/users, {user_id}", tags=["Users"])
async def update_user(user: User):
    pass


@router.delete("/users, {user_id}", tags=["Users"])
async def delete_user(user: User):
    pass

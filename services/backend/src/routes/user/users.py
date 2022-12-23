from typing import List

from fastapi import APIRouter, HTTPException, Path, status

from src.routes.user import crud
from src.routes.user.models import UserCreate, UserDB, UserUpdate

router = APIRouter()


@router.get("/", response_model=List[UserDB])
async def read_all_users():
    return await crud.get_all()


@router.get("/{id}/", response_model=UserDB, status_code=200)
async def read_user(id: int = Path(..., gt=0),):
    user = await crud.get(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/", response_model=UserDB, status_code=201)
async def create_user(payload: UserCreate):
    user_id = await crud.post(payload)

    response_object = {
        "id": user_id,
        "email": payload.email,
        "first_name": payload.first_name,
        "first_name": payload.first_name,
        "password": payload.password,

    }
    return response_object


@router.put("/{id}", response_model=UserDB)
async def update_user(id: int, payload: UserUpdate):
    user = await crud.get(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = await crud.put(id, payload)

    response_object = {
        "id": user_id,
        "email": payload.email,
        "first_name": payload.first_name,
        "last_name": payload.last_name,

    }
    return response_object


@router.delete("/{id}", response_model=UserDB, status_code=status.HTTP_202_ACCEPTED)
async def delete_user(id: int):
    user = await crud.get(id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    await crud.delete(id)
    return user

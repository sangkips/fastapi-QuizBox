import fastapi
from fastapi import Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session


from app.schema._user import UserCreate, User
from app.utils.user_crud import get_user, get_user_by_email, get_users, create_user
from app.db.database import get_db


router = fastapi.APIRouter()

# get all users from the database(100 records at a time)
@router.get("/users", response_model=List[User], tags=["Users"])
async def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


# get a single user by id
@router.get("/user/{user_id}", tags=["Users"])
async def get_single_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist"
        )
    return user


# create a new user
@router.post(
    "/user", response_model=User, tags=["Users"], status_code=status.HTTP_201_CREATED
)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = get_user_by_email(db=db, email=user.email)
    if new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with email already exist.",
        )
    return create_user(db=db, user=user)


# update user based on a given id
@router.put("/users, {user_id}", tags=["Users"])
async def update_user():
    pass


# delete user
@router.delete(
    "/users, {user_id}", tags=["Users"], status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user():
    pass

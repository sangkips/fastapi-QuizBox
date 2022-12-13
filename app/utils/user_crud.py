from sqlalchemy.orm import Session
from app.models.users import User
from app.schema._user import UserCreate, UserEdit


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = user.password
    db_user = User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# update user crud
def edit_user(db: Session, user_id: int, user: UserEdit):
    db_user = get_user(db, user_id)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# delete user
def delete_user(db: Session, user_id: int):
    user = get_user(db=db, user_id=user_id)

    db.delete(user)
    db.commit()
    return user

from sqlalchemy.orm import Session
from app.models.users import User
from app.schema._user import UserCreate


def get_user(db: Session, user_id: int):
    user_query = db.query(User).filter(User.id == user_id).first()
    return user_query


def get_user_by_email(db: Session, email: str):
    email_query = db.query(User).filter(User.email == email).first()
    return email_query


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = user.password
    db_user = User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

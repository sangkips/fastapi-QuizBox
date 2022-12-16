from sqlalchemy.orm import Session
from app.backend.models.votes import Vote
from app.backend.schema._vote import VoteCreate


def get_vote(db: Session, user_id: int):
    return db.query(Vote).filter(Vote.id == user_id).first()


def get_votes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vote).offset(skip).limit(limit).all()


def create_vote(db: Session, vote: VoteCreate):
    db_vote = Vote(**vote.dict())
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote

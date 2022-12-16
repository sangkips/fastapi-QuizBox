from sqlalchemy.orm import Session
from app.backend.models.answers import Answer
from app.backend.schema._answer import AnswerCreate


def get_answer(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.id == answer_id).first()


def get_answers(db: Session):
    return db.query(Answer).all()


def create_answer(db: Session, answer: AnswerCreate):
    db_answer = Answer(
        body=answer.body,
        user_id=answer.user_id,
        vote_id=answer.vote_id,
        question_id=answer.question_id,
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def get_user_answers(db: Session, user_id: int):
    return db.query(Answer).filter(Answer.user_id == user_id).all()

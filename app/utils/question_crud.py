from sqlalchemy.orm import Session
from app.models.questions import Question
from app.schema._question import QuestionCreate


def get_question(db: Session, question_id: int):
    question_query = db.query(Question).filter(Question.id == question_id).first()
    return question_query


def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Question).offset(skip).limit(limit).all()


def create_question(db: Session, question: QuestionCreate):
    db_question = Question(
        title=question.title,
        body=question.body,
        user_id=question.user_id,
        tag_id=question.tag_id,
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

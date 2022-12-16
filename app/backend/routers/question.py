import fastapi
from fastapi import Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session


from app.backend.schema._question import QuestionCreate, Question, QuestionEdit
from app.backend.utils.question_crud import get_question, get_questions, create_question
from app.backend.db.database import get_db

router = fastapi.APIRouter()


@router.get(
    "/questions",
    response_model=list[Question],
    tags=["Questions"],
    status_code=status.HTTP_200_OK,
)
async def get_all_questions(db: Session = Depends(get_db)):
    questions = get_questions(db=db)
    return questions


@router.get("/api/v1/questions/{question_id}", tags=["Questions"])
async def get_single_question(question_id: int, db: Session = Depends(get_db)):
    question = get_question(db=db, question_id=question_id)
    if question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question not found"
        )
    return question


@router.post(
    "/api/v1/questions",
    response_model=Question,
    tags=["Questions"],
    status_code=status.HTTP_201_CREATED,
)
async def create_new_question(question: QuestionCreate, db: Session = Depends(get_db)):
    new_question = create_question(db=db, question=question)
    return new_question


@router.patch("/api/v1/questions/{question_id}", tags=["Questions"])
async def update_question(question: QuestionEdit, db: Session = Depends(get_db)):
    question_to_update = Question(db, question)
    if question_to_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question does not exist"
        )
    return question_to_update


@router.delete(
    "/api/v1/questions/{question_id}",
    tags=["Questions"],
)
async def delete_question(question_id: int, db: Session = Depends(get_db)):
    question = get_question(db, question_id)
    if question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question does not exist"
        )
    db.delete(question)
    db.commit()

    return {"message": "Successfully deleted the question"}

import fastapi
from fastapi import Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session


from app.schema._question import QuestionCreate, Question
from app.utils.question_crud import get_question, get_questions, create_question
from app.db.database import get_db

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


@router.get("/questions, {question_id}", tags=["Questions"])
async def get_single_question():
    pass


@router.post(
    "/questions",
    response_model=Question,
    tags=["Questions"],
    status_code=status.HTTP_201_CREATED,
)
async def create_new_question(question: QuestionCreate, db: Session = Depends(get_db)):
    new_question = create_question(db=db, question=question)
    return new_question


@router.put("/questions, {question_id}", tags=["Questions"])
async def update_question():
    pass


@router.delete("/questions, {question_id}", tags=["Questions"])
async def delete_question():
    pass

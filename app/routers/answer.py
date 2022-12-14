import fastapi
from fastapi import Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session


from app.schema._answer import AnswerCreate, Answer
from app.utils.answer_crud import get_answer, get_answers, create_answer
from app.db.database import get_db


router = fastapi.APIRouter()


@router.get("/api/v1/answers", response_model=List[Answer], tags=["Answers"])
async def get_all_answers(db: Session = Depends(get_db)):
    answers = get_answers(db=db)
    return answers


@router.get("/api/v1/answers/{answer_id}", response_model=Answer, tags=["Answers"])
async def get_single_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = get_answer(db=db, answer_id=answer_id)
    if answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Answer not in the database"
        )
    return answer


@router.post("/api/v1/answers", response_model=Answer, tags=["Answers"])
async def create_new_answer(answer: AnswerCreate, db: Session = Depends(get_db)):
    new_answer = create_answer(db=db, answer=answer)
    return new_answer


@router.put("/api/v1/answers/{answer_id}", tags=["Answers"])
async def update_answer():
    pass


@router.delete("/api/v1/answers/{answer_id}", response_model=Answer, tags=["Answers"])
async def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = get_answer(db, answer_id)
    if answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Answer does not exist"
        )
    db.delete(answer)
    db.commit()
    db.refresh(answer)
    return {"Detail": "Deletion successfull"}

from typing import List

from fastapi import APIRouter, HTTPException, status, Path

from src.routes.question import crud
from src.routes.question.models import QuestionDB, QuestionCreate, QuestionEdit

router = APIRouter()


@router.get("/", response_model=List[QuestionDB], status_code=status.HTTP_200_OK)
async def read_all_questions():
    return await crud.get_all()


@router.get("/{id}/", response_model=QuestionDB, status_code=status.HTTP_200_OK)
async def read_questions(id: int = Path(..., gt=0),):
    question = await crud.get(id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    return question


@router.post("/", response_model=QuestionDB, status_code=status.HTTP_201_CREATED)
async def create_question(payload: QuestionCreate):
    question_id = await crud.post(payload)

    response_object = {
        "id": question_id,
        "title": payload.title,
        "body": payload.body,

    }
    return response_object


@router.put("/{id}", response_model=QuestionDB, status_code=status.HTTP_202_ACCEPTED)
async def update_question(payload: QuestionEdit, id: int = Path(..., gt=0),):
    question = await crud.get(id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    question_id = await crud.put(id, payload)

    response_object = {
        "id": question_id,
        "title": payload.title,
        "body": payload.body,

    }
    return response_object


@router.delete("/{id}", response_model=QuestionDB, status_code=status.HTTP_202_ACCEPTED)
async def delete_question(id: int = Path(..., gt=0),):
    question = await crud.get(id)
    if question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    await crud.delete(id)
    return question

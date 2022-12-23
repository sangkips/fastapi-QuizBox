from typing import List

from fastapi import APIRouter, HTTPException, status

from src.routes.answer import crud
from src.routes.answer.models import AnswerDB, AnswerCreate, AnswerEdit

router = APIRouter()


@router.get("/", response_model=List[AnswerDB])
async def read_all_answers():
    return await crud.get_all()


@router.get("/{id}/", response_model=AnswerDB, status_code=200)
async def read_answer(id: int):
    answer = await crud.get(id)
    if answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")

    return answer


@router.post("/", response_model=AnswerDB, status_code=201)
async def create_answer(payload: AnswerCreate):
    answer_id = await crud.post(payload)

    response_object = {
        "id": answer_id,
        "body": payload.body,

    }
    return response_object


@router.put("/{id}", response_model=AnswerDB)
async def update_answer(id: int, payload: AnswerEdit):
    answer = await crud.get(id)
    if answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")

    answer_id = await crud.put(id, payload)

    response_object = {
        "id": answer_id,
        "body": payload.body,

    }
    return response_object


@router.delete("/{id}", response_model=AnswerDB, status_code=status.HTTP_202_ACCEPTED)
async def delete_answer(id: int):
    answer = await crud.get(id)
    if answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Answer not found")

    await crud.delete(id)
    return answer

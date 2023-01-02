from typing import List

from fastapi import APIRouter, HTTPException, Path, status

from src.routes.vote import crud
from src.routes.vote.models import VoteCreate, VoteDB

router = APIRouter()


@router.get("/", response_model=List[VoteDB])
async def read_all_votes():
    return await crud.get_all()


@router.get("/{id}/", response_model=VoteDB, status_code=200)
async def read_vote(id: int = Path(..., gt=0),):
    vote = await crud.get(id)
    if vote is None:
        raise HTTPException(status_code=404, detail="vote not found")

    return vote


@router.post("/", response_model=VoteDB, status_code=201)
async def create_vote(payload: VoteCreate):
    vote_id = await crud.post(payload)

    response_object = {
        "id": vote_id,
        "question_id": payload.question_id,
        "answer_id": payload.answer_id,
        "user_id": payload.user_id,
        "like": payload.like,

    }
    return response_object


@router.put("/{id}", response_model=VoteDB)
async def update_vote(id: int, payload: VoteDB):
    vote = await crud.get(id)
    if vote is None:
        raise HTTPException(status_code=404, detail="vote not found")

    vote_id = await crud.put(id, payload)

    response_object = {
        "id": vote_id,
        "question_id": payload.question_id,
        "answer_id": payload.answer_id,
        "user_id": payload.user_id,
        "like": payload.like,

    }
    return response_object


@router.delete("/{id}", response_model=VoteDB, status_code=status.HTTP_202_ACCEPTED)
async def delete_vote(id: int):
    vote = await crud.get(id)
    if vote is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="vote not found")

    await crud.delete(id)
    return vote

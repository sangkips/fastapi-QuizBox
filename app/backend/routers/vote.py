import fastapi

from fastapi import Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session

from schema._vote import VoteCreate, Vote
from utils.vote_crud import (
    get_vote,
    get_votes,
    create_vote,
)
from db.database import get_db

router = fastapi.APIRouter()


@router.get("/api/v1/votes", response_model=List[Vote], tags=["votes"])
async def get_all_votes(db: Session = Depends(get_db)):
    return get_votes(db=db)


@router.get(
    "/api/v1/votes/{vote_id}",
    response_model=Vote,
    tags=["votes"],
    status_code=status.HTTP_200_OK,
)
async def get_single_vote(vote_id: int, db: Session = Depends(get_db)):
    return get_vote(db=db, vote_id=vote_id)


@router.post(
    "/api/v1/votes",
    response_model=Vote,
    tags=["votes"],
    status_code=status.HTTP_201_CREATED,
)
async def create_vote_record(vote: VoteCreate, db: Session = Depends(get_db)):
    return create_vote(db=db, vote=vote)


@router.put("/votes, {vote_id}", tags=["votes"])
async def update_vote():
    pass


@router.delete("/api/v1/votes/{vote_id}", tags=["votes"])
async def delete_vote(vote_id: int, db: Session = Depends(get_db)):
    vote = get_vote(db, vote_id)

    db.delete(vote)
    db.commit()
    db.refresh(vote)

    return {"message": " Delete successful"}

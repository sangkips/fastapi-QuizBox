import fastapi

from fastapi import Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session


from app.schema._tag import TagCreate, Tag
from app.utils.tag_crud import get_tag, create_tag, get_tags
from app.db.database import get_db


router = fastapi.APIRouter()


@router.get(
    "/api/v1/tags",
    response_model=List[Tag],
    tags=["Tags"],
    status_code=status.HTTP_200_OK,
)
async def get_all_tags(db: Session = Depends(get_db)):
    return get_tags(db=db)


@router.get("/api/v1/tags/{tag_id}", tags=["Tags"])
async def get_single_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Tag not found"
        )
    return db_tag


@router.post(
    "api/v1/tags",
    response_model=Tag,
    status_code=status.HTTP_201_CREATED,
    tags=["Tags"],
)
async def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = create_tag(db=db, tag=tag)
    return db_tag


@router.put("/tags, {tag_id}", tags=["Tags"])
async def update_tag():
    pass


@router.delete("/tags, {tag_id}", tags=["Tags"])
async def delete_tag():
    pass

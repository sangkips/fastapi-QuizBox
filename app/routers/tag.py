import fastapi

from fastapi import Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session


from app.schema._tag import TagCreate, Tag
from app.utils.tag_crud import get_tag, create_tag, get_tags, update_tag
from app.db.database import get_db


router = fastapi.APIRouter()

# retrieve all tags from the database
@router.get(
    "/api/v1/tags",
    response_model=List[Tag],
    tags=["Tags"],
    status_code=status.HTTP_200_OK,
)
async def get_all_tags(db: Session = Depends(get_db)):
    return get_tags(db=db)


# get tag by its id
@router.get("/api/v1/tags/{tag_id}", tags=["Tags"])
async def get_single_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Tag not found"
        )
    return db_tag


# create new tag and post to the database
@router.post(
    "api/v1/tags",
    response_model=Tag,
    status_code=status.HTTP_201_CREATED,
    tags=["Tags"],
)
async def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = create_tag(db=db, tag=tag)
    return db_tag


# update single tag by id
@router.put(
    "/api/v1/tags, {tag_id}",
    response_model=Tag,
    tags=["Tags"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_current_tag(tag: Tag, db: Session = Depends(get_db)):
    updated_tag = update_tag(db=db, name=tag.name)

    return updated_tag


# delete a given tag using its id
@router.delete(
    "/api/v1/tags/{tag_id}",
    response_model=Tag,
    tags=["Tags"],
)
async def delete_tag():
    pass

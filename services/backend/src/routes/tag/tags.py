from typing import List

from fastapi import APIRouter, HTTPException, status, Path

from src.routes.tag import crud
from src.routes.tag.models import TagSchema, TagDB

router = APIRouter()


@router.get("/", response_model=List[TagDB])
async def read_all_tags():
    return await crud.get_all()


@router.get("/{id}/", response_model=TagDB, status_code=200)
async def read_tag(id: int = Path(..., gt=0),):
    tag = await crud.get(id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    return tag


@router.post("/", response_model=TagDB, status_code=201)
async def create_tag(payload: TagSchema):
    tag_id = await crud.post(payload)

    response_object = {
        "id": tag_id,
        "name": payload.name,

    }
    return response_object


@router.put("/{id}", response_model=TagDB)
async def update_tag(payload: TagSchema, id: int = Path(..., gt=0),):
    tag = await crud.get(id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    tag_id = await crud.put(id, payload)

    response_object = {
        "id": tag_id,
        "name": payload.name,

    }
    return response_object


@router.delete("/{id}", response_model=TagDB, status_code=status.HTTP_202_ACCEPTED)
async def delete_tag(id: int = Path(..., gt=0),):
    tag = await crud.get(id)
    if tag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")

    await crud.delete(id)
    return tag

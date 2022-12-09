import fastapi


router = fastapi.APIRouter()

tags = []


@router.get("/tags", tags=["Tags"])
async def get_all_tags():
    return tags


@router.get("/tags, {tag_id}", tags=["Tags"])
async def get_single_tag(tag_id: int):
    return tags[tag_id]


@router.post("/tags", tags=["Tags"])
async def create_tag():
    pass


@router.put("/tags, {tag_id}", tags=["Tags"])
async def update_tag():
    pass


@router.delete("/tags, {tag_id}", tags=["Tags"])
async def delete_tag():
    pass

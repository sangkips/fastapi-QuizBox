import fastapi


router = fastapi.APIRouter()


@router.get("/tags", tags=["Tags"])
async def get_all_tags():
    pass


@router.get("/tags, {tag_id}", tags=["Tags"])
async def get_single_tag():
    pass


@router.post("/tags", tags=["Tags"])
async def create_tag():
    pass


@router.put("/tags, {tag_id}", tags=["Tags"])
async def update_tag():
    pass


@router.delete("/tags, {tag_id}", tags=["Tags"])
async def delete_tag():
    pass

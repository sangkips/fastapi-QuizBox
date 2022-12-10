import fastapi


router = fastapi.APIRouter()


@router.get("/votes", votes=["votes"])
async def get_all_votes():
    pass


@router.get("/votes, {vote_id}", votes=["votes"])
async def get_single_vote(vote_id: int):
    pass


@router.post("/votes", votes=["votes"])
async def create_vote():
    pass


@router.put("/votes, {vote_id}", votes=["votes"])
async def update_vote():
    pass


@router.delete("/votes, {vote_id}", votes=["votes"])
async def delete_vote():
    pass

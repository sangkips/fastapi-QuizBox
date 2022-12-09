import fastapi


router = fastapi.APIRouter()


@router.get("/answers", tags=["Answers"])
async def get_all_answers():
    pass


@router.get("/answers, {answer_id}", tags=["Answers"])
async def get_single_answer():
    pass


@router.post("/answers", tags=["Answers"])
async def create_answer():
    pass


@router.put("/answers, {answer_id}", tags=["Answers"])
async def update_answer():
    pass


@router.delete("/answers, {answer_id}", tags=["Answers"])
async def delete_answer():
    pass

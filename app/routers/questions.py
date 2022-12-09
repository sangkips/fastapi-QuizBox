import fastapi


router = fastapi.APIRouter()


@router.get("/questions", tags=["Questions"])
async def get_all_questions():
    pass


@router.get("/questions, {answer_id}", tags=["Questions"])
async def get_single_answer():
    pass


@router.post("/questions", tags=["Questions"])
async def create_answer():
    pass


@router.put("/questions, {answer_id}", tags=["Questions"])
async def update_answer():
    pass


@router.delete("/questions, {answer_id}", tags=["Questions"])
async def delete_answer():
    pass

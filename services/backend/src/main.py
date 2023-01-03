from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.db_connect import engine, database, metadata
from src.routes.user import users
from src.routes.tag import tags
from src.routes.question import questions
from src.routes.answer import answers
from src.routes.vote import votes


metadata.create_all(engine)

app = FastAPI(title="QuizBox")

# CORSHeaders
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.router, prefix="/Users", tags=["Users"])
app.include_router(tags.router, prefix="/tags", tags=["Tags"])
app.include_router(answers.router, prefix="/Answers", tags=["Answers"])
app.include_router(questions.router, prefix="/Questions", tags=["Questions"])
app.include_router(votes.router, prefix="/Votes", tags=["Votes"])

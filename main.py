from fastapi import FastAPI
from app.routers import answer, questions, tags, users

app = FastAPI(title="QuizBox")

app.include_router(answer.router)
app.include_router(questions.router)
app.include_router(tags.router)
app.include_router(users.router)

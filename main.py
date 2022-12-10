from fastapi import FastAPI
from app.routers import answer, question, tag, user

app = FastAPI(title="QuizBox")

app.include_router(answer.router)
app.include_router(question.router)
app.include_router(tag.router)
app.include_router(user.router)

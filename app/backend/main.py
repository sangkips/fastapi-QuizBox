from fastapi import FastAPI

from app.backend.routers import answer, question, tag, user, vote
from app.backend.db.database import engine
from app.backend.models import answers, questions, tags, users, votes

answers.Base.metadata.create_all(bind=engine)
questions.Base.metadata.create_all(bind=engine)
tags.Base.metadata.create_all(bind=engine)
users.Base.metadata.create_all(bind=engine)
votes.Base.metadata.create_all(bind=engine)


app = FastAPI(title="QuizBox")

app.include_router(answer.router)
app.include_router(question.router)
app.include_router(tag.router)
app.include_router(user.router)
app.include_router(vote.router)

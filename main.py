from fastapi import FastAPI

from app.routers import _user, answer, question, tag, vote
from app.db.database import engine
from app.models import answers, questions, tags, users, votes

answers.Base.metadata.create_all(bind=engine)
questions.Base.metadata.create_all(bind=engine)
tags.Base.metadata.create_all(bind=engine)
users.Base.metadata.create_all(bind=engine)
votes.Base.metadata.create_all(bind=engine)


app = FastAPI(title="QuizBox")

app.include_router(answer.router)
app.include_router(question.router)
app.include_router(tag.router)
app.include_router(_user.router)
app.include_router(vote.router)

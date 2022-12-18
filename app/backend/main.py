from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine
from models import answers, questions, tags, users, votes
from routers import answer, question, tag, user, vote


answers.Base.metadata.create_all(bind=engine)
questions.Base.metadata.create_all(bind=engine)
tags.Base.metadata.create_all(bind=engine)
users.Base.metadata.create_all(bind=engine)
votes.Base.metadata.create_all(bind=engine)


app = FastAPI(title="QuizBox")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(answer.router)
app.include_router(question.router)
app.include_router(tag.router)
app.include_router(user.router)
app.include_router(vote.router)

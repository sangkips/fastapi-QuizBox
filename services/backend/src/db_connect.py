import os

from sqlalchemy import create_engine, MetaData
from databases import Database


from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Table,
    Boolean,
    Text,
    ForeignKey,
    Enum,
)
from sqlalchemy.sql import func

from src.routes.vote.models import Like

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, unique=True),
    Column("is_active", Boolean, default=True),
    Column("password", String),
    Column("first_name", String),
    Column("last_name", String),
    Column("created_date", DateTime, default=func.now(), nullable=False),
    Column("updated_date", DateTime, default=func.now(), nullable=False),

)

tags = Table(
    "tags",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=False, index=True),
)

questions = Table(
    "questions",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String(100), nullable=False, index=True),
    Column("body", Text, nullable=False, index=True),
    Column("user_id", Integer, ForeignKey(
        "users.id"), nullable=False, index=True),
    Column("tag_id", Integer, ForeignKey(
        "tags.id"), nullable=False, index=True),
)

answers = Table(
    "answers",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("body", Text, nullable=False, index=True),
    Column("user_id", Integer, ForeignKey("users.id"),
           nullable=False, index=True),
    Column("question_id", Integer, ForeignKey("questions.id"), nullable=False),
)

votes = Table(
    "votes",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, index=True),
    Column("question_id", Integer, index=True),
    Column("answer_id", Integer, index=True),
    Column("like", Enum(Like), index=True),
)

database = Database(DATABASE_URL)

import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum

from db.database import Base

from .mixins import Timestamp


class Like(enum.IntEnum):
    down = 1
    up = 2


class Vote(Timestamp, Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    like = Column(Enum(Like))
    question_id = Column(Integer, ForeignKey(
        "questions.id"), index=True, nullable=True)
    answer_id = Column(Integer, ForeignKey(
        "answers.id"), nullable=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"),
                     nullable=False, index=True)

import enum

from sqlalchemy import Column, Integer, Enum

from app.db.database import Base

from .mixins import Timestamp


class Like(enum.Enum):
    down = "Down"
    up = "Up"


class Vote(Timestamp, Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    like = Column(Enum(Like))

from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from app.db.database import Base
from .users import User
from .questions import Question

from .mixins import Timestamp


class Answer(Timestamp, Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(Text, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    vote_id = Column(Integer, ForeignKey("votes.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)

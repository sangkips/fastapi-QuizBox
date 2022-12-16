from sqlalchemy import Column, ForeignKey, Integer, String, Text
from app.db.database import Base

from .mixins import Timestamp


class Question(Timestamp, Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    body = Column(Text, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False, index=True)
    vote_id = Column(Integer, ForeignKey("votes.id"), nullable=True, index=True)

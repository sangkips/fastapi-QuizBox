from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.database import Base
from .users import User
from .tags import Tag

from .mixins import Timestamp


class Question(Timestamp, Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    body = Column(Text, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    ask_by = relationship(User)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)

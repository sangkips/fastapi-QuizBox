from sqlalchemy import Column, Integer, String

from app.backend.db.database import Base

from .mixins import Timestamp


class Tag(Timestamp, Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, index=True)

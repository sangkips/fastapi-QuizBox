""" 
Mixins for holding all the timestamps such as created_at, updated_at. this will enable
us not to define when an item was created in all models.

"""

from datetime import datetime

from sqlalchemy import DateTime, Column
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class Timestamp:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

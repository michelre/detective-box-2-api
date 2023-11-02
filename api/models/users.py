from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, ForeignKey, Enum
from api.database import Base
from api.enums import BoxStatus
from api.models.box import Box

from typing import List


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    # boxes: Mapped[List[Box]] = relationship(UserBox)
